"""Higher-level layout blocks composed from primitives."""

import warnings

from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

from .primitives import _Namespace, make_primitives


SLIDE_WIDTH = Inches(13.33)
SLIDE_CONTENT_LEFT = Inches(0.35)
SLIDE_CONTENT_WIDTH = Inches(12.6)


def make_blocks(palette, min_text_size=10, min_code_size=9):
    """Build and return reusable composition blocks.

    Args:
        palette: Dictionary returned by ``get_palette``.
        min_text_size: Minimum font size floor applied by primitive text helpers.
        min_code_size: Minimum font size floor applied by primitive code helpers.

    Returns:
        Dict[str, Callable]: Prepared layout block helpers.
    """
    p = make_primitives(
        palette,
        min_text_size=min_text_size,
        min_code_size=min_code_size,
    )

    def toc_list_block(
        slide,
        items,
        left=SLIDE_CONTENT_LEFT,
        top=Inches(1.15),
        width=SLIDE_CONTENT_WIDTH,
        row_height=Inches(0.52),
        row_gap=Inches(0.05),
        number_width=Inches(0.52),
        page_width=Inches(1.9),
        section_size=13,
        page_size=12,
    ):
        """Render a numbered table-of-contents style list.

        Args:
            slide: Target slide object.
            items: Sequence of ``(number, section, page)`` tuples.
            left: Left position for the block.
            top: Top position for the first row.
            width: Total row width.
            row_height: Height of each row.
            row_gap: Gap between rows.
            number_width: Width of the numbered badge column.
            page_width: Width of the right page-reference column.
            section_size: Font size for section labels.
            page_size: Font size for page references.

        Returns:
            The ``top`` coordinate for the next row after the block.
        """
        y = top
        for index, (number, section, page) in enumerate(items):
            bg = palette["CARD_BG"] if index % 2 == 1 else palette["ROW_B"]
            p["add_rect"](slide, left, y, width, row_height, bg)
            p["add_rect"](slide, left, y, number_width, row_height, palette["ACCENT"])
            p["add_text"](
                slide,
                str(number),
                left,
                y,
                number_width,
                row_height,
                size=section_size,
                bold=True,
                color=palette["DARK_BG"],
                align=PP_ALIGN.CENTER,
            )
            p["add_text"](
                slide,
                section,
                left + number_width + Inches(0.1),
                y + Inches(0.1),
                width - number_width - page_width - Inches(0.2),
                row_height - Inches(0.1),
                size=section_size,
                color=palette["WHITE"],
            )
            p["add_text"](
                slide,
                page,
                left + width - page_width,
                y + Inches(0.1),
                page_width - Inches(0.1),
                row_height - Inches(0.1),
                size=page_size,
                italic=True,
                color=palette["SUBTITLE_C"],
                align=PP_ALIGN.RIGHT,
            )
            y += row_height + row_gap
        return y

    def data_source_cards_block(
        slide,
        sources,
        left=SLIDE_CONTENT_LEFT,
        top=Inches(1.15),
        width=SLIDE_CONTENT_WIDTH,
        height=Inches(3.85),
        columns=3,
        gap=Inches(0.2),
        row_height=Inches(0.33),
    ):
        """Render a multi-card data source overview.

        Args:
            slide: Target slide object.
            sources: Sequence of source tuples ``(name, source_id, meta, attrs)``.
                ``attrs`` should be ``(attr_name, mapping, is_null)`` tuples.
            left: Left position for the block.
            top: Top position for the cards.
            width: Total block width.
            height: Card height.
            columns: Number of cards per row.
            gap: Horizontal gap between cards.
            row_height: Height of each attribute row.

        Returns:
            The bottom ``y`` coordinate of the card block.
        """
        if columns < 1:
            columns = 1
        if len(sources) > columns:
            warnings.warn(
                f"data_source_cards_block received {len(sources)} sources but "
                f"columns={columns}; only the first {columns} will be rendered.",
                stacklevel=2,
            )

        card_width = (width - gap * (columns - 1)) / columns
        for card_index, (name, source_id, meta, attrs) in enumerate(sources[:columns]):
            x = left + card_index * (card_width + gap)
            p["add_rect"](slide, x, top, card_width, height, palette["CARD_BG"])
            p["add_text"](
                slide,
                name,
                x + Inches(0.1),
                top + Inches(0.05),
                card_width - Inches(0.2),
                Inches(0.3),
                size=13,
                bold=True,
                color=palette["ACCENT"],
            )
            p["add_text"](
                slide,
                source_id,
                x + Inches(0.1),
                top + Inches(0.37),
                card_width - Inches(0.2),
                Inches(0.25),
                size=8,
                color=palette["SUBTITLE_C"],
            )
            p["add_text"](
                slide,
                meta,
                x + Inches(0.1),
                top + Inches(0.63),
                card_width - Inches(0.2),
                Inches(0.22),
                size=10,
                bold=True,
                color=palette["ACCENT3"],
            )
            p["add_rect"](
                slide,
                x + Inches(0.06),
                top + Inches(0.9),
                card_width - Inches(0.12),
                Inches(0.02),
                palette["ACCENT"],
            )
            y = top + Inches(0.96)
            attr_width = card_width * 0.44
            map_width = card_width * 0.53
            for row_index, (attr, mapping, is_null) in enumerate(attrs):
                bg = palette["ROW_A"] if row_index % 2 == 0 else palette["ROW_B"]
                p["add_rect"](
                    slide,
                    x + Inches(0.06),
                    y,
                    card_width - Inches(0.12),
                    row_height,
                    bg,
                )
                p["add_text"](
                    slide,
                    attr,
                    x + Inches(0.1),
                    y + Inches(0.04),
                    attr_width - Inches(0.05),
                    row_height - Inches(0.04),
                    size=10,
                    bold=True,
                    color=palette["LIGHT_GREY"] if is_null else palette["WHITE"],
                )
                p["add_text"](
                    slide,
                    mapping,
                    x + attr_width + Inches(0.08),
                    y + Inches(0.04),
                    map_width - Inches(0.1),
                    row_height - Inches(0.04),
                    size=10,
                    color=palette["ACCENT3"] if is_null else palette["ACCENT2"],
                )
                y += row_height
        return top + height

    def coverage_table_block(
        slide,
        column_headers,
        rows,
        left=SLIDE_CONTENT_LEFT,
        top=Inches(1.15),
        width=SLIDE_CONTENT_WIDTH,
        header_height=Inches(0.4),
        row_height=Inches(0.43),
        first_col_width=Inches(4.0),
        insight_text=None,
        status_positive="Y",
        status_negative="-",
    ):
        """Render an attribute coverage matrix with optional insight bar.

        Args:
            slide: Target slide object.
            column_headers: Sequence of table header labels.
            rows: Sequence of tuples ``(label, statuses)`` where ``statuses`` is a
                sequence of values for each source column.
            left: Left position for the block.
            top: Top position for the table header.
            width: Total width of the table.
            header_height: Height of the table header.
            row_height: Height of each body row.
            first_col_width: Width of the first column.
            insight_text: Optional summary text rendered below the body.
            status_positive: Value treated as positive coverage.
            status_negative: Value treated as negative coverage.

        Returns:
            The bottom ``y`` coordinate of the block.
        """
        source_cols = max(1, len(column_headers) - 1)
        remaining_width = width - first_col_width
        source_col_width = remaining_width / source_cols

        x_positions = [left, left + first_col_width]
        for col_index in range(1, source_cols):
            x_positions.append(left + first_col_width + source_col_width * col_index)

        p["add_rect"](slide, left, top, width, header_height, palette["ACCENT"])
        p["add_text"](
            slide,
            column_headers[0],
            left + Inches(0.05),
            top + Inches(0.03),
            first_col_width - Inches(0.1),
            header_height - Inches(0.05),
            size=12,
            bold=True,
            color=palette["DARK_BG"],
        )

        for src_index in range(source_cols):
            header_text = column_headers[src_index + 1]
            x = x_positions[src_index + 1]
            p["add_text"](
                slide,
                header_text,
                x + Inches(0.05),
                top + Inches(0.03),
                source_col_width - Inches(0.1),
                header_height - Inches(0.05),
                size=12,
                bold=True,
                color=palette["DARK_BG"],
            )

        y = top + header_height
        for row_index, (label, statuses) in enumerate(rows):
            if len(statuses) < source_cols:
                warnings.warn(
                    f"coverage_table_block row '{label}' has {len(statuses)} status "
                    f"values but {source_cols} columns expected; missing cells will be blank.",
                    stacklevel=2,
                )
            bg = palette["ROW_A"] if row_index % 2 == 0 else palette["ROW_B"]
            p["add_rect"](slide, left, y, width, row_height, bg)
            p["add_text"](
                slide,
                label,
                left + Inches(0.05),
                y + Inches(0.07),
                first_col_width - Inches(0.1),
                row_height - Inches(0.07),
                size=12,
                bold=True,
                color=palette["WHITE"],
            )
            for status_index, status in enumerate(statuses[:source_cols]):
                status_text = str(status)
                if status_text == str(status_positive):
                    color = palette["ACCENT2"]
                elif status_text == str(status_negative):
                    color = palette["ACCENT3"]
                else:
                    color = palette["LIGHT_GREY"]
                p["add_text"](
                    slide,
                    status_text,
                    x_positions[status_index + 1] + Inches(0.05),
                    y + Inches(0.07),
                    source_col_width - Inches(0.1),
                    row_height - Inches(0.07),
                    size=12,
                    color=color,
                )
            y += row_height

        if insight_text:
            p["add_rect"](slide, left, y + Inches(0.1), width, Inches(0.45), palette["ROW_A"])
            p["add_text"](
                slide,
                insight_text,
                left + Inches(0.2),
                y + Inches(0.15),
                width - Inches(0.3),
                Inches(0.35),
                size=12,
                bold=True,
                color=palette["ACCENT2"],
            )
            y += Inches(0.55)

        return y

    def pipeline_stages_block(
        slide,
        stages,
        left=Inches(0.4),
        top=Inches(2.0),
        width=Inches(12.5),
        box_height=Inches(1.3),
        connector_text=">",
    ):
        """Render a horizontal process pipeline with stage cards.

        Args:
            slide: Target slide object.
            stages: Sequence of ``(stage_name, script_name, description)`` tuples.
            left: Left position for the first stage.
            top: Top position for the stage row.
            width: Total horizontal width allocated to the pipeline.
            box_height: Height of each stage card.
            connector_text: Text glyph used between cards.

        Returns:
            The bottom ``y`` coordinate of the pipeline row.
        """
        stage_count = max(1, len(stages))
        connector_gap = Inches(0.28)
        total_connectors = connector_gap * (stage_count - 1)
        box_width = (width - total_connectors) / stage_count

        x = left
        for index, (stage, script, desc) in enumerate(stages):
            p["add_rect"](
                slide,
                x,
                top,
                box_width,
                box_height,
                palette["CARD_BG"],
                line_color=palette["ACCENT"],
            )
            p["add_text"](
                slide,
                stage,
                x + Inches(0.05),
                top + Inches(0.05),
                box_width - Inches(0.1),
                Inches(0.35),
                size=10,
                bold=True,
                color=palette["ACCENT"],
                align=PP_ALIGN.CENTER,
            )
            p["add_text"](
                slide,
                script,
                x + Inches(0.05),
                top + Inches(0.4),
                box_width - Inches(0.1),
                Inches(0.28),
                size=8,
                color=palette["ACCENT3"],
                align=PP_ALIGN.CENTER,
            )
            p["add_text"](
                slide,
                desc,
                x + Inches(0.05),
                top + Inches(0.68),
                box_width - Inches(0.1),
                box_height - Inches(0.75),
                size=9,
                color=palette["LIGHT_GREY"],
                align=PP_ALIGN.CENTER,
            )
            if index < stage_count - 1:
                p["add_text"](
                    slide,
                    connector_text,
                    x + box_width,
                    top + box_height / 2 - Inches(0.11),
                    connector_gap,
                    Inches(0.22),
                    size=13,
                    bold=True,
                    color=palette["ACCENT"],
                    align=PP_ALIGN.CENTER,
                )
            x += box_width + connector_gap
        return top + box_height

    def left_border_card_list_block(
        slide,
        items,
        left=SLIDE_CONTENT_LEFT,
        top=Inches(1.15),
        width=SLIDE_CONTENT_WIDTH,
        row_height=Inches(1.0),
        row_gap=Inches(0.08),
        stripe_width=Inches(0.1),
        title_width=Inches(2.2),
        title_size=12,
        desc_size=11,
        alternating_bg=False,
    ):
        """Render rows with a colored left border stripe, title, and description.

        Args:
            slide: Target slide object.
            items: Sequence of ``(title, description, color)`` tuples.
            left: Left position for the block.
            top: Top position for the first row.
            width: Total row width.
            row_height: Height of each row.
            row_gap: Vertical gap between rows.
            stripe_width: Width of the left color stripe.
            title_width: Width reserved for the title text.
            title_size: Font size for title text.
            desc_size: Font size for description text.
            alternating_bg: Whether to alternate row backgrounds.

        Returns:
            The ``top`` coordinate for the next row after the block.
        """
        y = top
        for index, (title, desc, color) in enumerate(items):
            if alternating_bg:
                bg = palette["ROW_A"] if index % 2 == 0 else palette["ROW_B"]
            else:
                bg = palette["CARD_BG"]

            p["add_rect"](slide, left, y, width, row_height, bg)
            p["add_rect"](slide, left, y, stripe_width, row_height, color)
            p["add_text"](
                slide,
                title,
                left + stripe_width + Inches(0.1),
                y + Inches(0.08),
                title_width,
                row_height - Inches(0.12),
                size=title_size,
                bold=True,
                color=color,
            )
            p["add_text"](
                slide,
                desc,
                left + stripe_width + title_width + Inches(0.25),
                y + Inches(0.08),
                width - title_width - stripe_width - Inches(0.35),
                row_height - Inches(0.12),
                size=desc_size,
                color=palette["LIGHT_GREY"],
            )
            y += row_height + row_gap
        return y

    def two_column_panel_block(
        slide,
        left_title,
        left_items,
        right_title,
        right_items,
        left=Inches(0.6),
        top=Inches(2.0),
        width=Inches(12.13),
        height=Inches(4.4),
        gap=Inches(0.23),
    ):
        """Render a two-column framed analysis block with bullet content.

        Args:
            slide: Target slide object.
            left_title: Header for left column.
            left_items: Bullet list for left column.
            right_title: Header for right column.
            right_items: Bullet list for right column.
            left: Left position for the block.
            top: Top position for both panels.
            width: Total block width.
            height: Panel height.
            gap: Gap between left and right panels.

        Returns:
            The bottom ``y`` coordinate of the two-column block.
        """
        panel_width = (width - gap) / 2
        right_left = left + panel_width + gap

        p["add_rect"](
            slide,
            left,
            top,
            panel_width,
            height,
            palette["ROW_A"],
            line_color=palette["ACCENT"],
        )
        p["add_rect"](
            slide,
            right_left,
            top,
            panel_width,
            height,
            palette["ROW_B"],
            line_color=palette["ACCENT2"],
        )

        p["add_text"](
            slide,
            left_title,
            left + Inches(0.35),
            top - Inches(0.42),
            panel_width - Inches(0.5),
            Inches(0.35),
            size=13,
            bold=True,
            color=palette["ACCENT"],
        )
        p["add_text"](
            slide,
            right_title,
            right_left + Inches(0.32),
            top - Inches(0.42),
            panel_width - Inches(0.5),
            Inches(0.35),
            size=13,
            bold=True,
            color=palette["ACCENT2"],
        )

        p["bullet_block"](
            slide,
            left_items,
            left + Inches(0.35),
            top + Inches(0.35),
            panel_width - Inches(0.6),
            height - Inches(0.7),
            size=13,
            color=palette["LIGHT_GREY"],
        )
        p["bullet_block"](
            slide,
            right_items,
            right_left + Inches(0.32),
            top + Inches(0.35),
            panel_width - Inches(0.6),
            height - Inches(0.7),
            size=13,
            color=palette["LIGHT_GREY"],
        )

        return top + height

    def hero_banner_block(
        slide,
        title,
        subtitle,
        org_line,
        objective,
        band_top=Inches(2.3),
        band_height=Inches(2.9),
    ):
        """Render a centered hero banner with title, subtitle and meta lines.

        Args:
            slide: Target slide object.
            title: Main hero title text.
            subtitle: Hero subtitle text.
            org_line: Organization/context line text.
            objective: Objective/supporting text.
            band_top: Vertical start of accent band.
            band_height: Height of accent band.

        Returns:
            The bottom ``y`` coordinate of the accent band.
        """
        p["add_rect"](
            slide,
            0,
            band_top,
            SLIDE_WIDTH,
            band_height,
            palette["ACCENT"],
        )
        p["add_text"](
            slide,
            title,
            Inches(0.5),
            band_top + Inches(0.15),
            Inches(12.3),
            Inches(1.0),
            size=46,
            bold=True,
            color=palette["DARK_BG"],
            align=PP_ALIGN.CENTER,
        )
        p["add_text"](
            slide,
            subtitle,
            Inches(0.5),
            band_top + Inches(1.15),
            Inches(12.3),
            Inches(0.6),
            size=22,
            italic=True,
            color=palette["DARK_BG"],
            align=PP_ALIGN.CENTER,
        )
        p["add_text"](
            slide,
            org_line,
            Inches(0.5),
            Inches(5.8),
            Inches(12.3),
            Inches(0.4),
            size=13,
            color=palette["SUBTITLE_C"],
            align=PP_ALIGN.CENTER,
        )
        p["add_text"](
            slide,
            objective,
            Inches(1.0),
            Inches(6.3),
            Inches(11.3),
            Inches(0.5),
            size=12,
            italic=True,
            color=palette["LIGHT_GREY"],
            align=PP_ALIGN.CENTER,
        )
        return band_top + band_height

    def pipeline_strategy_block(
        slide,
        heading,
        strategy_text,
        code_text,
        top=Inches(3.55),
        width=SLIDE_CONTENT_WIDTH,
        left=SLIDE_CONTENT_LEFT,
    ):
        """Render architecture strategy text panel plus orchestration code panel.

        Args:
            slide: Target slide object.
            heading: Section heading text.
            strategy_text: Explanatory multi-line text.
            code_text: Code snippet text.
            top: Top position of the strategy block.
            width: Width of the strategy and code containers.
            left: Left position of the block.

        Returns:
            The bottom ``y`` coordinate of the code panel.
        """
        p["add_rect"](slide, left, top, width, Inches(1.35), palette["ROW_B"])
        p["section_label"](slide, heading, left + Inches(0.2), top + Inches(0.07), width - Inches(0.4))
        p["add_text"](
            slide,
            strategy_text,
            left + Inches(0.2),
            top + Inches(0.43),
            width - Inches(0.4),
            Inches(0.82),
            size=12,
            color=palette["LIGHT_GREY"],
        )
        code_top = top + Inches(1.53)
        p["add_code"](
            slide,
            code_text,
            left,
            code_top,
            width,
            Inches(1.65),
            size=12,
            wrap=True,
        )
        return code_top + Inches(1.65)

    def code_status_block(
        slide,
        code_text,
        status_rows,
        code_heading="Implementation",
        status_heading="Status Snapshot",
        left=Inches(0.6),
    ):
        """Render a code panel followed by compact status rows.

        Args:
            slide: Target slide object.
            code_text: Code snippet to display.
            status_rows: Sequence of ``(label, value)`` tuples.
            code_heading: Heading above code panel.
            status_heading: Heading above status rows.
            left: Left position of the block.

        Returns:
            The bottom ``y`` coordinate after status rows.
        """
        p["section_label"](slide, code_heading, left, Inches(1.25), Inches(6.0))
        p["add_code"](
            slide,
            code_text,
            left,
            Inches(1.65),
            Inches(12.2),
            Inches(2.5),
            size=12,
            wrap=True,
        )
        p["section_label"](slide, status_heading, left, Inches(4.35), Inches(6.0))
        y = Inches(4.7)
        for row_index, (label, value) in enumerate(status_rows):
            p["info_row"](slide, label, value, y, lw=Inches(2.4), row_index=row_index)
            y += Inches(0.52)
        return y

    def image_caption_card_block(
        slide,
        image_path,
        title,
        caption,
        left=SLIDE_CONTENT_LEFT,
        top=Inches(1.15),
        width=SLIDE_CONTENT_WIDTH,
        height=Inches(5.9),
        image_ratio=0.78,
        fit="cover",
    ):
        """Render a card containing a framed image with title and caption.

        Args:
            slide: Target slide object.
            image_path: Path to the image file.
            title: Title text below image.
            caption: Supporting caption text.
            left: Left position of the card.
            top: Top position of the card.
            width: Card width.
            height: Card height.
            image_ratio: Fraction of card height used by image region.
            fit: Image fit mode passed to ``add_image``.

        Returns:
            The bottom ``y`` coordinate of the card.
        """
        pad = Inches(0.12)
        p["add_rect"](slide, left, top, width, height, palette["CARD_BG"], line_color=palette["ACCENT"])

        image_h = (height - pad * 2) * image_ratio
        p["add_image"](
            slide,
            image_path,
            left + pad,
            top + pad,
            width=width - pad * 2,
            height=image_h,
            fit=fit,
            border_color=palette["ACCENT"],
        )

        text_top = top + pad + image_h + Inches(0.12)
        p["add_text"](
            slide,
            title,
            left + Inches(0.18),
            text_top,
            width - Inches(0.36),
            Inches(0.42),
            size=15,
            bold=True,
            color=palette["ACCENT2"],
            align=PP_ALIGN.CENTER,
        )
        p["add_text"](
            slide,
            caption,
            left + Inches(0.18),
            text_top + Inches(0.43),
            width - Inches(0.36),
            height - (text_top - top) - Inches(0.5),
            size=12,
            color=palette["LIGHT_GREY"],
            align=PP_ALIGN.CENTER,
        )
        return top + height

    def slide_chrome_block(
        slide,
        title=None,
        subtitle="",
        footer_text=None,
        show_title_bar=True,
        bg_color=None,
    ):
        """Apply common slide chrome: background, optional title bar, and footer.

        Args:
            slide: Target slide object.
            title: Optional title text for title bar.
            subtitle: Optional subtitle text for title bar.
            footer_text: Optional footer text.
            show_title_bar: Whether to render the title bar.
            bg_color: Optional background color override.

        Returns:
            None.
        """
        p["set_bg"](slide, bg_color or palette["DARK_BG"])
        if show_title_bar and title is not None:
            p["title_bar"](slide, title, subtitle)
        if footer_text:
            p["footer"](slide, footer_text)

    return _Namespace({
        "toc_list_block": toc_list_block,
        "data_source_cards_block": data_source_cards_block,
        "coverage_table_block": coverage_table_block,
        "pipeline_stages_block": pipeline_stages_block,
        "left_border_card_list_block": left_border_card_list_block,
        "two_column_panel_block": two_column_panel_block,
        "hero_banner_block": hero_banner_block,
        "pipeline_strategy_block": pipeline_strategy_block,
        "code_status_block": code_status_block,
        "image_caption_card_block": image_caption_card_block,
        "slide_chrome_block": slide_chrome_block,
    })
