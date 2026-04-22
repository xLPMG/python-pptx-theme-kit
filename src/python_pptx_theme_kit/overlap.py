"""Geometry helpers for detecting overlapping slide elements."""


def _bounds(shape):
    """Return rectangular bounds for a shape.

    Args:
        shape: A python-pptx shape object.

    Returns:
        Tuple[int, int, int, int]: Bounds as ``(left, top, right, bottom)``.
    """
    left = int(shape.left)
    top = int(shape.top)
    width = int(shape.width)
    height = int(shape.height)
    return left, top, left + width, top + height


def _intersection(a, b):
    """Return the intersection rectangle of two bounds, if any.

    Args:
        a: Bounds tuple ``(left, top, right, bottom)``.
        b: Bounds tuple ``(left, top, right, bottom)``.

    Returns:
        Optional[Tuple[int, int, int, int]]: Intersected bounds, or ``None`` if
        rectangles do not overlap.
    """
    left = max(a[0], b[0])
    top = max(a[1], b[1])
    right = min(a[2], b[2])
    bottom = min(a[3], b[3])
    if right <= left or bottom <= top:
        return None
    return left, top, right, bottom


def _area(bounds):
    """Compute area of a bounds tuple.

    Args:
        bounds: Bounds tuple ``(left, top, right, bottom)``.

    Returns:
        int: Non-negative area.
    """
    return max(0, bounds[2] - bounds[0]) * max(0, bounds[3] - bounds[1])


def _contains(outer, inner):
    """Check whether one bounds rectangle fully contains another.

    Args:
        outer: Candidate container bounds tuple.
        inner: Candidate contained bounds tuple.

    Returns:
        bool: True when ``outer`` fully contains ``inner``.
    """
    return (
        outer[0] <= inner[0]
        and outer[1] <= inner[1]
        and outer[2] >= inner[2]
        and outer[3] >= inner[3]
    )


def detect_slide_overlaps(
    slide,
    slide_number,
    min_overlap_ratio=0.01,
    ignore_full_containment=True,
    containment_ratio=0.98,
):
    """Return overlap entries for one slide.

    Each entry contains shape names, overlap area, and overlap ratios.
    Ratios are computed against each shape area to make it easy to tune noise.

    Args:
        slide: Slide whose shapes should be analyzed.
        slide_number: 1-based slide number used in output entries.
        min_overlap_ratio: Minimum overlap ratio required to report a finding.
        ignore_full_containment: Whether to suppress near-fully-contained pairs.
        containment_ratio: Ratio threshold used with containment suppression.

    Returns:
        List[dict]: Overlap findings for the slide.
    """
    entries = []
    shapes = list(slide.shapes)

    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            a = shapes[i]
            b = shapes[j]

            a_bounds = _bounds(a)
            b_bounds = _bounds(b)
            inter = _intersection(a_bounds, b_bounds)
            if inter is None:
                continue

            inter_area = _area(inter)
            a_area = _area(a_bounds)
            b_area = _area(b_bounds)
            if a_area == 0 or b_area == 0:
                continue

            ratio_a = inter_area / a_area
            ratio_b = inter_area / b_area
            max_ratio = max(ratio_a, ratio_b)
            if max_ratio < min_overlap_ratio:
                continue

            if ignore_full_containment:
                contained = (
                    _contains(a_bounds, b_bounds) and ratio_b >= containment_ratio
                ) or (
                    _contains(b_bounds, a_bounds) and ratio_a >= containment_ratio
                )
                if contained:
                    continue

            entries.append(
                {
                    "slide": slide_number,
                    "shape_a": getattr(a, "name", f"shape_{i + 1}"),
                    "shape_b": getattr(b, "name", f"shape_{j + 1}"),
                    "overlap_area": inter_area,
                    "overlap_ratio_a": ratio_a,
                    "overlap_ratio_b": ratio_b,
                }
            )

    return entries


def detect_overlaps(
    presentation,
    min_overlap_ratio=0.01,
    ignore_full_containment=True,
    containment_ratio=0.98,
):
    """Return overlap entries across all slides in a presentation.

    Args:
        presentation: python-pptx ``Presentation`` object.
        min_overlap_ratio: Minimum overlap ratio required to report a finding.
        ignore_full_containment: Whether to suppress near-fully-contained pairs.
        containment_ratio: Ratio threshold used with containment suppression.

    Returns:
        List[dict]: Aggregated overlap findings across all slides.
    """
    findings = []
    for idx, slide in enumerate(presentation.slides, start=1):
        findings.extend(
            detect_slide_overlaps(
                slide,
                idx,
                min_overlap_ratio=min_overlap_ratio,
                ignore_full_containment=ignore_full_containment,
                containment_ratio=containment_ratio,
            )
        )
    return findings


def format_overlaps(findings):
    """Format overlap findings into human-readable lines.

    Args:
        findings: Iterable of overlap dict entries from ``detect_overlaps``.

    Returns:
        List[str]: Human-readable overlap summary lines.
    """
    lines = []
    for f in findings:
        lines.append(
            "Slide {slide}: {a} overlaps {b} (A: {ra:.1%}, B: {rb:.1%})".format(
                slide=f["slide"],
                a=f["shape_a"],
                b=f["shape_b"],
                ra=f["overlap_ratio_a"],
                rb=f["overlap_ratio_b"],
            )
        )
    return lines
