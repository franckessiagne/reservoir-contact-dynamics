# Script used to generate Figure13.png
# Width: 190 mm; export: 1200 dpi

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def add_box(ax, xy, width, height, text, fontsize):
    p = FancyBboxPatch(
        xy, width, height,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=0.9,
        edgecolor="black",
        facecolor="white"
    )
    ax.add_patch(p)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        wrap=True
    )

def add_arrow(ax, start, end):
    ax.add_patch(
        FancyArrowPatch(
            start, end,
            arrowstyle="-|>",
            mutation_scale=10,
            linewidth=0.9,
            color="black",
            shrinkA=4,
            shrinkB=4
        )
    )

w = 190 / 25.4
h = w * 0.70

fig, ax = plt.subplots(figsize=(w, h), dpi=300)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Column 1
y1 = [0.80, 0.65, 0.50, 0.35, 0.20]
texts1 = [
    "Capillary pressure\nand entry barriers",
    "Capillary/permeability\nheterogeneity",
    "Stress-dependent\npermeability",
    "Transient and cyclic\nproduction forcing",
    "Relative-permeability\nhysteresis"
]
for y, t in zip(y1, texts1):
    add_box(ax, (0.03, y), 0.22, 0.095, t, 7.2)

# Column 2
y2 = [0.82, 0.69, 0.56, 0.43, 0.30, 0.17]
texts2 = [
    "Delayed mobilisation\nand threshold response",
    "Abrupt migration\nbursts",
    "Non-planar contact\nroughening",
    "Irreversible displacement\nand reservoir memory",
    "Frequency attenuation\nand phase lag",
    "Stable–transitional–\nunstable regime shift"
]
for y, t in zip(y2, texts2):
    add_box(ax, (0.30, y), 0.22, 0.085, t, 7.0)

# Column 3
y3 = [0.80, 0.65, 0.50, 0.35, 0.20]
texts3 = [
    "Saturation-threshold\ncontact extraction",
    "DCMR:\ninstantaneous mobility",
    "RCEI:\npressure sensitivity",
    "Hysteresis loop area\nand irreversibility index",
    "Gain, phase lag,\nand regime map"
]
for y, t in zip(y3, texts3):
    add_box(ax, (0.56, y), 0.18, 0.095, t, 6.9)

# Column 4 — resized/wrapped to fit text
x4 = 0.775
y4 = [0.80, 0.64, 0.48, 0.32, 0.10]
h4 = [0.115, 0.14, 0.115, 0.115, 0.19]
fs4 = [6.6, 6.2, 6.5, 6.5, 5.9]

texts4 = [
    "Improved forecasting\nof moving contacts",
    "Operational mitigation:\nBHP control and\nrate design",
    "Surveillance targeting\nand early warning",
    "Risk screening using\nmobility regimes",
    "Transferable to CO2 storage,\ngas storage, aquifers,\nand contaminant fronts"
]

for y, height, fs, t in zip(y4, h4, fs4, texts4):
    add_box(ax, (x4, y), 0.205, height, t, fs)

# Arrows: mechanisms -> behaviours
for i, j in [(0, 0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 3), (3, 5)]:
    add_arrow(ax, (0.25, y1[i] + 0.047), (0.30, y2[j] + 0.043))

# Arrows: behaviours -> diagnostics
for i, j in [(0, 0), (1, 1), (1, 2), (2, 0), (3, 3), (4, 4), (5, 4)]:
    add_arrow(ax, (0.52, y2[i] + 0.043), (0.56, y3[j] + 0.047))

# Arrows: diagnostics -> implications
for i, j in [(0, 0), (1, 3), (2, 0), (3, 2), (4, 3), (4, 4)]:
    add_arrow(ax, (0.74, y3[i] + 0.047), (x4, y4[j] + h4[j] / 2))

# Bottom synthesis statement
add_box(
    ax,
    (0.10, 0.03),
    0.80,
    0.06,
    "Fluid contacts are treated as emergent dynamic interfaces inferred from saturation fields,\n"
    "rather than fixed equilibrium boundaries.",
    6.8
)

fig.savefig(
    "Figure13.png",
    dpi=1200,
    bbox_inches="tight"
)

plt.close(fig)
