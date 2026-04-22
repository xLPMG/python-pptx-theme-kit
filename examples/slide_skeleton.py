"""Extensive multi-slide example using most available primitives."""

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

    # Slide 1: Hero
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["add_rect"](
        slide,
        Inches(0.3),
        Inches(1.2),
        Inches(12.73),
        Inches(5.85),
        palette["CARD_BG"],
        line_color=palette["ACCENT"],
    )
    p["title_bar"](
        slide,
        "Write your amazign title here",
        "A stylish multi-slide demo deck powered by reusable primitives",
    )
    p["add_text"](
        slide,
        "This slide talks about an interesting topic",
        Inches(0.8),
        Inches(1.6),
        Inches(7.8),
        Inches(0.8),
        size=24,
        bold=True,
        color=palette["WHITE"],
    )
    p["add_text"](
        slide,
        "Built with layered panels, accents, and reusable structures.",
        Inches(0.8),
        Inches(2.4),
        Inches(7.8),
        Inches(0.6),
        size=14,
        italic=True,
        color=palette["SUBTITLE_C"],
    )
    p["add_code"](
        slide,
        "def hello_world():\n    print('Hello world from slide code!')",
        Inches(8.6),
        Inches(1.55),
        Inches(3.9),
        Inches(2.1),
        size=12,
    )
    p["footer"](slide, "python-pptx-theme-kit · extensive sample deck · slide 1")

    # Slide 2: Content overview
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Agenda", "Fast walkthrough of a cool visual narrative")
    p["section_label"](slide, "What We Cover", Inches(1.25))
    p["bullet_block"](
        slide,
        [
            "Why reusable primitives speed up slide production",
            "How to combine geometry and text for visual rhythm",
            "Mixing code snippets with narrative blocks",
            "Practical structure for data and status updates",
        ],
        Inches(0.6),
        Inches(1.6),
        Inches(6.0),
        Inches(2.5),
        size=14,
    )
    p["add_rect"](
        slide,
        Inches(6.95),
        Inches(1.6),
        Inches(5.8),
        Inches(4.5),
        palette["CARD_BG"],
        line_color=palette["ACCENT4"],
    )
    p["add_text"](
        slide,
        "Design note",
        Inches(7.25),
        Inches(1.9),
        Inches(3.2),
        Inches(0.5),
        size=16,
        bold=True,
        color=palette["ACCENT4"],
    )
    p["add_text"](
        slide,
        "Alternating blocks and soft contrast keep the layout lively without feeling noisy.",
        Inches(7.25),
        Inches(2.45),
        Inches(5.1),
        Inches(1.8),
        size=13,
        color=palette["LIGHT_GREY"],
    )
    p["footer"](slide, "python-pptx-theme-kit · extensive sample deck · slide 2")

    # Slide 3: Code + metrics
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Code And KPIs", "Narrative on the left, operational summary on the right")
    p["section_label"](slide, "Code Example", Inches(1.25))
    p["add_code"](
        slide,
        "def hello_world():\n"
        "    message = 'This slide talks about an interesting topic'\n"
        "    print(message)\n"
        "\n"
        "if __name__ == '__main__':\n"
        "    hello_world()",
        Inches(0.6),
        Inches(1.65),
        Inches(12.2),
        Inches(2.25),
        size=12,
    )
    p["section_label"](slide, "Status Snapshot", Inches(4.1))
    p["info_row"](slide, "Theme", "catppuccin_mocha", Inches(4.45), lw=Inches(2.4))
    p["info_row"](slide, "Slides Built", "5", Inches(4.97), lw=Inches(2.4))
    p["info_row"](slide, "Primitives Used", "10 / 10", Inches(5.49), lw=Inches(2.4))
    p["info_row"](slide, "Export Mode", "PowerPoint (.pptx)", Inches(6.01), lw=Inches(2.4))
    p["add_text"](
        slide,
        "Execution-ready structure, presentation-ready style.",
        Inches(0.6),
        Inches(6.55),
        Inches(12.2),
        Inches(0.35),
        size=13,
        italic=True,
        color=palette["SUBTITLE_C"],
        align=PP_ALIGN.CENTER,
    )
    p["footer"](slide, "python-pptx-theme-kit · extensive sample deck · slide 3")

    # Slide 4: Two-column narrative
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Story Frame", "Balance narrative, structure, and visual anchors")
    p["add_rect"](
        slide,
        Inches(0.6),
        Inches(2.0),
        Inches(5.95),
        Inches(4.4),
        palette["ROW_A"],
        line_color=palette["ACCENT"],
    )
    p["add_rect"](
        slide,
        Inches(6.78),
        Inches(2.0),
        Inches(5.95),
        Inches(4.4),
        palette["ROW_B"],
        line_color=palette["ACCENT2"],
    )
    p["section_label"](slide, "Left: Problem", Inches(1.55))
    p["bullet_block"](
        slide,
        [
            "Decks often look inconsistent across teams",
            "Manual styling slows iteration",
            "Code snippets are hard to format clearly",
        ],
        Inches(0.95),
        Inches(2.35),
        Inches(5.1),
        Inches(2.7),
        size=13,
        color=palette["LIGHT_GREY"],
    )
    p["section_label"](slide, "Right: Approach", Inches(1.55))
    p["bullet_block"](
        slide,
        [
            "Use primitives as composable building blocks",
            "Apply a palette once, reuse everywhere",
            "Keep scripts short while scaling design quality",
        ],
        Inches(7.1),
        Inches(2.35),
        Inches(5.1),
        Inches(2.7),
        size=13,
        color=palette["LIGHT_GREY"],
    )
    p["footer"](slide, "python-pptx-theme-kit · extensive sample deck · slide 4")

    # Slide 5: Closing summary
    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["title_bar"](slide, "Closing", "Reusable slides with strong defaults and creative headroom")
    p["section_label"](slide, "Final Checklist", Inches(1.35))
    p["info_row"](slide, "Reusable Theme", "Enabled", Inches(1.7), lw=Inches(3.2))
    p["info_row"](slide, "Narrative Blocks", "Enabled", Inches(2.22), lw=Inches(3.2))
    p["info_row"](slide, "Code Rendering", "Enabled", Inches(2.74), lw=Inches(3.2))
    p["info_row"](slide, "Data Rows", "Enabled", Inches(3.26), lw=Inches(3.2))
    p["add_text"](
        slide,
        "Write your amazign title here",
        Inches(0.7),
        Inches(4.35),
        Inches(12.0),
        Inches(0.9),
        size=30,
        bold=True,
        color=palette["ACCENT"],
        align=PP_ALIGN.CENTER,
    )
    p["add_text"](
        slide,
        "This slide talks about an interesting topic",
        Inches(1.6),
        Inches(5.45),
        Inches(10.2),
        Inches(0.55),
        size=16,
        italic=True,
        color=palette["SUBTITLE_C"],
        align=PP_ALIGN.CENTER,
    )
    p["footer"](slide, "python-pptx-theme-kit · extensive sample deck · slide 5")

    output = "example_slide_skeleton_extensive.pptx"
    prs.save(output)
    print(f"Saved: {output}")

    findings = detect_overlaps(prs, min_overlap_ratio=0.02)
    if findings:
        print("Potential overlapping elements:")
        for line in format_overlaps(findings):
            print(f"- {line}")
    else:
        print("No significant overlaps detected.")


if __name__ == "__main__":
    main()
