"""Tests for python-pptx-theme-kit.

Run with: pytest tests/
"""

import warnings
import tempfile
import os

import pytest
from PIL import Image as PILImage

from python_pptx_theme_kit import (
    Presentation,
    Inches,
    REQUIRED_PALETTE_KEYS,
    get_palette,
    list_palettes,
    make_blocks,
    make_primitives,
    detect_overlaps,
    format_overlaps,
)
from python_pptx_theme_kit.primitives import _Namespace


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def palette():
    return get_palette("catppuccin_mocha")


@pytest.fixture
def prs():
    p = Presentation()
    p.slide_width = Inches(13.33)
    p.slide_height = Inches(7.5)
    return p


@pytest.fixture
def pr(palette):
    return make_primitives(palette)


@pytest.fixture
def bl(palette):
    return make_blocks(palette)


@pytest.fixture
def slide(prs, pr):
    return pr.blank_slide(prs)


@pytest.fixture
def test_image(tmp_path):
    """Return path to a 400×300 test PNG image."""
    img_path = tmp_path / "test.png"
    img = PILImage.new("RGB", (400, 300), color=(100, 150, 200))
    img.save(str(img_path))
    return str(img_path)


@pytest.fixture
def wide_test_image(tmp_path):
    """Return path to a wide (800×200) test PNG image."""
    img_path = tmp_path / "wide.png"
    img = PILImage.new("RGB", (800, 200), color=(200, 100, 50))
    img.save(str(img_path))
    return str(img_path)


# ── Palette API ───────────────────────────────────────────────────────────────

def test_list_palettes_returns_sorted():
    names = list_palettes()
    assert names == sorted(names)
    assert "catppuccin_mocha" in names
    assert len(names) >= 6


def test_get_palette_valid():
    p = get_palette("nord_frost")
    assert "ACCENT" in p


def test_get_palette_invalid():
    with pytest.raises(ValueError, match="Unknown palette"):
        get_palette("not_a_palette")


def test_get_palette_returns_copy():
    """Mutating the returned dict must not affect subsequent calls."""
    p1 = get_palette("catppuccin_mocha")
    original_accent = p1["ACCENT"]
    p1["ACCENT"] = None
    p2 = get_palette("catppuccin_mocha")
    assert p2["ACCENT"] == original_accent


def test_all_palettes_have_required_keys():
    for name in list_palettes():
        p = get_palette(name)
        assert REQUIRED_PALETTE_KEYS <= set(p.keys()), (
            f"Palette '{name}' is missing keys: {REQUIRED_PALETTE_KEYS - set(p.keys())}"
        )


# ── make_primitives validation ────────────────────────────────────────────────

def test_make_primitives_missing_key_raises():
    bad = {k: None for k in REQUIRED_PALETTE_KEYS - {"CARD_BG"}}
    with pytest.raises(ValueError, match="CARD_BG"):
        make_primitives(bad)


def test_make_primitives_extra_keys_ok(palette):
    extended = dict(palette, EXTRA_KEY="unused")
    pr = make_primitives(extended)
    assert pr is not None


# ── _Namespace ────────────────────────────────────────────────────────────────

def test_make_primitives_returns_namespace(palette):
    pr = make_primitives(palette)
    assert isinstance(pr, _Namespace)


def test_namespace_dict_access(palette):
    pr = make_primitives(palette)
    assert callable(pr["add_text"])


def test_namespace_attr_access(palette):
    pr = make_primitives(palette)
    assert callable(pr.add_text)


def test_namespace_dict_and_attr_are_same_object(palette):
    pr = make_primitives(palette)
    assert pr["add_text"] is pr.add_text


def test_namespace_missing_attr_raises():
    ns = _Namespace({"a": 1})
    with pytest.raises(AttributeError):
        _ = ns.nonexistent


def test_namespace_dir_includes_keys(palette):
    pr = make_primitives(palette)
    d = dir(pr)
    assert "add_text" in d
    assert "add_image" in d


def test_make_blocks_returns_namespace(palette):
    bl = make_blocks(palette)
    assert isinstance(bl, _Namespace)
    assert bl["slide_chrome_block"] is bl.slide_chrome_block


# ── add_image: native mode with both dimensions ───────────────────────────────

def test_add_image_native_both_dimensions_no_error(prs, pr, slide, test_image):
    """native fit with both width and height must not raise and must honour dimensions."""
    pic = pr.add_image(
        slide, test_image,
        Inches(1), Inches(1),
        width=Inches(3), height=Inches(2),
        fit="native",
    )
    assert pic.width == Inches(3)
    assert pic.height == Inches(2)


