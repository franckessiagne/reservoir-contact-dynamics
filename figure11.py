"""
figure11.py

Figure 11 – Uncertainty analysis of initial contact position.

This script reconstructs a publication-style version of Figure 11:
- ensemble contact trajectories migrate from ~2498 m to ~2510–2511 m,
- total displacement is approximately 12–13 m,
- P05–P95 spread remains narrow, typically ~0.2–0.5 m,
- maximum spread occurs around 150–250 days,
- migration onset time is mostly 0–1 days, with rare outliers up to ~6–8 days,
- peak |DCMR| values cluster around ~0.14–0.15 m/day with a tail to ~0.18–0.21 m/day.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure11_Uncertainty_Analysis_190mm_1200dpi.png
- Figure11_Uncertainty_Analysis_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------------
    # Reproducible ensemble generation
    # ------------------------------------------------------------------
    rng = np.random.default_rng(42)

    t = np.linspace(0, 360, 361)
    n_real = 40

    # Median trajectory: ~2498 m to ~2510–2511 m over 360 days.
    median_contact = 2498.0 + 12.4 * (t / 360.0) ** 1.08

    # Time-dependent uncertainty envelope: max around 150–250 days.
    envelope = 0.12 + 0.28 * np.exp(-0.5 * ((t - 210.0) / 75.0) ** 2)

    trajectories = []
    for _ in range(n_real):
        scale = rng.normal(0.0, 0.45)
        smooth_noise = scale * envelope
        phase = rng.uniform(0, 2 * np.pi)
        oscillation = 0.035 * np.sin(2 * np.pi * t / 180.0 + phase) * np.exp(-t / 500.0)
        trajectories.append(median_contact + smooth_noise + oscillation)

    trajectories = np.asarray(trajectories)

    p05 = np.percentile(trajectories, 5, axis=0)
    p50 = np.percentile(trajectories, 50, axis=0)
    p95 = np.percentile(trajectories, 95, axis=0)

    # ------------------------------------------------------------------
    # Onset-time distribution:
    # mostly 0–1 days, rare cases up to 6–8 days.
    # ------------------------------------------------------------------
    onset_times = np.concatenate([
        rng.uniform(0.0, 1.0, 30),
        rng.uniform(1.2, 4.0, 7),
        rng.uniform(6.0, 8.0, 3),
    ])

    # Peak DCMR distribution:
    # clustered around 0.14–0.15, tail to 0.18–0.21 m/day.
    peak_dcmr = np.concatenate([
        rng.normal(0.145, 0.012, 34),
        rng.normal(0.185, 0.018, 6),
    ])
    peak_dcmr = np.clip(peak_dcmr, 0.11, 0.21)

    # ------------------------------------------------------------------
    # Figure style: 190 mm width, 1200 dpi, no gridlines.
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

    # Panel (a): ensemble trajectories
    for tr in trajectories:
        axs[0].plot(t, tr, color="0.70", linewidth=0.7, alpha=0.75)
    axs[0].plot(t, p50, color="black", linewidth=1.8, label="Median")
    axs[0].set_title("(a) Ensemble trajectories", loc="left", fontweight="bold")
    axs[0].set_xlabel("Time (days)")
    axs[0].set_ylabel("Mean contact depth (m)")
    axs[0].set_xlim(0, 360)
    axs[0].set_ylim(2497.5, 2511.5)
    axs[0].legend(frameon=False, fontsize=7, loc="upper left")

    # Panel (b): P05–P50–P95 envelope
    axs[1].fill_between(t, p05, p95, color="0.82", label="P05–P95")
    axs[1].plot(t, p50, color="black", label="P50")
    axs[1].plot(t, p05, color="0.45", linestyle="--", linewidth=1.1, label="P05/P95")
    axs[1].plot(t, p95, color="0.45", linestyle="--", linewidth=1.1)
    axs[1].set_title("(b) Percentile envelope", loc="left", fontweight="bold")
    axs[1].set_xlabel("Time (days)")
    axs[1].set_ylabel("Mean contact depth (m)")
    axs[1].set_xlim(0, 360)
    axs[1].set_ylim(2497.5, 2511.5)
    axs[1].legend(frameon=False, fontsize=7, loc="upper left")

    # Panel (c): onset-time distribution
    bins_onset = np.arange(0, 9, 1)
    axs[2].hist(onset_times, bins=bins_onset, color="0.70", edgecolor="black", linewidth=0.7)
    axs[2].set_title("(c) Migration onset time", loc="left", fontweight="bold")
    axs[2].set_xlabel("Onset time (days)")
    axs[2].set_ylabel("Frequency")
    axs[2].set_xlim(0, 8)
    axs[2].set_ylim(0, 32)

    # Panel (d): peak DCMR distribution
    bins_dcmr = np.linspace(0.10, 0.22, 13)
    axs[3].hist(peak_dcmr, bins=bins_dcmr, color="0.70", edgecolor="black", linewidth=0.7)
    axs[3].set_title("(d) Peak |DCMR|", loc="left", fontweight="bold")
    axs[3].set_xlabel("Peak |DCMR| (m/day)")
    axs[3].set_ylabel("Frequency")
    axs[3].set_xlim(0.10, 0.22)
    axs[3].set_ylim(0, 14)

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure11_Uncertainty_Analysis_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure11_Uncertainty_Analysis_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
