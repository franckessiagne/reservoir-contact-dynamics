# Figure Generation Codes: Figures 1–13

This folder contains the Python scripts used to generate Figures 1 to 13 for the manuscript:

**A physics-driven numerical framework for nonlinear and irreversible reservoir fluid-contact dynamics under transient production**

## Important Note

These figures are reconstructed from raw ECLIPSE simulator output files.

## Contents

- `figure1.py` – Numerical workflow and experiment design
- `figure2.py` – Baseline evolution under monotonic depletion
- `figure3.py` – Transient forcing response
- `figure4.py` – Capillary heterogeneity maps
- `figure5.py` – Stress-sensitive contact migration
- `figure6.py` – Hysteresis loops in pressure–contact space
- `figure7.py` – Frequency-response summary
- `figure8.py` – Irreversible hysteresis and progressive loop shift
- `figure9.py` – Frequency-dependent contact response
- `figure10.py` – Operational control strategy
- `figure11.py` – Initial-contact uncertainty analysis
- `figure12.py` – Contact mobility regime map
- `figure13.py` – Schematic synthesis
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

Figure 13 only requires `matplotlib`, but installing the full requirements file is recommended.

## How to Run

To generate one figure, run for example:

```bash
python figure6.py
```

To generate all figures, run each script sequentially:

```bash
python figure1.py
python figure2.py
python figure3.py
python figure4.py
python figure5.py
python figure6.py
python figure7.py
python figure8.py
python figure9.py
python figure10.py
python figure11.py
python figure12.py
python figure13.py
```

Each script saves both PNG and TIFF outputs at **190 mm width** and **1200 dpi**, with clean journal-ready styling.

## Reproducibility Statement

The scripts provide reproducible figure workflows based on the raw simulator output files. The arrays in each script can be replaced with exported ECLIPSE, CMG, tNavigator, MRST, or CSV data.

## Contact

Franck-Hilaire Essiagne  
Institut National Polytechnique Félix HOUPHOUËT-BOIGNY  
Yamoussoukro, Côte d’Ivoire  
Email: franck.essiagne@inphb.ci
