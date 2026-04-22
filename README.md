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

- `catppuccin_latte`
- `catppuccin_frappe`
- `catppuccin_macchiato`
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
- image_caption_card_block: framed image card with title and caption
- two_column_panel_block: left/right framed analysis with bullet lists
- left_border_card_list_block: striped left-border cards for risks/summary lists

## Primitive layer

All original primitives remain available via make_primitives(palette), and are useful for:

- one-off decorative elements
- small spacing adjustments around a block
- bespoke slide patterns not yet covered by make_blocks

Image support is available at the primitive layer via `add_image` with fit modes:

- `native`: keep native image size (or honor width/height if provided)
- `contain`: preserve full image inside frame without crop
- `cover`: fill frame and crop overflow while preserving aspect ratio
- `stretch`: force image into frame dimensions (may distort)

## LLM support

The library is designed to be compatible with LLM-driven code generation. 
The primitives and blocks are structured to be easily discoverable and composable, making it straightforward to generate new slide layouts or modify existing ones using natural language prompts.

The example script `discovery_of_exoplanets.py` was created by GPT-5.3-Codex using the following prompt:

```text
Read create-ppt.txt and familiarize yourself with your task. 
The topic of the presentation is "Discovery of Exoplanets".
It should explain what exoplanets are, challenges of discovery
and the two methods we use to discover exoplanets.
It should also mention recently discovered exoplanets and
their properties. You should use images if appropriate. 
In that case, ask the user to search for specific images online 
based on your description and provide the file name under which 
the user should save the image for you.
```
