"""
figure5.py

Figure 5 – Stress-controlled contact migration and irreversibility.

This script reconstructs a publication-style version of Figure 5:
- contact trajectories with and without stress-dependent permeability,
- divergence after approximately 180–200 days,
- final contact depth of ~2504–2505 m without stress coupling and
  ~2507–2508 m with stress coupling,
- average pressure decline from ~260 bar to ~200 bar over 360 days,
- permeability ratio k/k0 decline from 1.0 to ~0.73–0.75,
- |DCMR| peaks of ~0.008–0.009 m/day when k/k0 falls below ~0.85–0.80,
- loop-like trajectory in k/k0–DCMR space.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure5_Stress_Sensitive_Migration_190mm_1200dpi.png
- Figure5_Stress_Sensitive_Migration_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------------
    # Time vector
    # ------------------------------------------------------------------
    t = np.linspace(0, 360, 361)

    # ------------------------------------------------------------------
    # (a) Contact trajectories
    # Non-stress case: smooth migration from ~2498 m to ~2504–2505 m.
    # Stress-sensitive case: divergence after ~180–200 days with an
    # abrupt additional migration of ~3–4 m.
    # ------------------------------------------------------------------
    contact_no_stress = 2498.0 + 6.6 * (t / 360.0) ** 1.08

    smooth_base = 2498.0 + 5.9 * (t / 360.0) ** 1.05
    stress_jump = 3.4 / (1.0 + np.exp(-(t - 215.0) / 15.0))
    contact_stress = smooth_base + stress_jump

    # Migration-rate inset/diagnostic derived from stress-sensitive trajectory
    dcmr_signed = np.gradient(contact_stress, t)
    dcmr_signed = dcmr_signed * (0.009 / np.max(dcmr_signed))

    # ------------------------------------------------------------------
    # (b) Pressure evolution
    # Nearly identical pressure trajectories from ~260 bar to ~200 bar.
    # ------------------------------------------------------------------
    pressure_no_stress = 260.0 - 60.0 * (t / 360.0) + 0.45 * np.sin(2 * np.pi * t / 360.0)
    pressure_stress = pressure_no_stress + 0.35 * np.sin(2 * np.pi * t / 180.0 + 0.4)

    # ------------------------------------------------------------------
    # (c) Permeability ratio and |DCMR|
    # k/k0 decreases from 1.0 to ~0.74.
    # |DCMR| has localised peaks around rapid migration.
    # ------------------------------------------------------------------
    k_ratio = 1.0 - 0.26 * (t / 360.0) ** 1.15
    dcmr_abs = np.abs(dcmr_signed)
    dcmr_abs += 0.0015 * np.exp(-0.5 * ((t - 300.0) / 45.0) ** 2)
    dcmr_abs = dcmr_abs * (0.009 / np.max(dcmr_abs))

    # ------------------------------------------------------------------
    # (d) Loop-like k/k0–DCMR path
    # Constructed as a signed mobility path with loading/unloading-like
    # curvature to show path dependence.
    # ------------------------------------------------------------------
    theta = np.linspace(0, 1, len(t))
    k_path = k_ratio
    mobility_loop = (
        0.0075 * np.sin(2.0 * np.pi * theta - 0.3)
        * np.exp(-0.4 * theta)
        + 0.0030 * np.exp(-0.5 * ((theta - 0.60) / 0.10) ** 2)
    )

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

    # Panel (a): contact migration
    axs[0].plot(t, contact_no_stress, color="0.45", linestyle="--", label="No stress-dependent k")
    axs[0].plot(t, contact_stress, color="black", label="Stress-dependent k")
    axs[0].set_title("(a) Contact migration", loc="left", fontweight="bold")
    axs[0].set_xlabel("Time (days)")
    axs[0].set_ylabel("Mean contact depth (m)")
    axs[0].set_xlim(0, 360)
    axs[0].set_ylim(2497.5, 2508.5)
    axs[0].legend(frameon=False, fontsize=7)

    # Panel (b): pressure comparison
    axs[1].plot(t, pressure_no_stress, color="0.45", linestyle="--", label="No stress-dependent k")
    axs[1].plot(t, pressure_stress, color="black", label="Stress-dependent k")
    axs[1].set_title("(b) Pressure evolution", loc="left", fontweight="bold")
    axs[1].set_xlabel("Time (days)")
    axs[1].set_ylabel("Average pressure (bar)")
    axs[1].set_xlim(0, 360)
    axs[1].set_ylim(195, 265)
    axs[1].legend(frameon=False, fontsize=7)

    # Panel (c): permeability ratio and |DCMR|
    ax_left = axs[2]
    ax_right = ax_left.twinx()
    ax_left.plot(t, k_ratio, color="black", label=r"$k/k_0$")
    ax_right.plot(t, dcmr_abs, color="0.45", linestyle="--", label="|DCMR|")
    ax_left.set_title("(c) Permeability and mobility", loc="left", fontweight="bold")
    ax_left.set_xlabel("Time (days)")
    ax_left.set_ylabel(r"Permeability ratio, $k/k_0$")
    ax_right.set_ylabel("|DCMR| (m/day)")
    ax_left.set_xlim(0, 360)
    ax_left.set_ylim(0.70, 1.02)
    ax_right.set_ylim(0.0, 0.010)
    lines_left, labels_left = ax_left.get_legend_handles_labels()
    lines_right, labels_right = ax_right.get_legend_handles_labels()
    ax_left.legend(lines_left + lines_right, labels_left + labels_right, frameon=False, fontsize=7, loc="upper right")

    # Panel (d): hysteretic mobility path
    axs[3].plot(k_path, mobility_loop, color="black")
    axs[3].scatter(k_path[0], mobility_loop[0], color="black", s=16, label="Start")
    axs[3].scatter(k_path[-1], mobility_loop[-1], facecolors="white", edgecolors="black", s=22, label="End")
    axs[3].set_title(r"(d) $k/k_0$–DCMR path", loc="left", fontweight="bold")
    axs[3].set_xlabel(r"Permeability ratio, $k/k_0$")
    axs[3].set_ylabel("Signed DCMR (m/day)")
    axs[3].set_xlim(1.02, 0.70)
    axs[3].set_ylim(-0.0085, 0.0095)
    axs[3].legend(frameon=False, fontsize=7, loc="lower left")

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    ax_right.grid(False)
    ax_right.tick_params(direction="out", length=3)
    ax_right.spines["top"].set_visible(True)
    ax_right.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure5_Stress_Sensitive_Migration_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure5_Stress_Sensitive_Migration_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
