# Figure Generation Codes: Figures 6–17

This folder contains the Python scripts used to generate Figures 6 to 17 for the manuscript:

**A physics-driven numerical framework for nonlinear and irreversible reservoir fluid-contact dynamics under transient production**

## Important Note

These figures are reconstructed from the quantitative trends reported in the manuscript, not from raw ECLIPSE simulator output files.

## Contents

- `generate_figure6.py` – Baseline evolution under monotonic depletion
- `generate_figure7.py` – Transient forcing response
- `generate_figure8.py` – Capillary heterogeneity maps
- `generate_figure9.py` – Stress-sensitive contact migration
- `generate_figure10.py` – Hysteresis loops in pressure–contact space
- `generate_figure11.py` – Frequency-response summary
- `generate_figure12.py` – Irreversible hysteresis and progressive loop shift
- `generate_figure13.py` – Frequency-dependent contact response
- `generate_figure14.py` – Operational control strategy
- `generate_figure15.py` – Initial-contact uncertainty analysis
- `generate_figure16.py` – Contact mobility regime map
- `generate_figure17.py` – Schematic synthesis
- `requirements.txt` – Python dependencies

## Requirements

Install Python 3.9 or newer, then install the dependencies:

```bash
pip install -r requirements.txt
```

The scripts require:

```bash
numpy
matplotlib
```

Figure 17 only requires `matplotlib`, but installing the full requirements file is recommended.

## How to Run

To generate one figure, run for example:

```bash
python generate_figure6.py
```

To generate all figures, run each script sequentially:

```bash
python generate_figure6.py
python generate_figure7.py
python generate_figure8.py
python generate_figure9.py
python generate_figure10.py
python generate_figure11.py
python generate_figure12.py
python generate_figure13.py
python generate_figure14.py
python generate_figure15.py
python generate_figure16.py
python generate_figure17.py
```

Each script saves both PNG and TIFF outputs at **190 mm width** and **1200 dpi**, with clean journal-ready styling.

## Reproducibility Statement

The scripts provide reproducible figure-generation workflows for the manuscript figures based on the reported numerical trends. If raw simulator data are available, the synthetic/reconstructed arrays in each script can be replaced with exported ECLIPSE, CMG, tNavigator, MRST, or CSV data.

## Contact

Franck-Hilaire Essiagne  
Institut National Polytechnique Félix HOUPHOUËT-BOIGNY  
Yamoussoukro, Côte d’Ivoire  
Email: franck.essiagne@inphb.ci
