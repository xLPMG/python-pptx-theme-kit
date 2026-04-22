from python_pptx_theme_kit import (
    Presentation,
    Inches,
    PP_ALIGN,
    get_palette,
    list_palettes,
    make_blocks,
    make_primitives,
    detect_overlaps,
    format_overlaps,
)


SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)


def main():
    palette_name = "catppuccin_mocha"
    if palette_name not in list_palettes():
        raise ValueError(f"Palette '{palette_name}' is not available.")

    palette = get_palette(palette_name)
    p = make_primitives(palette, min_text_size=11, min_code_size=10)
    b = make_blocks(palette, min_text_size=11, min_code_size=10)

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    # Slide 1: Hero
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](slide, show_title_bar=False)
    b["hero_banner_block"](
        slide,
        "Discovery of Exoplanets",
        "How we detect worlds beyond our Solar System",
        "Astronomy Briefing  |  2026",
        "Objective: explain what exoplanets are, discovery challenges, core detection methods, and recent discoveries.",
    )

    # Slide 2: Table of contents
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Table of Contents",
        subtitle="Roadmap for this presentation",
        footer_text="Discovery of Exoplanets | slide 2",
    )
    b["toc_list_block"](
        slide,
        [
            ("1", "What Are Exoplanets?", "Slide 3"),
            ("2", "Why Discovery Is Hard", "Slide 4"),
            ("3", "Method 1: Transit Photometry", "Slide 5"),
            ("4", "Method 2: Radial Velocity", "Slide 6"),
            ("5", "Comparing the Two Methods", "Slide 7"),
            ("6", "End-to-End Discovery Pipeline", "Slide 8"),
            ("7", "Recent Exoplanets and Properties", "Slide 9"),
            ("8", "Current Status Snapshot", "Slide 10"),
        ],
    )

    # Slide 3: What are exoplanets?
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="What Are Exoplanets?",
        subtitle="Planets orbiting stars other than the Sun",
        footer_text="Discovery of Exoplanets | slide 3",
    )
    b["two_column_panel_block"](
        slide,
        "Definition",
        [
            "An exoplanet is any planet outside our Solar System.",
            "Most are discovered indirectly from their effect on host stars.",
            "They range from rocky Earth-size worlds to hot gas giants.",
            "Some orbit in habitable zones where liquid water may exist.",
        ],
        "Why They Matter",
        [
            "They test models of planet formation and migration.",
            "Atmospheric studies reveal chemistry and climate clues.",
            "Population statistics show how common planetary systems are.",
            "They guide future searches for potentially life-friendly worlds.",
        ],
    )

    # Slide 4: Challenges
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Why Exoplanet Discovery Is Hard",
        subtitle="The signal is tiny, the noise is everywhere",
        footer_text="Discovery of Exoplanets | slide 4",
    )
    challenge_items = [
        (
            "Extreme Brightness Contrast",
            "A host star can be millions to billions of times brighter than its planet, so planetary light is often buried.",
            palette["ACCENT3"],
        ),
        (
            "Very Small Signals",
            "Typical brightness dips are under 1 percent, and stellar wobble speeds can be only a few meters per second.",
            palette["ACCENT4"],
        ),
        (
            "Stellar Activity",
            "Starspots, flares, and rotation can mimic or distort real planet signatures in both light and spectra.",
            palette["ACCENT"],
        ),
        (
            "Geometry Bias",
            "Transit detection works only when the orbital plane is aligned with our line of sight.",
            palette["ACCENT2"],
        ),
        (
            "Long Confirmation Cycles",
            "Reliable detections often require repeated observations over many orbits and multiple instruments.",
            palette["SUBTITLE_C"],
        ),
    ]
    b["left_border_card_list_block"](
        slide,
        challenge_items,
        top=Inches(1.2),
        row_height=Inches(1.0),
        row_gap=Inches(0.04),
        title_width=Inches(2.7),
        title_size=15,
        desc_size=14,
    )

    # Slide 5: Transit photometry
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Method 1: Transit Photometry",
        subtitle="Measure tiny dips in starlight when a planet crosses in front",
        footer_text="Discovery of Exoplanets | slide 5",
    )
    b["image_caption_card_block"](
        slide,
        "examples/images/transit_light_curve.jpg",
        "Transit Method",
        "When a planet passes in front of its star, observed brightness drops by a small and periodic amount. The dip depth estimates relative size, and repeat timing gives orbital period.",
        height=Inches(5.7),
        image_ratio=0.72,
        fit="contain",
    )

    # Slide 6: Radial velocity
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Method 2: Radial Velocity",
        subtitle="Detect the star's wobble induced by an orbiting planet",
        footer_text="Discovery of Exoplanets | slide 6",
    )
    b["image_caption_card_block"](
        slide,
        "examples/images/radial_velocity_method.jpg",
        "Radial Velocity Method",
        "A planet and star orbit a common center of mass. The star moves toward and away from us, shifting spectral lines via the Doppler effect. This constrains minimum planet mass.",
        height=Inches(5.7),
        image_ratio=0.72,
        fit="contain",
    )

    # Slide 7: Method comparison
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Comparing Transit and Radial Velocity",
        subtitle="Best used together for a fuller planet profile",
        footer_text="Discovery of Exoplanets | slide 7",
    )
    b["coverage_table_block"](
        slide,
        ["Capability", "Transit", "Radial Velocity"],
        [
            ("Planet radius estimate", ("✓", "-")),
            ("Minimum mass estimate", ("-", "✓")),
            ("Orbital period", ("✓", "✓")),
            ("Atmosphere follow-up potential", ("✓", "-")),
            ("Sensitive to face-on orbits", ("-", "✓")),
            ("High false-positive risk alone", ("✓", "-")),
        ],
        insight_text="Combining both methods yields planet density (mass + radius), a key clue to composition.",
        status_positive="✓",
        status_negative="-",
    )

    # Slide 8: Pipeline
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="End-to-End Discovery Pipeline",
        subtitle="From raw observations to validated exoplanets",
        footer_text="Discovery of Exoplanets | slide 8",
    )
    b["pipeline_stages_block"](
        slide,
        [
            ("OBSERVE", "telescopes", "Collect\nphotometry and spectra"),
            ("CALIBRATE", "reduction", "Remove instrument\nnoise and drift"),
            ("DETECT", "search", "Find periodic\ntransit/wobble signals"),
            ("VALIDATE", "checks", "Rule out\nstellar impostors"),
            ("MODEL", "fit", "Estimate orbit,\nsize, and mass"),
            ("PUBLISH", "catalog", "Archive confirmed\nplanets and data"),
        ],
    )
    b["pipeline_strategy_block"](
        slide,
        "Multi-method Confirmation Strategy",
        "Transit candidates are prioritized for radial-velocity follow-up. Agreement between period and phase across methods greatly increases confidence.",
        "# Conceptual workflow\nfor candidate in transit_candidates:\n    if has_periodic_dip(candidate):\n        rv_signal = check_radial_velocity(candidate.star)\n        if period_matches(candidate, rv_signal):\n            confirm_exoplanet(candidate)",
        top=Inches(3.55),
    )

    # Slide 9: Recent exoplanets
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Recent Notable Exoplanets",
        subtitle="Examples with diverse environments",
        footer_text="Discovery of Exoplanets | slide 9",
    )
    b["coverage_table_block"](
        slide,
        ["Property", "K2-18 b", "WASP-39 b", "TOI-700 e"],
        [
            ("Type", ("Mini-Neptune", "Hot Saturn", "Likely rocky")),
            ("Radius", ("~2.6 Earth radii", "~1.27 Jupiter radii", "~0.95 Earth radii")),
            ("Mass", ("~8.6 Earth masses", "~0.28 Jupiter masses", "Pending estimate")),
            ("Orbital period", ("~33 days", "~4.1 days", "~28 days")),
            ("Host star", ("M dwarf", "Sun-like", "M dwarf")),
            ("Distance", ("~124 ly", "~700 ly", "~100 ly")),
            ("Key note", ("Molecule-rich atmosphere", "JWST chemistry target", "Temperate orbit")),
        ],
        top=Inches(1.15),
        row_height=Inches(0.53),
        first_col_width=Inches(3.3),
        insight_text="These planets highlight diversity in size, temperature regime, and atmosphere across recent discoveries.",
        status_positive="Y",
        status_negative="-",
    )

    # Slide 10: Status snapshot + visual
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Current Status Snapshot",
        subtitle="Where exoplanet science is heading next",
        footer_text="Discovery of Exoplanets | slide 10",
    )
    b["code_status_block"](
        slide,
        "# What astronomers seek next\n1. More Earth-size planets in habitable zones\n2. Better mass + radius precision\n3. Atmospheric biosignature constraints\n4. Cross-validation across instruments",
        [
            ("Confirmed exoplanets", "> 5,000"),
            ("Primary survey drivers", "TESS, JWST, Gaia"),
            ("Fast-growing method", "Transit + RV joint analysis"),
            ("Near-term goal", "Characterize temperate rocky worlds"),
        ],
        code_heading="Research priorities",
        status_heading="Field snapshot",
        left=Inches(0.6),
    )

    # Slide 11: Closing visual
    slide = p["blank_slide"](prs)
    b["slide_chrome_block"](
        slide,
        title="Closing",
        subtitle="Each new detection sharpens our understanding of planetary systems",
        footer_text="Discovery of Exoplanets | slide 11",
    )
    b["image_caption_card_block"](
        slide,
        "examples/images/exoplanet-artist-concept.jpg",
        "Beyond Our Solar Neighborhood",
        "Exoplanet discovery has moved from first detections to comparative planetology. The next decade focuses on atmospheres, climate, and potential biosignatures.",
        height=Inches(5.5),
        image_ratio=0.75,
        fit="cover",
    )

    output = "discovery_of_exoplanets.pptx"
    prs.save(output)
    print(f"Saved: {output}")

    findings = detect_overlaps(
        prs,
        min_overlap_ratio=0.01,
        ignore_full_containment=True,
        containment_ratio=0.98,
    )
    if findings:
        print("Potential overlapping elements:")
        for line in format_overlaps(findings):
            print(f"- {line}")
    else:
        print("No significant overlaps detected.")


if __name__ == "__main__":
    main()
