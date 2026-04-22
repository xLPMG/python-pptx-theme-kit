"""Theme palettes for reusable slide generation."""

from pptx.dml.color import RGBColor


PALETTES = {
    "catppuccin_mocha": {
        "DARK_BG": RGBColor(0x1E, 0x1E, 0x2E),
        "ACCENT": RGBColor(0x89, 0xB4, 0xFA),
        "ACCENT2": RGBColor(0xA6, 0xE3, 0xA1),
        "ACCENT3": RGBColor(0xF3, 0x8B, 0xA8),
        "ACCENT4": RGBColor(0xFA, 0xB3, 0x87),
        "WHITE": RGBColor(0xFF, 0xFF, 0xFF),
        "LIGHT_GREY": RGBColor(0xCC, 0xC8, 0xC4),
        "CODE_BG": RGBColor(0x18, 0x18, 0x2E),
        "SUBTITLE_C": RGBColor(0xBA, 0xC2, 0xDE),
        "CARD_BG": RGBColor(0x28, 0x28, 0x44),
        "ROW_A": RGBColor(0x2A, 0x2A, 0x44),
        "ROW_B": RGBColor(0x22, 0x22, 0x38),
    },
    "nord_frost": {
        "DARK_BG": RGBColor(0x2E, 0x34, 0x40),
        "ACCENT": RGBColor(0x88, 0xC0, 0xD0),
        "ACCENT2": RGBColor(0xA3, 0xBE, 0x8C),
        "ACCENT3": RGBColor(0xBF, 0x61, 0x6A),
        "ACCENT4": RGBColor(0xEB, 0xCB, 0x8B),
        "WHITE": RGBColor(0xEC, 0xEF, 0xF4),
        "LIGHT_GREY": RGBColor(0xD8, 0xDE, 0xE9),
        "CODE_BG": RGBColor(0x3B, 0x42, 0x52),
        "SUBTITLE_C": RGBColor(0x81, 0xA1, 0xC1),
        "CARD_BG": RGBColor(0x43, 0x4C, 0x5E),
        "ROW_A": RGBColor(0x4C, 0x56, 0x6A),
        "ROW_B": RGBColor(0x43, 0x4C, 0x5E),
    },
    "paper_sunrise": {
        "DARK_BG": RGBColor(0xF8, 0xF1, 0xE7),
        "ACCENT": RGBColor(0x2E, 0x40, 0x5B),
        "ACCENT2": RGBColor(0x4D, 0x7C, 0x59),
        "ACCENT3": RGBColor(0xA6, 0x3D, 0x40),
        "ACCENT4": RGBColor(0xB5, 0x75, 0x2C),
        "WHITE": RGBColor(0x24, 0x25, 0x2A),
        "LIGHT_GREY": RGBColor(0x44, 0x47, 0x50),
        "CODE_BG": RGBColor(0xE7, 0xDB, 0xCA),
        "SUBTITLE_C": RGBColor(0x5A, 0x65, 0x78),
        "CARD_BG": RGBColor(0xF1, 0xE7, 0xD9),
        "ROW_A": RGBColor(0xEC, 0xE0, 0xD0),
        "ROW_B": RGBColor(0xE4, 0xD6, 0xC3),
    },
}


def list_palettes():
    """Return sorted list of available palette names."""
    return sorted(PALETTES)


def get_palette(name="catppuccin_mocha"):
    """Return palette dict for given name."""
    if name not in PALETTES:
        options = ", ".join(list_palettes())
        raise ValueError(f"Unknown palette '{name}'. Available: {options}")
    return PALETTES[name]
