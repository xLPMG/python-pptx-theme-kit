"""Extensive multi-slide example showcasing most available design patterns."""

from python_pptx_theme_kit import (
    Presentation,
    Inches,
    PP_ALIGN,
    detect_overlaps,
    format_overlaps,
    make_blocks,
    get_palette,
    make_primitives,
)


SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)


def main():
    palette = get_palette("catppuccin_mocha")
    p = make_primitives(palette)
    b = make_blocks(palette)

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # ── Slide 1: Hero ──────────────────────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](slide, show_title_bar=False)
    b["hero_banner_block"](
        slide,
        "Write Your Amazing Title Here",
        "A subtitle that describes the topic in a compelling way",
        "Organisation  ·  Department  ·  Year",
        "Objective: demonstrate reusable slide design patterns with python-pptx-theme-kit.",
    )

    # ── Slide 2: Table of Contents ─────────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Table of Contents",
        subtitle="Overview of slides and section structure",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 2",
    )
    sections = [
        ("1", "Introduction & Motivation",       "Slide 1"),
        ("2", "Data Sources Overview",           "Slide 3"),
        ("3", "Attribute Coverage Comparison",   "Slide 4"),
        ("4", "Architecture & Pipeline",         "Slide 5"),
        ("5", "Code Example & Status Snapshot",  "Slide 6"),
        ("6", "Two-Column Analysis Frame",       "Slide 7"),
        ("7", "Image Support Demo",              "Slide 8"),
        ("8", "Image Fit Modes",                 "Slide 9"),
        ("9", "Known Limitations",               "Slide 10"),
        ("10", "Summary",                        "Slide 11"),
    ]
    b["toc_list_block"](slide, sections)

    # ── Slide 3: Data Sources Overview ─────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Data Sources Overview",
        subtitle="Three example sources with complementary attributes",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 3",
    )
    sources = [
        ("Source A", "primary-provider/dataset-alpha", "64 000 records  ·  8 attributes", [
            ("id",          "→ id",         False),
            ("name",        "→ title",      False),
            ("category",    "→ category",   False),
            ("score",       "→ score",      False),
            ("release",     "→ date",       False),
            ("region",      "NULL",         True),
            ("internal_id", "NULL",         True),
            ("vendor",      "→ publisher",  False),
        ]),
        ("Source B", "secondary-provider/dataset-beta", "18 800 records  ·  5 attributes", [
            ("title",       "→ title",      False),
            ("platform",    "→ platform",   False),
            ("date",        "→ date",       False),
            ("description", "→ summary",    False),
            ("user_rating", "→ user_score", False),
        ]),
        ("Source C", "tertiary-provider/dataset-gamma", "14 000 records  ·  6 attributes", [
            ("Title",   "→ title",     False),
            ("Launch",  "→ date",      False),
            ("Creator", "→ developer", False),
            ("Label",   "→ publisher", False),
            ("Tags",    "→ category",  False),
            ("Rating",  "→ rating",    False),
        ]),
    ]
    b["data_source_cards_block"](slide, sources)

    # ── Slide 4: Attribute Coverage Comparison ─────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Attribute Coverage Comparison",
        subtitle="Which attributes are provided by which sources?",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 4",
    )
    col_headers = ["Attribute", "Source A", "Source B", "Source C"]
    rows = [
        ("title", ("✓", "✓", "✓")),
        ("platform", ("✓", "✓", "-")),
        ("date", ("✓", "✓", "✓")),
        ("developer", ("-", "-", "✓")),
        ("publisher", ("✓", "-", "✓")),
        ("category", ("✓", "-", "✓")),
        ("score", ("✓", "-", "-")),
        ("user_score", ("-", "✓", "-")),
        ("rating", ("-", "-", "✓")),
        ("summary", ("-", "✓", "-")),
    ]
    b["coverage_table_block"](
        slide,
        col_headers,
        rows,
        insight_text="Key insight: No single source is complete. Integration across all three is required for full coverage.",
        status_positive="✓",
        status_negative="-",
    )
    # ── Slide 5: Architecture Pipeline ─────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Architecture & Pipeline",
        subtitle="Extract → Map → Normalize → Match → Merge → Output",
        footer_text="GAV integration: target schema is defined first; each source is mapped into it independently",
    )
    stages = [
        ("EXTRACT",   "loader.py",    "Download\n& load CSVs"),
        ("MAP",       "mapping.py",   "NULL / 1:1 / 1:n\nattribute mapping"),
        ("NORMALIZE", "normalize.py", "Dates, scores\n& identifiers"),
        ("MATCH",     "resolver.py",  "Blocking + fuzzy\ngreedy matching"),
        ("MERGE",     "resolver.py",  "Conflict resolution\n+ provenance"),
        ("OUTPUT",    "main.py",      "Sorted, deduped\nCSV dataset"),
    ]
    b["pipeline_stages_block"](slide, stages)
    b["pipeline_strategy_block"](
        slide,
        "Pairwise Integration Strategy",
        "Sources are not merged all at once. A two-step pairwise approach is used:\n  Step A:  Source A  ⊕  Source B  →  Intermediate result\n  Step B:  Intermediate  ⊕  Source C  →  Final integrated dataset",
        "# main.py – orchestration\ndf_intermediate = merge(source_a, source_b)\nfinal_df        = merge(df_intermediate, source_c)\nfinal_df.sort_values('title').to_csv('output.csv', index=False)",
    )
    # ── Slide 6: Code + Metrics ─────────────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Code Example & Status Snapshot",
        subtitle="Full function alongside operational metrics",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 6",
    )
    b["code_status_block"](
        slide,
        "def hello_world():\n    \"\"\"Print a greeting and return it.\"\"\"\n    message = 'This slide talks about an interesting topic'\n    print(message)\n    return message\n\nif __name__ == '__main__':\n    result = hello_world()\n    print(f'Done: {result}')",
        [
            ("Theme", "catppuccin_mocha"),
            ("Slides Built", "11"),
            ("Primitives Used", "11 / 11"),
            ("Export Mode", "PowerPoint (.pptx)"),
        ],
    )
    # ── Slide 7: Two-Column Analysis Frame ─────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Analysis Frame",
        subtitle="Left: challenges, Right: solutions",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 7",
    )
    b["two_column_panel_block"](
        slide,
        "Challenges",
        [
            "Decks look inconsistent across teams",
            "Manual styling slows iteration cycles",
            "Code snippets are hard to format clearly",
            "Layout bugs are hard to detect visually",
        ],
        "Solutions",
        [
            "Use primitives as composable building blocks",
            "Apply a palette once, reuse everywhere",
            "add_code() auto-fits font size to box height",
            "detect_overlaps() flags layout collisions early",
        ],
    )

    # ── Slide 8: Image Support Demo ────────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Image Support Demo",
        subtitle="Using add_image() via image_caption_card_block",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 8",
    )
    b["image_caption_card_block"](
        slide,
        "examples/jupiter.jpg",
        "Jupiter Atmospheric Layers",
        "Image loaded from local file and placed in a framed card using fit='cover'.\nUse fit='contain' to preserve full image without crop.",
        height=Inches(5.5),
        image_ratio=0.72,
    )

    # ── Slide 9: Image Fit Modes ───────────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Image Fit Modes",
        subtitle="Comparing cover, contain, stretch, and native (width-only)",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 9",
    )

    card_w = Inches(6.15)
    card_h = Inches(2.7)
    gap_x = Inches(0.3)
    top_1 = Inches(1.2)
    top_2 = Inches(4.0)
    left_1 = Inches(0.35)
    left_2 = left_1 + card_w + gap_x

    cards = [
        ("cover", left_1, top_1, "cover", True),
        ("contain", left_2, top_1, "contain", True),
        ("stretch", left_1, top_2, "stretch", True),
        ("native", left_2, top_2, "native", False),
    ]

    for name, left, top, fit_mode, use_frame in cards:
        p["add_rect"](slide, left, top, card_w, card_h, palette["CARD_BG"], line_color=palette["ACCENT"])
        p["add_text"](
            slide,
            f"fit='{fit_mode}'",
            left + Inches(0.12),
            top + Inches(0.07),
            card_w - Inches(0.24),
            Inches(0.28),
            size=12,
            bold=True,
            color=palette["ACCENT2"],
        )
        image_left = left + Inches(0.12)
        image_top = top + Inches(0.42)
        image_w = card_w - Inches(0.24)
        image_h = Inches(1.9)

        if use_frame:
            p["add_image"](
                slide,
                "examples/jupiter.jpg",
                image_left,
                image_top,
                width=image_w,
                height=image_h,
                fit=fit_mode,
                border_color=palette["ACCENT3"],
            )
        else:
            p["add_image"](
                slide,
                "examples/jupiter.jpg",
                image_left,
                image_top,
                width=Inches(1.95),
                fit=fit_mode,
                border_color=palette["ACCENT3"],
            )

        desc = "fills frame with crop" if fit_mode == "cover" else (
            "preserves full image" if fit_mode == "contain" else (
                "forces exact frame size" if fit_mode == "stretch" else "preserves ratio from native image"
            )
        )
        p["add_text"](
            slide,
            desc,
            left + Inches(0.12),
            top + Inches(2.44),
            card_w - Inches(0.24),
            Inches(0.24),
            size=10,
            italic=True,
            color=palette["SUBTITLE_C"],
            align=PP_ALIGN.CENTER,
        )

    # ── Slide 10: Known Limitations (left-border card pattern) ─────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Known Limitations",
        subtitle="Design decisions and their trade-offs",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 10",
    )
    limitations = [
        ("Fixed slide dimensions",  "All primitives assume 13.33 × 7.5 in widescreen. Changing dimensions requires recalibrating all spacing constants.",                         palette["ACCENT3"]),
        ("No auto-layout engine",   "Element positions are hand-coded in EMU/Inches. Overlaps must be detected and fixed manually or via detect_overlaps().",                    palette["ACCENT4"]),
        ("Single-run text boxes",   "add_text() renders one styled run per box. Mixed formatting in one line requires separate non-overlapping boxes.",                          palette["ACCENT"]),
        ("Code truncation visible", "add_code() appends '...' when lines overflow the box height. Prefer sizing boxes generously or setting a lower min_size.",                 palette["ACCENT2"]),
        ("Palette coupling",        "Primitive colors are closed over at make_primitives() time. Switching palette mid-deck requires instantiating a second primitives dict.",   palette["SUBTITLE_C"]),
    ]
    b["left_border_card_list_block"](slide, limitations)

    # ── Slide 11: Summary ──────────────────────────────────────────────────
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Summary",
        subtitle="",
        footer_text="python-pptx-theme-kit · design patterns demo · slide 11",
    )
    p["add_rect"](slide, 0, Inches(1.05), SLIDE_W, Inches(0.05), palette["ACCENT"])
    summary_items = [
        ("Palette",       "get_palette() provides a cohesive color system shared across all primitives",                        palette["ACCENT3"]),
        ("Primitives",    "make_primitives() returns 10 composable helpers covering all common slide elements",                  palette["ACCENT4"]),
        ("Title bar",     "title_bar() renders a full-width header with title and optional subtitle line",                      palette["ACCENT"]),
        ("Section label", "section_label() places a bold heading — position and width are now caller-controlled",               palette["ACCENT"]),
        ("Bullet block",  "bullet_block() renders a styled multi-line list with a configurable bullet marker",                  palette["ACCENT2"]),
        ("Code panel",    "add_code() auto-fits font size and truncates gracefully when lines exceed box height",                palette["ACCENT2"]),
        ("Info rows",     "info_row() draws alternating-stripe key/value rows for compact metrics summaries",                   palette["ACCENT3"]),
        ("Overlap check", "detect_overlaps() + format_overlaps() report layout collisions after deck generation",               palette["ACCENT4"]),
        ("Output",        "prs.save() writes a fully themed, overlap-checked .pptx ready to open in PowerPoint",               palette["ACCENT"]),
    ]
    b["left_border_card_list_block"](
        slide,
        summary_items,
        top=Inches(1.2),
        row_height=Inches(0.6),
        row_gap=Inches(0.01),
        title_width=Inches(2.2),
        title_size=12,
        desc_size=12,
        alternating_bg=True,
    )
    output = "example_slide_showcase.pptx"
    prs.save(output)
    print(f"Saved: {output}  ({len(prs.slides)} slides)")

    findings = detect_overlaps(prs, min_overlap_ratio=0.02)
    if findings:
        print("Potential overlapping elements:")
        for line in format_overlaps(findings):
            print(f"- {line}")
    else:
        print("No significant overlaps detected.")


if __name__ == "__main__":
    main()
