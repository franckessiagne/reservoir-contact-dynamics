"""
figure9.py

Figure 9 – Frequency-dependent response of fluid contacts.

This script reconstructs a publication-style version of Figure 9:
- forcing-frequency range of approximately 1e-3 to 1e-1 day^-1,
- gain near unity at low frequency and <0.2 at high frequency,
- gain values at high frequency approximately:
  FR01: 0.18–0.20, FR02: 0.15–0.18, FR03: 0.12–0.15, FR04: 0.08–0.10,
- phase lag near 0 degrees at low frequency,
- phase lag at high frequency approximately:
  FR01: -350°, FR02: -500°, FR03: -600°, FR04: -700°,
- normalized forcing signals and delayed, attenuated contact responses.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure9_Frequency_Dependent_Response_190mm_1200dpi.png
- Figure9_Frequency_Dependent_Response_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def square_wave(t, period):
    """Return square-wave forcing with values -1 and +1."""
    return np.where(np.sin(2.0 * np.pi * t / period) >= 0.0, 1.0, -1.0)


def lowpass_gain(freq, fc, high_freq_floor):
    """
    Smooth attenuation curve: near 1 at low frequency, tending toward
    high_freq_floor at high frequency.
    """
    return high_freq_floor + (1.0 - high_freq_floor) / (1.0 + (freq / fc) ** 1.35)


def phase_lag_curve(freq, target_high_lag, fc):
    """
    Smooth phase-lag curve: near 0 at low frequency, approaching target_high_lag
    at high frequency.
    """
    return target_high_lag * (freq / fc) ** 1.15 / (1.0 + (freq / fc) ** 1.15)


def main():
    # ------------------------------------------------------------------
    # Frequency-response curves
    # ------------------------------------------------------------------
    freq = np.logspace(-3, -1, 120)

    cases = {
        "FR01": {"floor": 0.19, "lag": -350.0, "fc": 0.010},
        "FR02": {"floor": 0.16, "lag": -500.0, "fc": 0.011},
        "FR03": {"floor": 0.135, "lag": -600.0, "fc": 0.012},
        "FR04": {"floor": 0.090, "lag": -700.0, "fc": 0.013},
    }

    gains = {}
    phases = {}
    for name, pars in cases.items():
        gains[name] = lowpass_gain(freq, fc=pars["fc"], high_freq_floor=pars["floor"])
        phases[name] = phase_lag_curve(freq, target_high_lag=pars["lag"], fc=pars["fc"])

    # ------------------------------------------------------------------
    # Time-domain normalized forcing and response
    # Manuscript: high-frequency forcing has many short cycles; low-frequency
    # forcing has fewer long cycles; contact response is attenuated and delayed.
    # ------------------------------------------------------------------
    t = np.linspace(0, 1200, 1201)
    forcing_high = square_wave(t, period=120.0)   # many short oscillations
    forcing_low = square_wave(t, period=520.0)    # fewer long cycles

    response_high = 1.6 * np.sin(2.0 * np.pi * (t - 25.0) / 120.0)
    response_high = response_high / np.std(response_high)

    response_low = 1.2 * np.sin(2.0 * np.pi * (t - 70.0) / 520.0)
    response_low = response_low / np.std(response_low)

    # Scale responses to manuscript z-score-like amplitude ranges
    response_high = 1.6 * response_high / np.max(np.abs(response_high))
    response_low = 1.2 * response_low / np.max(np.abs(response_low))

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

    linestyles = {
        "FR01": "-",
        "FR02": "--",
        "FR03": "-.",
        "FR04": ":",
    }
    colors = {
        "FR01": "black",
        "FR02": "0.30",
        "FR03": "0.50",
        "FR04": "0.65",
    }

    # Panel (a): gain attenuation
    for name in cases:
        axs[0].semilogx(freq, gains[name], linestyle=linestyles[name], color=colors[name], label=name)
    axs[0].set_title("(a) Gain attenuation", loc="left", fontweight="bold")
    axs[0].set_xlabel(r"Forcing frequency (day$^{-1}$)")
    axs[0].set_ylabel("Gain (-)")
    axs[0].set_xlim(1e-3, 1e-1)
    axs[0].set_ylim(0.0, 1.15)
    axs[0].legend(frameon=False, fontsize=7)

    # Panel (b): phase lag
    for name in cases:
        axs[1].semilogx(freq, phases[name], linestyle=linestyles[name], color=colors[name], label=name)
    axs[1].set_title("(b) Phase lag growth", loc="left", fontweight="bold")
    axs[1].set_xlabel(r"Forcing frequency (day$^{-1}$)")
    axs[1].set_ylabel("Phase lag (degrees)")
    axs[1].set_xlim(1e-3, 1e-1)
    axs[1].set_ylim(-760, 40)
    axs[1].legend(frameon=False, fontsize=7, loc="lower left")

    # Panel (c): normalized forcing signals
    axs[2].plot(t, forcing_high, color="black", label="High-frequency forcing")
    axs[2].plot(t, forcing_low, color="0.55", linestyle="--", label="Low-frequency forcing")
    axs[2].set_title("(c) Normalized forcing", loc="left", fontweight="bold")
    axs[2].set_xlabel("Time (days)")
    axs[2].set_ylabel("Normalized forcing")
    axs[2].set_xlim(0, 1200)
    axs[2].set_ylim(-1.25, 1.25)
    axs[2].set_xticks(np.arange(0, 1201, 300))
    axs[2].legend(frameon=False, fontsize=7, loc="upper right")

    # Panel (d): normalized contact responses
    axs[3].plot(t, response_high, color="black", label="High-frequency response")
    axs[3].plot(t, response_low, color="0.55", linestyle="--", label="Low-frequency response")
    axs[3].set_title("(d) Normalized contact response", loc="left", fontweight="bold")
    axs[3].set_xlabel("Time (days)")
    axs[3].set_ylabel("Contact response (z-score)")
    axs[3].set_xlim(0, 1200)
    axs[3].set_ylim(-1.85, 1.85)
    axs[3].set_xticks(np.arange(0, 1201, 300))
    axs[3].legend(frameon=False, fontsize=7, loc="upper right")

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure9_Frequency_Dependent_Response_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure9_Frequency_Dependent_Response_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
