"""Reusable PowerPoint theming helpers built on python-pptx."""

from .palettes import get_palette, list_palettes
from .blocks import make_blocks
from .overlap import detect_overlaps, format_overlaps
from .primitives import REQUIRED_PALETTE_KEYS, make_primitives
from .pptx_imports import Presentation, Inches, Pt, RGBColor, PP_ALIGN

__all__ = [
    "get_palette",
    "list_palettes",
    "make_blocks",
    "make_primitives",
    "REQUIRED_PALETTE_KEYS",
    "detect_overlaps",
    "format_overlaps",
    "Presentation",
    "Inches",
    "Pt",
    "RGBColor",
    "PP_ALIGN",
]
