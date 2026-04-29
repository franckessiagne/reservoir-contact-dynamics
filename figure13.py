"""
figure13.py

Figure 13 – Schematic synthesis of governing mechanisms, dynamic contact
behaviours, diagnostic metrics, and field-scale implications.

This script generates a publication-style conceptual synthesis figure. The schematic summarizes the interpretation developed from the
numerical results:
- governing mechanisms: capillarity, heterogeneity, stress sensitivity, forcing,
  and hysteresis,
- dynamic behaviours: delayed mobilisation, abrupt migration, roughening,
  irreversible displacement, frequency filtering, and regime transition,
- diagnostics: contact extraction, DCMR, RCEI, hysteresis loop area, phase lag,
  and regime map,
- implications: forecasting, operational control, surveillance, risk screening,
  and transferability to other subsurface systems.

Outputs:
- Figure13_Schematic_Synthesis_190mm_1200dpi.png
- Figure13_Schematic_Synthesis_190mm_1200dpi.tiff
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def add_box(ax, xy, width, height, text, fontsize=7.5, facecolor="white"):
    """Add a rounded text box."""
    box = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=0.9,
        edgecolor="black",
        facecolor=facecolor,
    )
    ax.add_patch(box)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        wrap=True,
    )
    return box


def add_arrow(ax, start, end, connectionstyle="arc3,rad=0.0"):
    """Add an arrow between two points."""
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=10,
        linewidth=0.9,
        color="black",
        connectionstyle=connectionstyle,
        shrinkA=4,
        shrinkB=4,
    )
    ax.add_patch(arrow)
    return arrow


def main():
    # ------------------------------------------------------------------
    # Figure style: 190 mm width, 1200 dpi, no gridlines.
    # ------------------------------------------------------------------
    width_mm = 190
    width_in = width_mm / 25.4
    height_in = width_in * 0.70

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "axes.linewidth": 0.8,
        "figure.dpi": 300,
        "savefig.dpi": 1200,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })

    fig, ax = plt.subplots(figsize=(width_in, height_in))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # ------------------------------------------------------------------
    # Column headers
    # ------------------------------------------------------------------
    ax.text(0.14, 0.95, "Governing mechanisms", ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(0.39, 0.95, "Dynamic contact behaviours", ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(0.64, 0.95, "Diagnostics", ha="center", va="center", fontsize=9, fontweight="bold")
    ax.text(0.86, 0.95, "Field-scale implications", ha="center", va="center", fontsize=9, fontweight="bold")

    # ------------------------------------------------------------------
    # Mechanism boxes
    # ------------------------------------------------------------------
    mechanism_texts = [
        "Capillary pressure\nand entry barriers",
        "Capillary/permeability\nheterogeneity",
        "Stress-dependent\npermeability",
        "Transient and cyclic\nproduction forcing",
        "Relative-permeability\nhysteresis",
    ]

    mech_boxes = []
    y_positions = [0.78, 0.63, 0.48, 0.33, 0.18]
    for y, txt in zip(y_positions, mechanism_texts):
        mech_boxes.append(add_box(ax, (0.03, y), 0.22, 0.095, txt, fontsize=7.2, facecolor="0.96"))

    # ------------------------------------------------------------------
    # Behaviour boxes
    # ------------------------------------------------------------------
    behaviour_texts = [
        "Delayed mobilisation\nand threshold response",
        "Abrupt migration\nbursts",
        "Non-planar contact\nroughening",
        "Irreversible displacement\nand reservoir memory",
        "Frequency attenuation\nand phase lag",
        "Stable–transitional–\nunstable regime shift",
    ]

    beh_boxes = []
    y_beh = [0.80, 0.67, 0.54, 0.41, 0.28, 0.15]
    for y, txt in zip(y_beh, behaviour_texts):
        beh_boxes.append(add_box(ax, (0.30, y), 0.22, 0.085, txt, fontsize=7.0, facecolor="white"))

    # ------------------------------------------------------------------
    # Diagnostic boxes
    # ------------------------------------------------------------------
    diag_texts = [
        "Saturation-threshold\ncontact extraction",
        "DCMR:\ninstantaneous mobility",
        "RCEI:\npressure sensitivity",
        "Hysteresis loop area\nand irreversibility index",
        "Gain, phase lag,\nand regime map",
    ]

    diag_boxes = []
    y_diag = [0.78, 0.63, 0.48, 0.33, 0.18]
    for y, txt in zip(y_diag, diag_texts):
        diag_boxes.append(add_box(ax, (0.56, y), 0.18, 0.095, txt, fontsize=6.9, facecolor="0.96"))

    # ------------------------------------------------------------------
    # Implication boxes
    # ------------------------------------------------------------------
    implication_texts = [
        "Improved forecasting\nof moving contacts",
        "Operational mitigation:\nBHP control and rate design",
        "Surveillance targeting\nand early warning",
        "Risk screening using\nmobility regimes",
        "Transferable to CO2 storage,\ngas storage, aquifers,\nand contaminant fronts",
    ]

    imp_boxes = []
    y_imp = [0.78, 0.63, 0.48, 0.33, 0.15]
    for y, txt in zip(y_imp, implication_texts):
        imp_boxes.append(add_box(ax, (0.79, y), 0.18, 0.095 if y != 0.15 else 0.13, txt, fontsize=6.8, facecolor="white"))

    # ------------------------------------------------------------------
    # Arrows: mechanisms -> behaviours
    # ------------------------------------------------------------------
    pairs_mech_beh = [
        (0, 0),  # capillary -> delay
        (0, 1),  # capillary -> burst
        (1, 2),  # heterogeneity -> roughening
        (2, 3),  # stress -> irreversibility
        (3, 4),  # cyclic forcing -> frequency response
        (4, 3),  # hysteresis -> memory
        (3, 5),  # forcing -> regime shift
    ]

    for i, j in pairs_mech_beh:
        start = (0.25, y_positions[i] + 0.047)
        end = (0.30, y_beh[j] + 0.043)
        add_arrow(ax, start, end)

    # ------------------------------------------------------------------
    # Arrows: behaviours -> diagnostics
    # ------------------------------------------------------------------
    pairs_beh_diag = [
        (0, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (3, 3),
        (4, 4),
        (5, 4),
    ]

    for i, j in pairs_beh_diag:
        start = (0.52, y_beh[i] + 0.043)
        end = (0.56, y_diag[j] + 0.047)
        add_arrow(ax, start, end)

    # ------------------------------------------------------------------
    # Arrows: diagnostics -> implications
    # ------------------------------------------------------------------
    pairs_diag_imp = [
        (0, 0),
        (1, 3),
        (2, 0),
        (3, 2),
        (4, 3),
        (4, 4),
    ]

    for i, j in pairs_diag_imp:
        start = (0.74, y_diag[i] + 0.047)
        end = (0.79, y_imp[j] + (0.047 if j != 4 else 0.065))
        add_arrow(ax, start, end)

    # ------------------------------------------------------------------
    # Bottom synthesis statement
    # ------------------------------------------------------------------
    add_box(
        ax,
        (0.12, 0.025),
        0.76,
        0.075,
        "Fluid contacts are treated as emergent dynamic interfaces inferred from saturation fields, "
        "rather than fixed equilibrium boundaries.",
        fontsize=7.3,
        facecolor="0.93",
    )

    fig.savefig("Figure13_Schematic_Synthesis_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure13_Schematic_Synthesis_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
