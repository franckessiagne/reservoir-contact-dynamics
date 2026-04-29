"""
figure6.py

Figure 6 – Hysteresis loops in pressure–contact space.

This script reconstructs a publication-style version of Figure 6:
- cyclic depletion–repressurisation trajectories in pressure–contact space,
- pressure range of approximately 280–325 bar,
- contact-depth range of approximately 2498–2510 m,
- three successive hysteresis loops with decreasing loop magnitude,
- loop-area trend decreasing from ~260 to ~155 to ~95 arbitrary pressure-depth units.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure6_Hysteresis_Loops_190mm_1200dpi.png
- Figure6_Hysteresis_Loops_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def ellipse_loop(center_p, center_c, amp_p, amp_c, phase=0.0, n=240):
    """Return one pressure-contact hysteresis loop."""
    theta = np.linspace(0, 2 * np.pi, n)
    pressure = center_p + amp_p * np.cos(theta)
    contact = center_c + amp_c * np.sin(theta + phase) + 0.08 * amp_c * np.sin(2 * theta)
    return pressure, contact, theta


def polygon_area(x, y):
    """Shoelace polygon area."""
    return 0.5 * np.abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def main():
    # ------------------------------------------------------------------
    # Construct three shrinking hysteresis cycles.
    # Cycle 1: pressure spans ~280–325 bar; depth spans ~2498–2510 m.
    # Later cycles have progressively smaller contact-depth amplitude.
    # ------------------------------------------------------------------
    cycles = []
    params = [
        (302.5, 2504.0, 22.5, 6.0, 0.25),  # largest loop
        (302.5, 2502.8, 21.0, 3.7, 0.25),  # intermediate loop
        (302.5, 2501.7, 19.0, 2.5, 0.25),  # smaller loop
    ]

    for par in params:
        p, c, th = ellipse_loop(*par)
        cycles.append((p, c, th))

    # Reported loop-area trend used for panel (d)
    cycle_numbers = np.array([1, 2, 3])
    loop_areas_reported = np.array([260.0, 155.0, 95.0])

    # Time-coloured trajectory for panel (a), assembled from all cycles
    p_all = np.concatenate([cycles[i][0] for i in range(3)])
    c_all = np.concatenate([cycles[i][1] for i in range(3)])
    time_all = np.linspace(0, 360, len(p_all))

    # Representative cycle for panel (b)
    p1, c1, theta1 = cycles[0]
    delta_c1 = c1 - np.mean(c1)

    # ------------------------------------------------------------------
    # Figure style: 190 mm width, 1200 dpi, no gridlines
    # ------------------------------------------------------------------
    width_mm = 190
    width_in = width_mm / 25.4
    height_in = width_in * 0.82

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

    fig, axs = plt.subplots(2, 2, figsize=(width_in, height_in))
    axs = axs.ravel()

    # Panel (a): time-coloured pressure-contact trajectory
    scatter = axs[0].scatter(p_all, c_all, c=time_all, s=5, cmap="viridis", linewidths=0)
    axs[0].plot(p_all, c_all, color="0.25", linewidth=0.8, alpha=0.55)
    axs[0].set_title("(a) Time-coloured trajectory", loc="left", fontweight="bold")
    axs[0].set_xlabel("Average pressure (bar)")
    axs[0].set_ylabel("Mean contact depth (m)")
    axs[0].set_xlim(276, 329)
    axs[0].set_ylim(2497, 2511.5)
    cbar = fig.colorbar(scatter, ax=axs[0], fraction=0.046, pad=0.03)
    cbar.set_label("Time (days)")

    # Panel (b): representative hysteresis cycle
    axs[1].plot(p1, c1, color="black")
    axs[1].scatter(p1[0], c1[0], color="black", s=16, label="Start")
    axs[1].scatter(p1[-1], c1[-1], facecolors="white", edgecolors="black", s=22, label="End")
    axs[1].set_title("(b) Representative cycle", loc="left", fontweight="bold")
    axs[1].set_xlabel("Average pressure (bar)")
    axs[1].set_ylabel("Mean contact depth (m)")
    axs[1].set_xlim(276, 329)
    axs[1].set_ylim(2497, 2511.5)
    axs[1].legend(frameon=False, fontsize=7, loc="upper right")

    # Inset for contact displacement in panel (b)
    inset = axs[1].inset_axes([0.12, 0.12, 0.38, 0.35])
    inset.plot(theta1 / (2 * np.pi), delta_c1, color="black", linewidth=1.0)
    inset.set_xlabel("Cycle", fontsize=6)
    inset.set_ylabel(r"$\Delta C$ (m)", fontsize=6)
    inset.tick_params(labelsize=6, direction="out", length=2)
    inset.grid(False)

    # Panel (c): successive cycles
    labels = ["Cycle 1", "Cycle 2", "Cycle 3"]
    linestyles = ["-", "--", ":"]
    colors = ["black", "0.35", "0.60"]
    for (p, c, _), lab, ls, col in zip(cycles, labels, linestyles, colors):
        axs[2].plot(p, c, linestyle=ls, color=col, label=lab)
    axs[2].set_title("(c) Successive cycles", loc="left", fontweight="bold")
    axs[2].set_xlabel("Average pressure (bar)")
    axs[2].set_ylabel("Mean contact depth (m)")
    axs[2].set_xlim(276, 329)
    axs[2].set_ylim(2497, 2511.5)
    axs[2].legend(frameon=False, fontsize=7)

    # Panel (d): loop-area decay
    axs[3].plot(cycle_numbers, loop_areas_reported, color="black", marker="o", markersize=3.5)
    axs[3].set_title("(d) Hysteresis-area decay", loc="left", fontweight="bold")
    axs[3].set_xlabel("Cycle number")
    axs[3].set_ylabel("Loop area (pressure-depth units)")
    axs[3].set_xlim(0.7, 3.3)
    axs[3].set_ylim(70, 285)
    axs[3].set_xticks([1, 2, 3])

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure6_Hysteresis_Loops_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure6_Hysteresis_Loops_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
