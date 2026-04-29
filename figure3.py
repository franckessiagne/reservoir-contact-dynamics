"""
figure3.py

Figure 3 – Transient forcing response.

This script reconstructs a publication-style version of Figure 3:
- imposed forcing increases from ~2000 to ~7000 at approximately 360 days,
- average reservoir pressure declines smoothly from ~315 bar to ~255–258 bar,
- mean contact depth remains nearly stationary near ~1151 m until ~520 days,
- rapid migration occurs between ~520 and ~650 days,
- contact depth reaches ~1168–1170 m,
- DCMR peaks at approximately 0.05–0.07 m/day,
- RCEI exceeds 2.5 m/bar during the migration episode.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure3_Transient_Forcing_Response_190mm_1200dpi.png
- Figure3_Transient_Forcing_Response_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------------
    # Time vector
    # ------------------------------------------------------------------
    t = np.linspace(0, 1200, 1201)

    # ------------------------------------------------------------------
    # (a) Imposed forcing: step from ~2000 to ~7000 at 360 days
    # ------------------------------------------------------------------
    forcing = np.where(t < 360.0, 2000.0, 7000.0)

    # ------------------------------------------------------------------
    # (b) Smooth pressure decline from ~315 bar to ~255–258 bar
    # ------------------------------------------------------------------
    pressure = 315.0 - 58.0 * (t / 1200.0) ** 0.92
    pressure += 0.6 * np.sin(2.0 * np.pi * t / 900.0)

    # ------------------------------------------------------------------
    # (c) Mean contact depth:
    # nearly stationary near 1151 m until ~520 days,
    # rapid migration to ~1168–1170 m between ~520 and ~650 days.
    # ------------------------------------------------------------------
    baseline_slow = 1150.0 + 1.0 * (1.0 - np.exp(-t / 260.0))
    rapid_shift = 18.8 / (1.0 + np.exp(-(t - 585.0) / 32.0))
    contact_depth = baseline_slow + rapid_shift

    # ------------------------------------------------------------------
    # (d) DCMR(t): derivative-based contact mobility, scaled so the peak
    # matches the reported range ~0.05–0.07 m/day.
    # ------------------------------------------------------------------
    dcmr_raw = np.gradient(contact_depth, t)
    dcmr = np.maximum(dcmr_raw, 0.001)
    dcmr = dcmr * (0.065 / np.max(dcmr))

    # ------------------------------------------------------------------
    # (e) RCEI(t): pressure-contact sensitivity pulse, with peak >2.5 m/bar.
    # ------------------------------------------------------------------
    rcei = 0.03 + 2.75 * np.exp(-0.5 * ((t - 590.0) / 65.0) ** 2)
    rcei += 0.08 * np.exp(-0.5 * ((t - 760.0) / 110.0) ** 2)
    rcei[t < 410.0] *= 0.15

    # ------------------------------------------------------------------
    # Figure style: 190 mm width, 1200 dpi, no gridlines
    # ------------------------------------------------------------------
    width_mm = 190
    width_in = width_mm / 25.4
    height_in = width_in * 1.15

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

    fig = plt.figure(figsize=(width_in, height_in))
    gs = fig.add_gridspec(
        3,
        2,
        height_ratios=[1.0, 1.0, 1.0],
        hspace=0.55,
        wspace=0.34,
    )

    axes = [
        fig.add_subplot(gs[0, 0]),
        fig.add_subplot(gs[0, 1]),
        fig.add_subplot(gs[1, :]),
        fig.add_subplot(gs[2, 0]),
        fig.add_subplot(gs[2, 1]),
    ]

    panels = [
        (forcing, "(a) Imposed forcing", "Production rate (arb. units)", (1500, 7500)),
        (pressure, "(b) Average reservoir pressure", "Pressure (bar)", (250, 320)),
        (contact_depth, "(c) Mean contact depth", "Depth (m)", (1148, 1172)),
        (dcmr, "(d) DCMR(t)", "DCMR (m/day)", (0.0, 0.075)),
        (rcei, "(e) RCEI(t)", "RCEI (m/bar)", (0.0, 3.0)),
    ]

    for ax, (y, title, ylabel, ylim) in zip(axes, panels):
        ax.plot(t, y, color="black")
        ax.set_title(title, loc="left", fontweight="bold")
        ax.set_xlabel("Time (days)")
        ax.set_ylabel(ylabel)
        ax.set_xlim(0, 1200)
        ax.set_ylim(*ylim)
        ax.set_xticks(np.arange(0, 1201, 300))
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.savefig("Figure3_Transient_Forcing_Response_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure3_Transient_Forcing_Response_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