def test_add_image_invalid_fit_raises(prs, pr, slide, test_image):
    with pytest.raises(ValueError, match="Unsupported fit mode"):
        pr.add_image(slide, test_image, Inches(1), Inches(1),
                     width=Inches(3), height=Inches(2), fit="invalid")


def test_add_image_missing_file_raises(pr, slide):
    with pytest.raises(FileNotFoundError):
        pr.add_image(slide, "/nonexistent/path/image.png", Inches(1), Inches(1))


# ── add_image: cover mode uses PIL, not _element hack ────────────────────────

def test_add_image_cover_adds_exactly_one_shape(prs, pr, slide, test_image):
    """Cover mode must add exactly one picture shape (no lingering probe shape)."""
    before = len(slide.shapes)
    pr.add_image(
        slide, test_image,
        Inches(1), Inches(1),
        width=Inches(4), height=Inches(2),
        fit="cover",
    )
    assert len(slide.shapes) == before + 1


def test_add_image_cover_wide_image_crops_horizontally(prs, pr, slide, wide_test_image):
    """A 4:1 image in a square frame should produce non-zero horizontal crop."""
    pic = pr.add_image(
        slide, wide_test_image,
        Inches(1), Inches(1),
        width=Inches(2), height=Inches(2),  # square frame, wide image
        fit="cover",
    )
    # The wide image should be cropped on the sides
    assert pic.crop_left > 0 or pic.crop_right > 0


# ── data_source_cards_block: warn on truncation ───────────────────────────────

def test_data_source_cards_warns_extra_sources(prs, bl, pr):
    slide = pr.blank_slide(prs)
    sources = [
        ("A", "id-a", "meta", []),
        ("B", "id-b", "meta", []),
        ("C", "id-c", "meta", []),
        ("D", "id-d", "meta", []),  # extra
    ]
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        bl.data_source_cards_block(slide, sources, columns=3)
    assert any("4 sources" in str(w.message) for w in caught)


def test_data_source_cards_no_warning_when_count_matches(prs, bl, pr):
    slide = pr.blank_slide(prs)
    sources = [("A", "id-a", "meta", []), ("B", "id-b", "meta", [])]
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        bl.data_source_cards_block(slide, sources, columns=2)
    assert not any("sources" in str(w.message) for w in caught)


# ── coverage_table_block: warn on short status tuples ─────────────────────────

def test_coverage_table_warns_short_statuses(prs, bl, pr):
    slide = pr.blank_slide(prs)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        bl.coverage_table_block(
            slide,
            ["Attr", "Src A", "Src B"],
            [("field", ("Y",))],  # 1 status for 2 source columns
        )
    assert any("missing cells" in str(w.message) for w in caught)


def test_coverage_table_no_warning_when_statuses_match(prs, bl, pr):
    slide = pr.blank_slide(prs)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        bl.coverage_table_block(
            slide,
            ["Attr", "Src A", "Src B"],
            [("field", ("Y", "-"))],  # correct count
        )
    assert not any("missing cells" in str(w.message) for w in caught)


# ── detect_overlaps / format_overlaps ─────────────────────────────────────────

def test_detect_overlaps_returns_list(prs, bl, pr):
    slide = pr.blank_slide(prs)
    bl.slide_chrome_block(slide, title="Test", footer_text="footer")
    findings = detect_overlaps(prs, min_overlap_ratio=0.02)
    assert isinstance(findings, list)


def test_format_overlaps_empty():
    assert format_overlaps([]) == []


def test_format_overlaps_structure():
    fake = [{
        "slide": 1, "shape_a": "ShapeA", "shape_b": "ShapeB",
        "overlap_area": 1000, "overlap_ratio_a": 0.5, "overlap_ratio_b": 0.3,
    }]
    lines = format_overlaps(fake)
    assert len(lines) == 1
    assert "Slide 1" in lines[0]
    assert "ShapeA" in lines[0]
    assert "50.0%" in lines[0]


# ── Smoke test: full mini-presentation ────────────────────────────────────────

def test_basic_presentation_builds_and_saves(tmp_path, palette):
    """A minimal deck using attribute-style access must save without error."""
    pr = make_primitives(palette)
    bl = make_blocks(palette)

    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    slide = pr.blank_slide(prs)
    bl.slide_chrome_block(slide, title="Test Slide", footer_text="footer")
    bl.toc_list_block(slide, [("1", "Introduction", "Slide 2")])

    output = tmp_path / "smoke_test.pptx"
    prs.save(str(output))
    assert output.exists()
    assert output.stat().st_size > 5000
