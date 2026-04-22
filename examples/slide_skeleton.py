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
    p["set_bg"](slide, palette["DARK_BG"])
    b["hero_banner_block"](
        slide,
        "Write Your Amazing Title Here",
        "A subtitle that describes the topic in a compelling way",
        "Organisation  ·  Department  ·  Year",
        "Objective: demonstrate reusable slide design patterns with python-pptx-theme-kit.",
    )

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
    b["toc_list_block"](slide, sections)
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
    b["data_source_cards_block"](slide, sources)
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 3")

    # ── Slide 4: Attribute Coverage Comparison ─────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Attribute Coverage Comparison", "Which attributes are provided by which sources?")
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
    b["pipeline_stages_block"](slide, stages)
    b["pipeline_strategy_block"](
        slide,
        "Pairwise Integration Strategy",
        "Sources are not merged all at once. A two-step pairwise approach is used:\n  Step A:  Source A  ⊕  Source B  →  Intermediate result\n  Step B:  Intermediate  ⊕  Source C  →  Final integrated dataset",
        "# main.py – orchestration\ndf_intermediate = merge(source_a, source_b)\nfinal_df        = merge(df_intermediate, source_c)\nfinal_df.sort_values('title').to_csv('output.csv', index=False)",
    )
    p["footer"](slide, "GAV integration: target schema is defined first; each source is mapped into it independently")

    # ── Slide 6: Code + Metrics ─────────────────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Code Example & Status Snapshot", "Full function alongside operational metrics")
    b["code_status_block"](
        slide,
        "def hello_world():\n    \"\"\"Print a greeting and return it.\"\"\"\n    message = 'This slide talks about an interesting topic'\n    print(message)\n    return message\n\nif __name__ == '__main__':\n    result = hello_world()\n    print(f'Done: {result}')",
        [
            ("Theme", "catppuccin_mocha"),
            ("Slides Built", "9"),
            ("Primitives Used", "10 / 10"),
            ("Export Mode", "PowerPoint (.pptx)"),
        ],
    )
    p["footer"](slide, "python-pptx-theme-kit · design patterns demo · slide 6")

    # ── Slide 7: Two-Column Analysis Frame ─────────────────────────────────
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Analysis Frame", "Left: challenges, Right: solutions")
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
    b["left_border_card_list_block"](slide, limitations)
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
