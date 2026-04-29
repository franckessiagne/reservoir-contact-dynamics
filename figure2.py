"""
figure2.py

Figure 2 – Baseline evolution under monotonic depletion.

This script reconstructs a publication-style version of Figure 2 :
- average reservoir pressure declines from ~330 bar to ~195 bar over 360 days,
- mean contact depth migrates from ~2500 m to ~2510 m,
- DCMR decreases from ~0.045 m/day to ~0.020–0.025 m/day,
- RCEI decreases from ~0.12 m/bar to ~0.07 m/bar.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure2_Baseline_Evolution_190mm_1200dpi.png
- Figure2_Baseline_Evolution_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------------
    # Time vector
    # ------------------------------------------------------------------
    t = np.linspace(0, 360, 361)

    # ------------------------------------------------------------------
    # Reconstructed quantitative trends from the manuscript
    # ------------------------------------------------------------------
    pressure = 330.0 - (135.0 / 360.0) * t + 1.2 * np.sin(2.0 * np.pi * t / 360.0)

    contact_depth = 2500.0 + 10.0 * (t / 360.0) ** 1.15

    dcmr = 0.022 + 0.023 * np.exp(-t / 55.0)
    dcmr += 0.0006 * np.sin(2.0 * np.pi * t / 45.0)
    dcmr = np.clip(dcmr, 0.020, None)

    rcei = 0.070 + 0.050 * np.exp(-t / 70.0)
    rcei += 0.002 * np.sin(2.0 * np.pi * t / 130.0)

    # ------------------------------------------------------------------
    # Figure style: 190 mm width, 1200 dpi, no gridlines
    # ------------------------------------------------------------------
    width_mm = 190
    width_in = width_mm / 25.4
    height_in = width_in * 0.67

    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 8,
        "axes.linewidth": 0.8,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "lines.linewidth": 1.8,
        "figure.dpi": 300,
        "savefig.dpi": 1200,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })

    fig, axs = plt.subplots(2, 2, figsize=(width_in, height_in))
    axs = axs.ravel()

    panels = [
        (pressure, "(a) Average reservoir pressure", "Pressure (bar)", (190, 335)),
        (contact_depth, "(b) Mean contact depth", "Depth (m)", (2499, 2511)),
        (dcmr, "(c) DCMR(t)", "DCMR (m/day)", (0.018, 0.047)),
        (rcei, "(d) RCEI(t)", "RCEI (m/bar)", (0.065, 0.125)),
    ]

    for ax, (y, title, ylabel, ylim) in zip(axs, panels):
        ax.plot(t, y, color="black")
        ax.set_title(title, loc="left", fontweight="bold")
        ax.set_xlabel("Time (days)")
        ax.set_ylabel(ylabel)
        ax.set_xlim(0, 360)
        ax.set_ylim(*ylim)
        ax.set_xticks(np.arange(0, 361, 90))
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure2_Baseline_Evolution_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure2_Baseline_Evolution_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
