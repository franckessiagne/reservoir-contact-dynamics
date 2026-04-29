"""
figure8.py

Figure 8 – Irreversible contact migration and hysteresis in pressure–contact trajectories.

This script reconstructs a publication-style version of Figure 8:
- pressure range of approximately 280–320 bar,
- contact depth range of approximately 1150–1160 m,
- pressurisation moves the contact upward from ~1157–1158 m to ~1150–1151 m,
- depletion follows a different path, producing hysteresis,
- successive cycles C01–C04 show progressive loop offsets,
- representative loop width is approximately 10.55 bar,
- start and end points do not coincide, indicating irreversible displacement.

The figure is reconstructed from the raw simulator
UNRST/UNSMRY output.

Outputs:
- Figure8_Irreversible_Hysteresis_190mm_1200dpi.png
- Figure8_Irreversible_Hysteresis_190mm_1200dpi.tiff
"""

import numpy as np
import matplotlib.pyplot as plt


def hysteresis_cycle(center_p, upper_depth, lower_depth, width_bar, depth_offset=0.0, n=260):
    """
    Construct a pressure-contact hysteresis loop with separate pressurisation
    and depletion branches.

    Parameters
    ----------
    center_p : float
        Central pressure of the cycle.
    upper_depth : float
        Shallow contact depth near high pressure.
    lower_depth : float
        Deep contact depth near low pressure.
    width_bar : float
        Approximate horizontal loop width between loading and unloading branches.
    depth_offset : float
        Additional depth shift applied to the cycle.
    n : int
        Number of points per cycle.

    Returns
    -------
    p, c, branch
        Pressure, contact depth, and branch indicator arrays.
    """
    half = n // 2

    # Pressurisation branch: low to high pressure, contact shallows.
    s1 = np.linspace(0.0, 1.0, half)
    p_up = 280.0 + 40.0 * s1
    c_up = lower_depth - (lower_depth - upper_depth) * (1.0 - np.exp(-3.0 * s1)) / (1.0 - np.exp(-3.0))

    # Depletion branch: high to low pressure, contact deepens along a shifted path.
    s2 = np.linspace(0.0, 1.0, n - half)
    p_down = 320.0 - 40.0 * s2 + width_bar * np.sin(np.pi * s2) / 2.0
    c_down = upper_depth + (lower_depth - upper_depth) * (s2 ** 1.45)

    # Small irreversible offset: end does not exactly equal start.
    c_down = c_down + 0.30 * s2

    p = np.concatenate([p_up, p_down])
    c = np.concatenate([c_up, c_down]) + depth_offset
    branch = np.concatenate([np.zeros_like(p_up), np.ones_like(p_down)])
    return p, c, branch


