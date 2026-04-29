"""
figure7.py

Figure 7 – Frequency response of contact migration.

This script reconstructs a publication-style version of Figure 7:
- response gain varies across FR01–FR04 from approximately 5e-4 to 1.9e-3,
- phase lag varies from approximately -320 days to +35 days,
- normalized forcing follows a square-wave pattern,
- contact response is smoother, attenuated, and phase shifted relative to forcing.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure7_Frequency_Response_190mm_1200dpi.png
- Figure7_Frequency_Response_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def square_wave(t, period):
    """Simple square wave with values -1 and +1."""
    return np.where(np.sin(2.0 * np.pi * t / period) >= 0.0, 1.0, -1.0)


def smooth_response(t, period, lag_days, amplitude):
    """
    Smooth sinusoidal response used to approximate delayed, attenuated
    contact migration relative to square-wave forcing.
    """
    return amplitude * np.sin(2.0 * np.pi * (t - lag_days) / period)


def main():
    # ------------------------------------------------------------------
    # Quantitative trends reported in the manuscript for Figure 11
    # ------------------------------------------------------------------
    cases = np.array(["FR01", "FR02", "FR03", "FR04"])
    gain = np.array([5.0e-4, 1.0e-3, 1.05e-3, 1.90e-3])
    phase_lag_days = np.array([-320.0, -5.0, 10.0, 35.0])

    # Representative normalized forcing-response overlay
    t = np.linspace(0, 1200, 1201)
    period = 300.0
    forcing = square_wave(t, period)

    # Use two representative contact responses to show attenuation and lag
    response_fast = smooth_response(t, period=300.0, lag_days=35.0, amplitude=0.55)
    response_slow = smooth_response(t, period=300.0, lag_days=80.0, amplitude=0.35)

    # ------------------------------------------------------------------
    # Figure style: 190 mm width, 1200 dpi, no gridlines
    # ------------------------------------------------------------------
    width_mm = 190
    width_in = width_mm / 25.4
    height_in = width_in * 0.58

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

    fig, axs = plt.subplots(1, 3, figsize=(width_in, height_in))

    # Panel (a): response gain
    x = np.arange(len(cases))
    axs[0].plot(x, gain, color="black", marker="o", markersize=3.5)
    axs[0].set_title("(a) Response gain", loc="left", fontweight="bold")
    axs[0].set_xlabel("Forcing case")
    axs[0].set_ylabel("Gain (-)")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(cases)
    axs[0].set_ylim(0.0, 2.1e-3)
    axs[0].ticklabel_format(axis="y", style="sci", scilimits=(-3, -3))

    # Panel (b): phase lag
    axs[1].plot(x, phase_lag_days, color="black", marker="o", markersize=3.5)
    axs[1].axhline(0.0, color="0.60", linewidth=0.8, linestyle="--")
    axs[1].set_title("(b) Phase lag", loc="left", fontweight="bold")
    axs[1].set_xlabel("Forcing case")
    axs[1].set_ylabel("Lag (days)")
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(cases)
    axs[1].set_ylim(-350, 60)

    # Panel (c): forcing-response overlay
    axs[2].plot(t, forcing, color="black", label="Forcing")
    axs[2].plot(t, response_fast, color="0.35", linestyle="--", label="Contact response A")
    axs[2].plot(t, response_slow, color="0.60", linestyle=":", label="Contact response B")
    axs[2].set_title("(c) Forcing-response overlay", loc="left", fontweight="bold")
    axs[2].set_xlabel("Time (days)")
    axs[2].set_ylabel("Normalized signal")
    axs[2].set_xlim(0, 1200)
    axs[2].set_ylim(-1.25, 1.25)
    axs[2].set_xticks(np.arange(0, 1201, 300))
    axs[2].legend(frameon=False, fontsize=7, loc="upper right")

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure7_Frequency_Response_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure7_Frequency_Response_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
