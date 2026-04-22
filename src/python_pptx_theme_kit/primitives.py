"""Primitive drawing helpers for python-pptx slides."""

from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN


def make_primitives(palette):
    dark_bg = palette["DARK_BG"]
    code_bg = palette["CODE_BG"]
    accent = palette["ACCENT"]
    code_fg = palette["ACCENT2"]
    accent3 = palette["ACCENT3"]
    white = palette["WHITE"]
    light_grey = palette["LIGHT_GREY"]
    subtitle_c = palette["SUBTITLE_C"]
    row_a = palette["ROW_A"]
    row_b = palette["ROW_B"]

    slide_w = Inches(13.33)

    def set_bg(slide, color):
        fill = slide.background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_rect(slide, left, top, width, height, fill_color,
                 line_color=None, line_width=None):
        shape = slide.shapes.add_shape(1, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
        if line_color:
            shape.line.color.rgb = line_color
            if line_width:
                shape.line.width = line_width
        else:
            shape.line.fill.background()
        return shape

    def add_text(slide, text, left, top, width, height,
                 size=14, bold=False, italic=False,
                 color=white, align=PP_ALIGN.LEFT, wrap=True):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = wrap
        p = tf.paragraphs[0]
        p.alignment = align
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        return tb

    def add_code(slide, code, left, top, width, height, size=10):
        add_rect(slide, left, top, width, height, code_bg, accent, Pt(1))
        tb = slide.shapes.add_textbox(
            left + Inches(0.15), top + Inches(0.1),
            width - Inches(0.3), height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = False
        first = True
        for line in code.split("\n"):
            if first:
                p = tf.paragraphs[0]
                first = False
            else:
                p = tf.add_paragraph()
            p.alignment = PP_ALIGN.LEFT
            r = p.add_run()
            r.text = line
            r.font.size = Pt(size)
            r.font.name = "Courier New"
            r.font.color.rgb = code_fg

    def blank_slide(prs):
        return prs.slides.add_slide(prs.slide_layouts[6])

    def title_bar(slide, title, subtitle="", bar_height=Inches(1.05)):
        add_rect(slide, 0, 0, slide_w, bar_height, accent)
        add_text(slide, title, Inches(0.35), Inches(0.1),
                 Inches(12.6), Inches(0.58), size=26, bold=True,
                 color=dark_bg)
        if subtitle:
            add_text(slide, subtitle, Inches(0.35), Inches(0.68),
                     Inches(12.6), Inches(0.32), size=13,
                     italic=True, color=dark_bg)

    def section_label(slide, text, y):
        add_text(slide, text, Inches(0.35), y, Inches(12.6), Inches(0.3),
                 size=13, bold=True, color=accent)

    def bullet_block(slide, items, left, top, width, height,
                     size=13, color=light_grey, bullet="•"):
        tb = slide.shapes.add_textbox(left, top, width, height)
        tf = tb.text_frame
        tf.word_wrap = True
        first = True
        for item in items:
            if first:
                p = tf.paragraphs[0]
                first = False
            else:
                p = tf.add_paragraph()
            r = p.add_run()
            r.text = f"{bullet}  {item}"
            r.font.size = Pt(size)
            r.font.color.rgb = color

    def info_row(slide, label, value, y, row_h=Inches(0.52),
                 lw=Inches(2.8), label_color=accent3,
                 value_color=light_grey):
        bg = row_a if int(y / Inches(0.52)) % 2 == 0 else row_b
        add_rect(slide, Inches(0.35), y, Inches(12.6), row_h, bg)
        add_text(slide, label, Inches(0.5), y + Inches(0.08),
                 lw - Inches(0.2), row_h - Inches(0.1),
                 size=12, bold=True, color=label_color)
        add_text(slide, value, Inches(0.5) + lw, y + Inches(0.08),
                 Inches(12.6) - lw - Inches(0.3), row_h - Inches(0.1),
                 size=12, color=value_color)

    def footer(slide, text):
        add_text(slide, text, Inches(0.35), Inches(7.1),
                 Inches(12.6), Inches(0.3), size=10,
                 italic=True, color=subtitle_c, align=PP_ALIGN.CENTER)

    return {
        "set_bg": set_bg,
        "add_rect": add_rect,
        "add_text": add_text,
        "add_code": add_code,
        "title_bar": title_bar,
        "section_label": section_label,
        "bullet_block": bullet_block,
        "info_row": info_row,
        "blank_slide": blank_slide,
        "footer": footer,
    }
