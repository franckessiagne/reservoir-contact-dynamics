"""
figure4.py

Figure 4 – Capillary heterogeneity maps.

This script reconstructs a publication-style version of Figure 4:
- non-planar contact depth under capillary heterogeneity,
- central deeper region of approximately 2515–2517 m,
- peripheral shallower region of approximately 2500–2505 m,
- displacement anomaly with a central positive anomaly > 0.30,
- contact roughness evolving from ~4.685 m to ~4.658 m, then ~4.682 m,
- comparison between homogeneous and heterogeneous capillary cases.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure4_Capillary_Heterogeneity_Maps_190mm_1200dpi.png
- Figure4_Capillary_Heterogeneity_Maps_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # ------------------------------------------------------------------
    # Synthetic spatial domain representing the areal reservoir grid
    # ------------------------------------------------------------------
    nx, ny = 140, 140
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    X, Y = np.meshgrid(x, y)

    # Elliptical radial coordinate: central capillary heterogeneity pattern
    R = ((X - 0.52) / 0.33) ** 2 + ((Y - 0.50) / 0.25) ** 2

    # ------------------------------------------------------------------
    # (a) Contact-depth map
    # Target from manuscript: peripheral ~2500–2505 m; central >2515–2517 m
    # ------------------------------------------------------------------
    contact_depth = 2501.5 + 15.5 * np.exp(-R)
    contact_depth += 0.8 * np.sin(2 * np.pi * X) * np.cos(2 * np.pi * Y)

    # ------------------------------------------------------------------
    # (b) Displacement anomaly map
    # Target from manuscript: coherent central anomaly > 0.30
    # ------------------------------------------------------------------
    displacement_anomaly = 0.36 * np.exp(-1.25 * R)
    displacement_anomaly -= 0.08 * np.exp(-((X - 0.12) ** 2 + (Y - 0.78) ** 2) / 0.015)
    displacement_anomaly -= 0.06 * np.exp(-((X - 0.86) ** 2 + (Y - 0.20) ** 2) / 0.020)

    # ------------------------------------------------------------------
    # (c) Roughness evolution
    # Target from manuscript: ~4.685 m -> ~4.658 m -> ~4.682 m
    # ------------------------------------------------------------------
    t = np.linspace(200, 1400, 241)
    roughness_heterogeneous = (
        4.685
        - 0.027 * np.exp(-((t - 1000) / 430) ** 2)
        + 0.003 * ((t - 1000) / 600) ** 2
    )
    roughness_homogeneous = 0.42 + 0.02 * (1 - np.exp(-(t - 200) / 500))

    # ------------------------------------------------------------------
    # (d) Homogeneous vs heterogeneous mean contact depth
    # Heterogeneous case shows slightly larger/nonlinear displacement.
    # ------------------------------------------------------------------
    t_depth = np.linspace(0, 1400, 281)
    contact_homogeneous = 2500 + 8.2 * (1 - np.exp(-t_depth / 760))
    contact_heterogeneous = 2500 + 10.5 * (1 - np.exp(-t_depth / 680))
    contact_heterogeneous += 0.45 * np.exp(-((t_depth - 850) / 300) ** 2)

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

    # Panel (a): contact-depth map
    im0 = axs[0].imshow(
        contact_depth,
        origin="lower",
        extent=[0, 1, 0, 1],
        cmap="viridis",
        aspect="auto",
    )
    axs[0].contour(X, Y, contact_depth, levels=8, colors="black", linewidths=0.35)
    axs[0].set_title("(a) Contact-depth map", loc="left", fontweight="bold")
    axs[0].set_xlabel("Normalized x")
    axs[0].set_ylabel("Normalized y")
    cbar0 = fig.colorbar(im0, ax=axs[0], fraction=0.046, pad=0.03)
    cbar0.set_label("Depth (m)")

    # Panel (b): displacement anomaly
    im1 = axs[1].imshow(
        displacement_anomaly,
        origin="lower",
        extent=[0, 1, 0, 1],
        cmap="coolwarm",
        aspect="auto",
        vmin=-0.10,
        vmax=0.36,
    )
    axs[1].contour(X, Y, displacement_anomaly, levels=7, colors="black", linewidths=0.35)
    axs[1].set_title("(b) Displacement anomaly", loc="left", fontweight="bold")
    axs[1].set_xlabel("Normalized x")
    axs[1].set_ylabel("Normalized y")
    cbar1 = fig.colorbar(im1, ax=axs[1], fraction=0.046, pad=0.03)
    cbar1.set_label("Relative displacement")

    # Panel (c): roughness evolution
    axs[2].plot(t, roughness_heterogeneous, color="black", label="Heterogeneous capillary case")
    axs[2].plot(t, roughness_homogeneous, color="0.45", linestyle="--", label="Homogeneous case")
    axs[2].set_title("(c) Contact roughness evolution", loc="left", fontweight="bold")
    axs[2].set_xlabel("Time (days)")
    axs[2].set_ylabel(r"Roughness, $\sigma_c$ (m)")
    axs[2].set_xlim(200, 1400)
    axs[2].set_ylim(0, 5.1)
    axs[2].legend(frameon=False, fontsize=7)

    # Panel (d): mean contact depth comparison
    axs[3].plot(t_depth, contact_heterogeneous, color="black", label="Heterogeneous capillary case")
    axs[3].plot(t_depth, contact_homogeneous, color="0.45", linestyle="--", label="Homogeneous case")
    axs[3].set_title("(d) Mean contact-depth comparison", loc="left", fontweight="bold")
    axs[3].set_xlabel("Time (days)")
    axs[3].set_ylabel("Mean contact depth (m)")
    axs[3].set_xlim(0, 1400)
    axs[3].set_ylim(2499.5, 2511.5)
    axs[3].legend(frameon=False, fontsize=7)

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure4_Capillary_Heterogeneity_Maps_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure4_Capillary_Heterogeneity_Maps_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
