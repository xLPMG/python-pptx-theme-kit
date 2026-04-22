"""Extensive multi-slide example showcasing most available design patterns."""

from python_pptx_theme_kit import (
    Presentation,
    Inches,
    PP_ALIGN,
    detect_overlaps,
    format_overlaps,
    get_palette,
    make_primitives,
)


SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)


def main():
    palette = get_palette("catppuccin_mocha")
    p = make_primitives(palette)

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # ── Slide 1: Hero ──────────────────────────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["add_rect"](slide, 0, Inches(2.3), SLIDE_W, Inches(2.9), palette["ACCENT"])
    p["add_text"](slide, "Write Your Amazing Title Here", Inches(0.5), Inches(2.45), Inches(12.3), Inches(1.0), size=46, bold=True, color=palette["DARK_BG"], align=PP_ALIGN.CENTER)
    p["add_text"](slide, "A subtitle that describes the topic in a compelling way", Inches(0.5), Inches(3.45), Inches(12.3), Inches(0.6), size=22, italic=True, color=palette["DARK_BG"], align=PP_ALIGN.CENTER)
    p["add_text"](slide, "Organisation  ·  Department  ·  Year", Inches(0.5), Inches(5.8), Inches(12.3), Inches(0.4), size=13, color=palette["SUBTITLE_C"], align=PP_ALIGN.CENTER)
    p["add_text"](slide, "Objective: demonstrate reusable slide design patterns with python-pptx-theme-kit.", Inches(1.0), Inches(6.3), Inches(11.3), Inches(0.5), size=12, italic=True, color=palette["LIGHT_GREY"], align=PP_ALIGN.CENTER)

    # ── Slide 2: Table of Contents ─────────────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Table of Contents", "Overview of slides and section structure")
    sections = [
        ("1", "Introduction & Motivation",       "Slide 1"),
        ("2", "Data Sources Overview",           "Slide 3"),
        ("3", "Attribute Coverage Comparison",   "Slide 4"),
        ("4", "Architecture & Pipeline",         "Slide 5"),
        ("5", "Code Example & Status Snapshot",  "Slide 6"),
        ("6", "Two-Column Analysis Frame",       "Slide 7"),
        ("7", "Known Limitations",               "Slide 8"),
        ("8", "Summary",                         "Slide 9"),
    ]
    y = Inches(1.15)
    for num, section, pages in sections:
        bg = palette["CARD_BG"] if int(num) % 2 == 0 else palette["ROW_B"]
        p["add_rect"](slide, Inches(0.35), y, Inches(12.6), Inches(0.52), bg)
        p["add_rect"](slide, Inches(0.35), y, Inches(0.52), Inches(0.52), palette["ACCENT"])
        p["add_text"](slide, num, Inches(0.35), y, Inches(0.52), Inches(0.52), size=13, bold=True, color=palette["DARK_BG"], align=PP_ALIGN.CENTER)
        p["add_text"](slide, section, Inches(0.97), y + Inches(0.1), Inches(9.9), Inches(0.35), size=13, color=palette["WHITE"])
        p["add_text"](slide, pages, Inches(11.0), y + Inches(0.1), Inches(1.9), Inches(0.35), size=12, italic=True, color=palette["SUBTITLE_C"], align=PP_ALIGN.RIGHT)
        y += Inches(0.57)
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 2")

    # ── Slide 3: Data Sources Overview ─────────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Data Sources Overview", "Three example sources with complementary attributes")
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
    card_w = Inches(4.08)
    gap = Inches(0.2)
    rh = Inches(0.33)
    card_top = Inches(1.15)
    card_h = Inches(3.85)
    for ci, (ds_name, source_id, meta, attrs) in enumerate(sources):
        x = Inches(0.35) + ci * (card_w + gap)
        p["add_rect"](slide, x, card_top, card_w, card_h, palette["CARD_BG"])
        p["add_text"](slide, ds_name, x + Inches(0.1), card_top + Inches(0.05), card_w - Inches(0.2), Inches(0.3), size=13, bold=True, color=palette["ACCENT"])
        p["add_text"](slide, source_id, x + Inches(0.1), card_top + Inches(0.37), card_w - Inches(0.2), Inches(0.25), size=8, color=palette["SUBTITLE_C"])
        p["add_text"](slide, meta, x + Inches(0.1), card_top + Inches(0.63), card_w - Inches(0.2), Inches(0.22), size=10, bold=True, color=palette["ACCENT3"])
        p["add_rect"](slide, x + Inches(0.06), card_top + Inches(0.9), card_w - Inches(0.12), Inches(0.02), palette["ACCENT"])
        y = card_top + Inches(0.96)
        attr_w = card_w * 0.44
        map_w = card_w * 0.53
        for i, (attr, mapping, is_null) in enumerate(attrs):
            bg = palette["ROW_A"] if i % 2 == 0 else palette["ROW_B"]
            p["add_rect"](slide, x + Inches(0.06), y, card_w - Inches(0.12), rh, bg)
            p["add_text"](slide, attr, x + Inches(0.1), y + Inches(0.04), attr_w - Inches(0.05), rh - Inches(0.04), size=10, bold=True, color=palette["LIGHT_GREY"] if is_null else palette["WHITE"])
            p["add_text"](slide, mapping, x + attr_w + Inches(0.08), y + Inches(0.04), map_w - Inches(0.1), rh - Inches(0.04), size=10, color=palette["ACCENT3"] if is_null else palette["ACCENT2"])
            y += rh
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 3")

    # ── Slide 4: Attribute Coverage Comparison ─────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Attribute Coverage Comparison", "Which attributes are provided by which sources?")
    attrs_list = ["title", "platform", "date", "developer", "publisher", "category", "score", "user_score", "rating", "summary"]
    col_headers = ["Attribute", "Source A", "Source B", "Source C"]
    coverage = {
        "title":      ("✓", "✓", "✓"),
        "platform":   ("✓", "✓", "—"),
        "date":       ("✓", "✓", "✓"),
        "developer":  ("—", "—", "✓"),
        "publisher":  ("✓", "—", "✓"),
        "category":   ("✓", "—", "✓"),
        "score":      ("✓", "—", "—"),
        "user_score": ("—", "✓", "—"),
        "rating":     ("—", "—", "✓"),
        "summary":    ("—", "✓", "—"),
    }
    hx = [Inches(0.35), Inches(4.5), Inches(7.5), Inches(10.5)]
    hw = [Inches(4.0), Inches(2.85), Inches(2.85), Inches(2.35)]
    p["add_rect"](slide, Inches(0.35), Inches(1.15), Inches(12.6), Inches(0.4), palette["ACCENT"])
    for i, col in enumerate(col_headers):
        p["add_text"](slide, col, hx[i] + Inches(0.05), Inches(1.18), hw[i], Inches(0.35), size=12, bold=True, color=palette["DARK_BG"])
    y = Inches(1.55)
    row_h = Inches(0.43)
    for j, attr in enumerate(attrs_list):
        cov = coverage[attr]
        bg = palette["ROW_A"] if j % 2 == 0 else palette["ROW_B"]
        p["add_rect"](slide, Inches(0.35), y, Inches(12.6), row_h, bg)
        p["add_text"](slide, attr, hx[0] + Inches(0.05), y + Inches(0.07), hw[0], row_h - Inches(0.07), size=12, bold=True, color=palette["WHITE"])
        for k, val in enumerate(cov):
            c = palette["ACCENT2"] if val.startswith("✓") else palette["ACCENT3"]
            p["add_text"](slide, val, hx[k + 1] + Inches(0.05), y + Inches(0.07), hw[k + 1], row_h - Inches(0.07), size=12, color=c)
        y += row_h
    p["add_rect"](slide, Inches(0.35), Inches(5.95), Inches(12.6), Inches(0.45), palette["ROW_A"])
    p["add_text"](slide, "Key insight: No single source is complete. Integration across all three is required for full coverage.", Inches(0.55), Inches(6.0), Inches(12.2), Inches(0.35), size=12, bold=True, color=palette["ACCENT2"])
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 4")

    # ── Slide 5: Architecture Pipeline ─────────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Architecture & Pipeline", "Extract → Map → Normalize → Match → Merge → Output")
    stages = [
        ("EXTRACT",   "loader.py",    "Download\n& load CSVs"),
        ("MAP",       "mapping.py",   "NULL / 1:1 / 1:n\nattribute mapping"),
        ("NORMALIZE", "normalize.py", "Dates, scores\n& identifiers"),
        ("MATCH",     "resolver.py",  "Blocking + fuzzy\ngreedy matching"),
        ("MERGE",     "resolver.py",  "Conflict resolution\n+ provenance"),
        ("OUTPUT",    "main.py",      "Sorted, deduped\nCSV dataset"),
    ]
    box_w = Inches(1.75)
    box_h = Inches(1.3)
    y_box = Inches(2.0)
    arrow_gap = Inches(0.28)
    x = Inches(0.4)
    for i, (stage, script, desc) in enumerate(stages):
        p["add_rect"](slide, x, y_box, box_w, box_h, palette["CARD_BG"], line_color=palette["ACCENT"])
        p["add_text"](slide, stage, x + Inches(0.05), y_box + Inches(0.05), box_w - Inches(0.1), Inches(0.35), size=10, bold=True, color=palette["ACCENT"], align=PP_ALIGN.CENTER)
        p["add_text"](slide, script, x + Inches(0.05), y_box + Inches(0.4), box_w - Inches(0.1), Inches(0.28), size=8, color=palette["ACCENT3"], align=PP_ALIGN.CENTER)
        p["add_text"](slide, desc, x + Inches(0.05), y_box + Inches(0.68), box_w - Inches(0.1), Inches(0.55), size=9, color=palette["LIGHT_GREY"], align=PP_ALIGN.CENTER)
        if i < len(stages) - 1:
            p["add_text"](slide, ">", x + box_w, y_box + box_h / 2 - Inches(0.11), arrow_gap, Inches(0.22), size=13, bold=True, color=palette["ACCENT"], align=PP_ALIGN.CENTER)
        x += box_w + arrow_gap
    p["add_rect"](slide, Inches(0.35), Inches(3.55), Inches(12.6), Inches(1.35), palette["ROW_B"])
    p["section_label"](slide, "Pairwise Integration Strategy", Inches(0.55), Inches(3.62), Inches(12.2))
    p["add_text"](slide, "Sources are not merged all at once. A two-step pairwise approach is used:\n  Step A:  Source A  ⊕  Source B  →  Intermediate result\n  Step B:  Intermediate  ⊕  Source C  →  Final integrated dataset", Inches(0.55), Inches(3.98), Inches(12.2), Inches(0.82), size=12, color=palette["LIGHT_GREY"])
    p["add_code"](slide, "# main.py – orchestration\ndf_intermediate = merge(source_a, source_b)\nfinal_df        = merge(df_intermediate, source_c)\nfinal_df.sort_values('title').to_csv('output.csv', index=False)", Inches(0.35), Inches(5.08), Inches(12.6), Inches(1.65), size=12, wrap=True)
    p["footer"](slide, "GAV integration: target schema is defined first; each source is mapped into it independently")

    # ── Slide 6: Code + Metrics ─────────────────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Code Example & Status Snapshot", "Full function alongside operational metrics")
    p["section_label"](slide, "Implementation", Inches(0.6), Inches(1.25), Inches(6.0))
    p["add_code"](slide, "def hello_world():\n    \"\"\"Print a greeting and return it.\"\"\"\n    message = 'This slide talks about an interesting topic'\n    print(message)\n    return message\n\nif __name__ == '__main__':\n    result = hello_world()\n    print(f'Done: {result}')", Inches(0.6), Inches(1.65), Inches(12.2), Inches(2.5), size=12, wrap=True)
    p["section_label"](slide, "Status Snapshot", Inches(0.6), Inches(4.35), Inches(6.0))
    p["info_row"](slide, "Theme",           "catppuccin_mocha",   Inches(4.7),  lw=Inches(2.4))
    p["info_row"](slide, "Slides Built",    "9",                  Inches(5.22), lw=Inches(2.4))
    p["info_row"](slide, "Primitives Used", "10 / 10",            Inches(5.74), lw=Inches(2.4))
    p["info_row"](slide, "Export Mode",     "PowerPoint (.pptx)", Inches(6.26), lw=Inches(2.4))
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 6")

    # ── Slide 7: Two-Column Analysis Frame ─────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Analysis Frame", "Left: challenges, Right: solutions")
    p["add_rect"](slide, Inches(0.6), Inches(2.0), Inches(5.95), Inches(4.4), palette["ROW_A"], line_color=palette["ACCENT"])
    p["add_rect"](slide, Inches(6.78), Inches(2.0), Inches(5.95), Inches(4.4), palette["ROW_B"], line_color=palette["ACCENT2"])
    p["add_text"](slide, "Challenges", Inches(0.95), Inches(1.58), Inches(5.1), Inches(0.35), size=13, bold=True, color=palette["ACCENT"])
    p["bullet_block"](slide, ["Decks look inconsistent across teams", "Manual styling slows iteration cycles", "Code snippets are hard to format clearly", "Layout bugs are hard to detect visually"], Inches(0.95), Inches(2.35), Inches(5.1), Inches(2.7), size=13, color=palette["LIGHT_GREY"])
    p["add_text"](slide, "Solutions", Inches(7.1), Inches(1.58), Inches(5.1), Inches(0.35), size=13, bold=True, color=palette["ACCENT2"])
    p["bullet_block"](slide, ["Use primitives as composable building blocks", "Apply a palette once, reuse everywhere", "add_code() auto-fits font size to box height", "detect_overlaps() flags layout collisions early"], Inches(7.1), Inches(2.35), Inches(5.1), Inches(2.7), size=13, color=palette["LIGHT_GREY"])
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 7")

    # ── Slide 8: Known Limitations (left-border card pattern) ──────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Known Limitations", "Design decisions and their trade-offs")
    limitations = [
        ("Fixed slide dimensions",  "All primitives assume 13.33 × 7.5 in widescreen. Changing dimensions requires recalibrating all spacing constants.",                         palette["ACCENT3"]),
        ("No auto-layout engine",   "Element positions are hand-coded in EMU/Inches. Overlaps must be detected and fixed manually or via detect_overlaps().",                    palette["ACCENT4"]),
        ("Single-run text boxes",   "add_text() renders one styled run per box. Mixed formatting in one line requires separate non-overlapping boxes.",                          palette["ACCENT"]),
        ("Code truncation visible", "add_code() appends '...' when lines overflow the box height. Prefer sizing boxes generously or setting a lower min_size.",                 palette["ACCENT2"]),
        ("Palette coupling",        "Primitive colors are closed over at make_primitives() time. Switching palette mid-deck requires instantiating a second primitives dict.",   palette["SUBTITLE_C"]),
    ]
    y = Inches(1.15)
    for title, desc, color in limitations:
        p["add_rect"](slide, Inches(0.35), y, Inches(12.6), Inches(1.0), palette["CARD_BG"])
        p["add_rect"](slide, Inches(0.35), y, Inches(0.1), Inches(1.0), color)
        p["add_text"](slide, title, Inches(0.55), y + Inches(0.07), Inches(12.2), Inches(0.28), size=12, bold=True, color=color)
        p["add_text"](slide, desc,  Inches(0.55), y + Inches(0.38), Inches(12.2), Inches(0.55), size=11, color=palette["LIGHT_GREY"])
        y += Inches(1.08)
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 8")

    # ── Slide 9: Summary ───────────────────────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Summary", "")
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
    y = Inches(1.2)
    rh = Inches(0.6)
    for i, (label, desc, color) in enumerate(summary_items):
        bg = palette["ROW_A"] if i % 2 == 0 else palette["ROW_B"]
        p["add_rect"](slide, Inches(0.35), y, Inches(12.6), rh, bg)
        p["add_rect"](slide, Inches(0.35), y, Inches(0.1), rh, color)
        p["add_text"](slide, label, Inches(0.55), y + Inches(0.1), Inches(2.2), rh - Inches(0.1), size=12, bold=True, color=color)
        p["add_text"](slide, desc,  Inches(2.85), y + Inches(0.1), Inches(9.9), rh - Inches(0.1), size=12, color=palette["LIGHT_GREY"])
        y += rh + Inches(0.01)
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 9")

    output = "example_slide_skeleton_extensive.pptx"
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
