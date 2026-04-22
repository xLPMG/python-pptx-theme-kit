"""Minimal example showing how to use python_pptx_theme_kit."""

from python_pptx_theme_kit import (
    Presentation,
    Inches,
    PP_ALIGN,
    get_palette,
    make_primitives,
)


def main():
    palette = get_palette("catppuccin_mocha")
    p = make_primitives(palette)

    prs = Presentation()
    prs.slide_width = Inches(13.33)
    prs.slide_height = Inches(7.5)

    slide = p["blank_slide"](prs)
    p["set_bg"](slide, palette["DARK_BG"])
    p["add_rect"](slide, 0, 0, Inches(13.33), Inches(1.0), palette["ACCENT"])
    p["add_text"](
        slide,
        "Hello from python-pptx-theme-kit",
        Inches(0.4),
        Inches(0.15),
        Inches(12.5),
        Inches(0.6),
        size=28,
        bold=True,
        color=palette["DARK_BG"],
        align=PP_ALIGN.CENTER,
    )
    p["add_code"](
        slide,
        "palette = get_palette('catppuccin_mocha')\\nprimitives = make_primitives(palette)",
        Inches(0.8),
        Inches(1.6),
        Inches(11.7),
        Inches(2.0),
        size=14,
    )

    out = "example_theme_kit_deck.pptx"
    prs.save(out)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
