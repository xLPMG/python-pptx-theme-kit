# python-pptx-theme-kit

Reusable Python helpers for building styled PowerPoint decks with `python-pptx`.

## Quick start

```bash
cd python-pptx-theme-kit
python -m venv .venv
source .venv/bin/activate
pip install -e .
python examples/slide_showcase.py
```

Generated output:

- `example_slide_showcase.pptx`

## Available palettes

- `catppuccin_mocha`
- `nord_frost`
- `paper_sunrise`

## How to use in your own script

```python
from python_pptx_theme_kit import Presentation, Inches, get_palette, make_primitives, make_blocks

palette = get_palette("catppuccin_mocha")
pr = make_primitives(palette)
bl = make_blocks(palette)

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

slide = pr["blank_slide"](prs)
bl["slide_chrome_block"](
	slide,
	title="Table of Contents",
	subtitle="Overview of deck sections",
	footer_text="example footer",
)
bl["toc_list_block"](
	slide,
	[
		("1", "Intro", "Slide 1"),
		("2", "Details", "Slide 2"),
		("3", "Summary", "Slide 3"),
	],
)

prs.save("my_deck.pptx")
```

## Blocks-first workflow

The toolkit supports a two-layer API:

- blocks: reusable prepared slide constellations (recommended first choice)
- primitives: low-level building blocks for fine-grained custom layout

Use blocks when your slide matches an existing pattern, then add small primitive overrides only when needed.

Available blocks from make_blocks(palette):

- slide_chrome_block: apply background + optional title bar + optional footer
- hero_banner_block: centered hero title/subtitle and meta lines
- toc_list_block: numbered table-of-contents rows
- data_source_cards_block: multi-card source overview with attribute rows
- coverage_table_block: striped comparison matrix with optional insight row
- pipeline_stages_block: horizontal process cards with connectors
- pipeline_strategy_block: architecture strategy panel + code area
- code_status_block: implementation code panel + status key/value rows
- two_column_panel_block: left/right framed analysis with bullet lists
- left_border_card_list_block: striped left-border cards for risks/summary lists

## Primitive layer

All original primitives remain available via make_primitives(palette), and are useful for:

- one-off decorative elements
- small spacing adjustments around a block
- bespoke slide patterns not yet covered by make_blocks
