# python-pptx-theme-kit

Reusable Python helpers for building styled PowerPoint decks with `python-pptx`.

## Quick start

```bash
cd python-pptx-theme-kit
python -m venv .venv
source .venv/bin/activate
pip install -e .
python examples/minimal_deck.py
```

Generated output:

- `example_theme_kit_deck.pptx`

## Available palettes

- `catppuccin_mocha`
- `nord_frost`
- `paper_sunrise`

## How to use in your own script

```python
from python_pptx_theme_kit import Presentation, Inches, get_palette, make_primitives

palette = get_palette("catppuccin_mocha")
pr = make_primitives(palette)

prs = Presentation()
slide = pr["blank_slide"](prs)
pr["set_bg"](slide, palette["DARK_BG"])
```