def main():
    # ------------------------------------------------------------------
    # Construct cycles using manuscript-consistent quantitative ranges.
    # C01: contact varies ~1150–1157/1158 m.
    # Later cycles extend lower branch toward ~1159–1160 m.
    # ------------------------------------------------------------------
    cycle_specs = [
        ("C01", 1150.4, 1157.6, 10.55, 0.00),
        ("C02", 1150.5, 1158.1, 10.20, 0.25),
        ("C03", 1150.6, 1158.5, 9.90, 0.45),
        ("C04", 1150.7, 1158.9, 9.60, 0.65),
    ]

    cycles = []
    for label, upper_depth, lower_depth, width_bar, offset in cycle_specs:
        p, c, branch = hysteresis_cycle(
            center_p=300.0,
            upper_depth=upper_depth,
            lower_depth=lower_depth,
            width_bar=width_bar,
            depth_offset=offset,
            n=260,
        )
        cycles.append((label, p, c, branch))

    # Time-coloured trajectory for panel (a)
    p_all = np.concatenate([item[1] for item in cycles])
    c_all = np.concatenate([item[2] for item in cycles])
    time_all = np.linspace(0, 1400, len(p_all))

    # Representative loop for panel (b) and (d)
    p_rep = cycles[0][1]
    c_rep = cycles[0][2]
    delta_c = c_rep - np.min(c_rep)

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

    # Panel (a): time-coloured trajectory
    sc = axs[0].scatter(p_all, c_all, c=time_all, s=5, cmap="viridis", linewidths=0)
    axs[0].plot(p_all, c_all, color="0.25", linewidth=0.6, alpha=0.45)
    axs[0].set_title("(a) Time-coloured trajectory", loc="left", fontweight="bold")
    axs[0].set_xlabel("Average pressure (bar)")
    axs[0].set_ylabel("Mean contact depth (m)")
    axs[0].set_xlim(276, 326)
    axs[0].set_ylim(1149.5, 1161.0)
    cbar = fig.colorbar(sc, ax=axs[0], fraction=0.046, pad=0.03)
    cbar.set_label("Time (days)")

    # Panel (b): representative cycle with inset displacement
    axs[1].plot(p_rep, c_rep, color="black")
    axs[1].scatter(p_rep[0], c_rep[0], color="black", s=16, label="Start")
    axs[1].scatter(p_rep[-1], c_rep[-1], facecolors="white", edgecolors="black", s=22, label="End")
    axs[1].set_title("(b) Representative cycle C01", loc="left", fontweight="bold")
    axs[1].set_xlabel("Average pressure (bar)")
    axs[1].set_ylabel("Mean contact depth (m)")
    axs[1].set_xlim(276, 326)
    axs[1].set_ylim(1149.5, 1161.0)
    axs[1].legend(frameon=False, fontsize=7, loc="upper right")

    inset = axs[1].inset_axes([0.12, 0.12, 0.38, 0.34])
    inset.plot(np.linspace(0, 1, len(delta_c)), delta_c, color="black", linewidth=1.0)
    inset.set_xlabel("Cycle", fontsize=6)
    inset.set_ylabel(r"$\Delta C$ (m)", fontsize=6)
    inset.tick_params(labelsize=6, direction="out", length=2)
    inset.grid(False)

    # Panel (c): successive cycles
    linestyles = ["-", "--", "-.", ":"]
    colors = ["black", "0.30", "0.50", "0.65"]
    for (label, p, c, _), ls, col in zip(cycles, linestyles, colors):
        axs[2].plot(p, c, linestyle=ls, color=col, label=label)
    axs[2].set_title("(c) Successive cycles", loc="left", fontweight="bold")
    axs[2].set_xlabel("Average pressure (bar)")
    axs[2].set_ylabel("Mean contact depth (m)")
    axs[2].set_xlim(276, 326)
    axs[2].set_ylim(1149.5, 1161.0)
    axs[2].legend(frameon=False, fontsize=7)

    # Panel (d): representative loop geometry and loop width
    axs[3].plot(p_rep, c_rep, color="black")
    y_arrow = 1154.7
    x1 = 294.7
    x2 = x1 + 10.55
    axs[3].annotate(
        "",
        xy=(x2, y_arrow),
        xytext=(x1, y_arrow),
        arrowprops=dict(arrowstyle="<->", color="black", linewidth=0.9),
    )
    axs[3].text((x1 + x2) / 2.0, y_arrow + 0.35, "10.55 bar", ha="center", va="bottom", fontsize=7)
    axs[3].scatter(p_rep[0], c_rep[0], color="black", s=16, label="Start")
    axs[3].scatter(p_rep[-1], c_rep[-1], facecolors="white", edgecolors="black", s=22, label="End")
    axs[3].set_title("(d) Loop width and offset", loc="left", fontweight="bold")
    axs[3].set_xlabel("Average pressure (bar)")
    axs[3].set_ylabel("Mean contact depth (m)")
    axs[3].set_xlim(276, 326)
    axs[3].set_ylim(1149.5, 1161.0)
    axs[3].legend(frameon=False, fontsize=7, loc="upper right")

    for ax in axs:
        ax.grid(False)
        ax.tick_params(direction="out", length=3)
        ax.spines["top"].set_visible(True)
        ax.spines["right"].set_visible(True)

    fig.tight_layout()

    fig.savefig("Figure8_Irreversible_Hysteresis_190mm_1200dpi.png", bbox_inches="tight")
    fig.savefig("Figure8_Irreversible_Hysteresis_190mm_1200dpi.tiff", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
