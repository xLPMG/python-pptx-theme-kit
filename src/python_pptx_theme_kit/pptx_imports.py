"""Centralized python-pptx imports for reuse across slide projects."""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

__all__ = ["Presentation", "Inches", "Pt", "RGBColor", "PP_ALIGN"]
