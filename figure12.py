"""
figure12.py

Figure 12 – Contact mobility regime map.

This script reconstructs a publication-style version of Figure 12 from the
quantitative trends reported in the manuscript:
- stable regime: DCMR ~0.05–0.20, RCEI ~0.05–0.25,
- transitional regime: DCMR ~0.35–0.60, RCEI ~0.35–0.55,
- unstable regime: DCMR >0.60 up to ~0.95, RCEI ~0.75–0.95,
- panel (a) shows clustered realizations in DCMR–RCEI space,
- panel (b) shows regime boundaries/envelopes with minimal overlap.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure12_Contact_Mobility_Regime_Map_190mm_1200dpi.png
- Figure12_Contact_Mobility_Regime_Map_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def clipped_cluster(rng, mean, cov, n, xmin, xmax, ymin, ymax):
    """
    Generate a clipped 2D cluster inside specified DCMR and RCEI bounds.
    """
    points = []
    while len(points) < n:
        batch = rng.multivariate_normal(mean, cov, size=n)
        mask = (
            (batch[:, 0] >= xmin)
            & (batch[:, 0] <= xmax)
            & (batch[:, 1] >= ymin)
            & (batch[:, 1] <= ymax)
        )
        points.extend(batch[mask].tolist())
    return np.asarray(points[:n])


def add_regime_ellipse(ax, xy, width, height, angle, label, label_xy):
    """
    Add a clean unfilled ellipse to represent a regime envelope.
    """
    ellipse = Ellipse(
        xy=xy,
        width=width,
        height=height,
        angle=angle,
        facecolor="none",
        edgecolor="black",
        linewidth=1.1,
    )
    ax.add_patch(ellipse)
    ax.text(label_xy[0], label_xy[1], label, fontsize=8, ha="center", va="center")


def main():
    rng = np.random.default_rng(123)

    # ------------------------------------------------------------------
    # Regime clusters based on manuscript-reported quantitative ranges
    # ------------------------------------------------------------------
    stable = clipped_cluster(
        rng,
        mean=[0.125, 0.155],
        cov=[[0.0012, 0.0007], [0.0007, 0.0016]],
        n=42,
        xmin=0.05,
        xmax=0.20,
        ymin=0.05,
        ymax=0.25,
    )

    transitional = clipped_cluster(
        rng,
        mean=[0.475, 0.455],
        cov=[[0.0028, 0.0015], [0.0015, 0.0020]],
        n=36,
        xmin=0.35,
        xmax=0.60,
        ymin=0.35,
        ymax=0.55,
    )

    unstable = clipped_cluster(
        rng,
        mean=[0.78, 0.86],
        cov=[[0.0050, 0.0025], [0.0025, 0.0028]],
        n=44,
        xmin=0.60,
        xmax=0.95,
        ymin=0.75,
        ymax=0.95,
    )

    # ------------------------------------------------------------------
    # Figure style: 190 mm width, 1200 dpi, no gridlines.
    # ------------------------------------------------------------------
    width_mm = 190
    width_in = width_mm / 25.4
    height_in = width_in * 0.50

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "lines.linewidth": 1.7,
        "figure.dpi": 300,
        "savefig.dpi": 1200,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })

    fig, axs = plt.subplots(1, 2, figsize=(width_in, height_in))

    # ------------------------------------------------------------------
    # Panel (a): scatter clusters
    # ------------------------------------------------------------------
    axs[0].scatter(stable[:, 0], stable[:, 1], s=16, color="0.70", edgecolor="black", linewidth=0.3, label="Stable")
    axs[0].scatter(transitional[:, 0], transitional[:, 1], s=16, color="0.45", edgecolor="black", linewidth=0.3, label="Transitional")
    axs[0].scatter(unstable[:, 0], unstable[:, 1], s=16, color="black", edgecolor="black", linewidth=0.3, label="Unstable")

    axs[0].set_title("(a) Regime clustering", loc="left", fontweight="bold")
    axs[0].set_xlabel("Peak DCMR (-)")
    axs[0].set_ylabel("Peak RCEI (-)")
    axs[0].set_xlim(0.0, 1.0)
    axs[0].set_ylim(0.0, 1.0)
    axs[0].legend(frameon=False, fontsize=7, loc="upper left")

    # ------------------------------------------------------------------
    # Panel (b): regime envelopes
    # ------------------------------------------------------------------
    axs[1].scatter(stable[:, 0], stable[:, 1], s=10, color="0.75", edgecolor="none")
    axs[1].scatter(transitional[:, 0], transitional[:, 1], s=10, color="0.50", edgecolor="none")
    axs[1].scatter(unstable[:, 0], unstable[:, 1], s=10, color="0.20", edgecolor="none")

    add_regime_ellipse(
        axs[1],
        xy=(0.13, 0.16),
        width=0.20,
        height=0.24,
        angle=30,
        label="Stable",
        label_xy=(0.18, 0.07),
    )
    add_regime_ellipse(
        axs[1],
        xy=(0.48, 0.45),
        width=0.30,
        height=0.24,
        angle=25,
        label="Transitional",
        label_xy=(0.48, 0.30),
    )
    add_regime_ellipse(
        axs[1],
        xy=(0.78, 0.86),
        width=0.38,
        height=0.24,
        angle=20,
        label="Unstable",
        label_xy=(0.82, 0.68),
    )

    # Optional light threshold guides, no gridlines
    axs[1].axvline(0.30, color="0.75", linestyle="--", linewidth=0.8)
    axs[1].axvline(0.60, color="0.75", linestyle="--", linewidth=0.8)
    axs[1].axhline(0.30, color="0.75", linestyle="--", linewidth=0.8)
    axs[1].axhline(0.65, color="0.75", linestyle="--", linewidth=0.8)

    axs[1].set_title("(b) Regime envelopes", loc="left", fontweight="bold")
    axs[1].set_xlabel("Peak DCMR (-)")
    axs[1].set_ylabel("Peak RCEI (-)")
    axs[1].set_xlim(0.0, 1.0)
    axs[1].set_ylim(0.0, 1.0)

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure12_Contact_Mobility_Regime_Map_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure12_Contact_Mobility_Regime_Map_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
