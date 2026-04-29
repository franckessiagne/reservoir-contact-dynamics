"""
figure1.py

Figure 1 – Numerical workflow and structured experiment design.

Corrections included:
- 190 mm figure width.
- 1200 dpi raster export.

Outputs:
- Figure1.png
- Figure1.tiff
- Figure1.pdf
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


def add_box(ax, x, y, w, h, text, face="white", lw=0.9, fontsize=7.0, weight="normal", ls=1.05):
    """Draw a rounded box with centered multi-line text."""
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.010,rounding_size=0.014",
        linewidth=lw,
        edgecolor="black",
        facecolor=face,
    )
    ax.add_patch(box)

    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=weight,
        linespacing=ls,
    )
    return box


def add_arrow(ax, start, end, lw=0.9):
    """Draw a clean arrow between two positions."""
    arr = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=9,
        linewidth=lw,
        color="black",
        shrinkA=4,
        shrinkB=4,
    )
    ax.add_patch(arr)
    return arr


def main():
    # ------------------------------------------------------------------
    # Journal figure specifications
    # ------------------------------------------------------------------
    width_mm = 190
    width_in = width_mm / 25.4
    height_in = width_in * 0.68
    dpi = 1200

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 7.3,
        "axes.linewidth": 0.8,
        "figure.dpi": 300,
        "savefig.dpi": dpi,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    })

    fig, ax = plt.subplots(figsize=(width_in, height_in))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # ------------------------------------------------------------------
    # Title
    # ------------------------------------------------------------------
    ax.text(
        0.5, 0.965,
        "Numerical workflow and structured experiment design",
        ha="center",
        va="center",
        fontsize=10,
        fontweight="bold",
    )

    # ------------------------------------------------------------------
    # Top row: main computational workflow
    # Original structure preserved.
    # Box 5 uses slightly smaller font and manual wrapping to prevent
    # "roughness" from crossing into Box 6.
    # ------------------------------------------------------------------
    top_y = 0.640
    box_h = 0.195
    box_w = 0.153
    gap = 0.0075
    xs = [0.010 + i * (box_w + gap) for i in range(6)]

    workflow = [
        (
            "1. Physical model\nand grid\n\n"
            "3D reservoir grid\n"
            "Black-oil phases\n"
            "Initial OWC/GOC\n"
            "Rock and PVT data"
        ),
        (
            "2. Governing physics\n\n"
            "Capillary pressure\n"
            "Heterogeneity\n"
            "Hysteresis\n"
            "Stress-sensitive k"
        ),
        (
            "3. Transient forcing\n\n"
            "Step-rate depletion\n"
            "Repressurisation cycles\n"
            "Cyclic forcing\n"
            "Rate vs BHP control"
        ),
        (
            "4. Simulation outputs\n\n"
            "UNSMRY/RSM data\n"
            "UNRST fields\n"
            "Pressure P(x,y,z,t)\n"
            "Saturation S(x,y,z,t)"
        ),
        (
            "5. Contact extraction\n\n"
            "OWC/GOC from\n"
            "saturation thresholds\n"
            "Areal contact\n"
            "surfaces\n"
            "Mean depth and\n"
            "roughness"
        ),
        (
            "6. Dynamic diagnosis\n\n"
            "DCMR and RCEI\n"
            "Hysteresis area\n"
            "Phase lag and gain\n"
            "Mobility regimes"
        ),
    ]

    for i, text in enumerate(workflow):
        fontsize = 5.45
        linespacing = 1.05
        if i == 4:
            fontsize = 4.85
            linespacing = 0.98
        add_box(
            ax,
            xs[i],
            top_y,
            box_w,
            box_h,
            text,
            face="0.96",
            fontsize=fontsize,
            ls=linespacing,
        )

    for i in range(5):
        add_arrow(
            ax,
            (xs[i] + box_w, top_y + box_h / 2),
            (xs[i + 1], top_y + box_h / 2),
            lw=0.95,
        )

    # ------------------------------------------------------------------
    # Bottom-left: scenario matrix and sensitivity design
    # ------------------------------------------------------------------
    matrix_x = 0.050
    matrix_y = 0.235
    matrix_w = 0.600
    matrix_h = 0.315

    add_box(ax, matrix_x, matrix_y, matrix_w, matrix_h, "", face="white", lw=0.9)

    ax.text(
        matrix_x + matrix_w / 2,
        matrix_y + matrix_h - 0.035,
        "Numerical experiment matrix",
        ha="center",
        va="center",
        fontsize=8.2,
        fontweight="bold",
    )

    col_titles = [
        "Mechanism\nseparation",
        "Hysteresis\nand memory",
        "Sensitivity\nanalysis",
        "Frequency\nresponse",
        "Control and\nuncertainty",
    ]

    col_bodies = [
        "Pc on/off\nStress-k on/off\nCausal attribution",
        "Depletion–\nrepressurisation\nLoop area, Iirr",
        "Heterogeneity\nkv/kh\nStress level",
        "Cycle periods\nGain\nPhase lag",
        "Rate vs BHP\nInitial OWC/GOC\nP05–P95 bands",
    ]

    col_w = matrix_w / 5
    for i, (title, body) in enumerate(zip(col_titles, col_bodies)):
        cx = matrix_x + i * col_w

        ax.plot(
            [cx, cx],
            [matrix_y, matrix_y + matrix_h - 0.070],
            color="black",
            lw=0.5,
        )

        ax.text(
            cx + col_w / 2,
            matrix_y + matrix_h - 0.095,
            title,
            ha="center",
            va="center",
            fontsize=6.25,
            fontweight="bold",
            linespacing=1.0,
        )

        ax.text(
            cx + col_w / 2,
            matrix_y + 0.105,
            body,
            ha="center",
            va="center",
            fontsize=5.9,
            linespacing=1.05,
        )

    ax.plot(
        [matrix_x + matrix_w, matrix_x + matrix_w],
        [matrix_y, matrix_y + matrix_h - 0.070],
        color="black",
        lw=0.5,
    )
    ax.plot(
        [matrix_x, matrix_x + matrix_w],
        [matrix_y + matrix_h - 0.070, matrix_y + matrix_h - 0.070],
        color="black",
        lw=0.5,
    )

    # Arrow from forcing to experiment matrix
    add_arrow(
        ax,
        (xs[2] + box_w / 2, top_y),
        (matrix_x + matrix_w / 2, matrix_y + matrix_h),
        lw=0.95,
    )

    # ------------------------------------------------------------------
    # Bottom-right: interpretation and field relevance
    # ------------------------------------------------------------------
    interp_x = 0.705
    interp_y = 0.255
    interp_w = 0.255
    interp_h = 0.275

    add_box(
        ax,
        interp_x,
        interp_y,
        interp_w,
        interp_h,
        "Interpretation and use\n\n"
        "Stable, transitional and unstable\n"
        "contact mobility regimes\n\n"
        "Operational screening for\n"
        "transient production decisions\n\n"
        "Transferable interface-tracking\n"
        "workflow for subsurface systems",
        face="0.96",
        fontsize=6.1,
    )

    add_arrow(
        ax,
        (xs[5] + box_w / 2, top_y),
        (interp_x + interp_w / 2, interp_y + interp_h),
        lw=0.95,
    )
    add_arrow(
        ax,
        (matrix_x + matrix_w, matrix_y + matrix_h / 2),
        (interp_x, interp_y + interp_h / 2),
        lw=0.95,
    )

    # ------------------------------------------------------------------
    # Bottom synthesis statement
    # ------------------------------------------------------------------
    outcome_x = 0.060
    outcome_y = 0.050
    outcome_w = 0.880
    outcome_h = 0.125

    outcome_text = (
        "Outcome: a reproducible computational framework that treats reservoir fluid contacts as\n"
        "emergent dynamic interfaces inferred from evolving saturation fields, rather than fixed\n"
        "equilibrium boundaries."
    )

    add_box(
        ax,
        outcome_x,
        outcome_y,
        outcome_w,
        outcome_h,
        outcome_text,
        face="white",
        fontsize=5.85,
        ls=1.12,
    )

    # New arrow requested by user:
    # Numerical experiment matrix -> bottom Outcome box
    add_arrow(
        ax,
        (matrix_x + matrix_w / 2, matrix_y),
        (outcome_x + outcome_w / 2, outcome_y + outcome_h),
        lw=0.95,
    )

    # ------------------------------------------------------------------
    # Export
    # ------------------------------------------------------------------
    fig.savefig(
        "Figure1.png",
        bbox_inches="tight",
        dpi=dpi,
    )
    fig.savefig(
        "Figure1.tiff",
        bbox_inches="tight",
        dpi=dpi,
    )
    fig.savefig(
        "Figure1.pdf",
        bbox_inches="tight",
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
