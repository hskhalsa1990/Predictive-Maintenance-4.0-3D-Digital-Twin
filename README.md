# Predictive Maintenance 4.0 — Complete 3D Engineering Atlas (v21)

**Physics-Aware Industrial Digital Twin**  
Mechanical Engineering × Vibration Diagnostics × Thermal Modeling × Machine Learning × 2D + 3D Visualization

Flat GitHub-ready project (**no sub-folders**) with **real PNG diagrams** (3D + 2D + Bar charts) and interactive HTML, all in one directory.

---

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run fleet_monitor_v21.py
```

Run tests: `python -m unittest test_v21_3d_atlas.py`  
Regenerate interactive HTML: `python generate_diagrams.py`

---

## Architecture

```mermaid
flowchart LR
    A[monitoring.py<br/>synthetic sensor batch] --> B[v8_engine / v10_enterprise<br/>health index + priority]
    B --> C[v9_intelligence / v11_validation<br/>ML risk model]
    D[signal_diagnostics / advanced_diagnostics<br/>FFT, envelope, orders] --> F
    E[v16-v20 rotor modules<br/>FEM, Campbell, bearing response] --> F
    C --> F[v21_3d_atlas.py<br/>28 3D diagrams]
    F --> G[fleet_monitor_v21.py<br/>Streamlit dashboard]
    C --> H[api.py<br/>FastAPI inference]
```

---

## 3D Diagrams

### Fleet Health Digital Twin
![Fleet Health](01_fleet_health_digital_twin.png)

### ML Decision Space
![ML Decision](05_ml_decision_space.png)

### Shaft Orbit
![Shaft Orbit](08_shaft_orbit.png)

### FFT Harmonic Map (3D)
![FFT 3D](09_fft_harmonic_map.png)

### STFT Spectrogram Surface
![STFT](10_stft_surface.png)

### Thermal Hotspot Field
![Thermal](11_thermal_hotspot.png)

### Rolling Bearing 3D Assembly
![Bearing](12_bearing_3d_assembly.png)

### Condition-Indicator Trajectory
![Trajectory](15_condition_trajectory.png)

### Spectral Band Energy
![Spectral](16_spectral_band_energy.png)

### Gyroscopic Campbell Branches
![Campbell](17_campbell_branches.png)

### Synchronous Unbalance Response
![Unbalance](25_unbalance_response.png)

### Rotor Stability Map
![Stability](26_stability_map.png)

---

## 2D Charts & Spectra

### FFT Spectrum with Harmonics
![FFT 2D](2d_fft_spectrum.png)

### Envelope Spectrum (Bearing Fault)
![Envelope](2d_envelope_spectrum.png)

### Vibration RMS Trend
![Vibration Trend](2d_vibration_trend.png)

### Temperature vs Vibration
![Temp vs Vib](2d_temp_vs_vibration.png)

### Confusion Matrix
![Confusion](2d_confusion_matrix.png)

---

## Bar Graphs

### Fleet Health Index by Machine
![Health Bar](bar_fleet_health.png)

### Feature Importance
![Feature Importance](bar_feature_importance.png)

### Predicted vs Actual RUL
![RUL](bar_rul_comparison.png)

### Maintenance Priority Distribution
![Priority](bar_priority_distribution.png)

### Capability Growth Across Versions
![Capability](bar_version_capability.png)

---

## Comparison Tables

### Version Feature Matrix

| Capability                    | v10 | v15 | v18 | v19 | v20 | **v21** |
|-------------------------------|-----|-----|-----|-----|-----|---------|
| Multi-machine synthetic data  | ✓   | ✓   | ✓   | ✓   | ✓   | ✓       |
| Health Index & Priority       | ✓   | ✓   | ✓   | ✓   | ✓   | ✓       |
| FFT / Envelope / Orders       |     | ✓   | ✓   | ✓   | ✓   | ✓       |
| FEM Rotor (Timoshenko)        |     |     | ✓   | ✓   | ✓   | ✓       |
| Campbell / Gyroscopic         |     |     |     | ✓   | ✓   | ✓       |
| User Bearing K/C Inputs       |     |     |     |     | ✓   | ✓       |
| Unbalance + Stability Maps    |     |     |     |     | ✓   | ✓       |
| **Complete 3D Atlas (28)**    |     |     |     |     |     | **✓**   |
| Interactive HTML + PNG        |     |     |     |     |     | **✓**   |

### Diagram Types Included

| Type              | Count | Examples |
|-------------------|-------|----------|
| 3D Scatter / Surface | 12  | Fleet twin, STFT, Campbell, Stability, Bearing assembly |
| 2D Spectra / Trends  | 5   | FFT, Envelope, RMS trend, Temp-Vib, Confusion matrix |
| Bar / Grouped Charts | 5   | Health by machine, Feature importance, RUL, Priority, Version capability |

### Input Modules Available

| Module                    | Description                              | How to use                  |
|---------------------------|------------------------------------------|-----------------------------|
| Bearing coefficients      | Kxx, Kxy, Kyx, Kyy, Cxx, Cyy…           | `input_demo.py` or Streamlit |
| Sensor batch generator    | Vibration, temp, RPM, load               | `generate_sensor_batch()`   |
| Rotor geometry            | Length, diameter, disk locations         | v18 / v19 modules           |
| FastAPI inference         | Real-time risk prediction                | `uvicorn api:app`   |

---

## Project Layout (flat — everything in one folder)

```
.
├── README.md
├── V21_RELEASE_NOTES.md
├── requirements.txt
├── .gitignore
├── fleet_monitor_v21.py       ← main Streamlit dashboard
├── input_demo.py              ← bearing + rotor input demo
├── generate_diagrams.py       ← regenerates HTML diagrams
├── test_v21_3d_atlas.py       ← unit tests
├── api.py                     ← FastAPI inference
├── monitoring.py, signal_diagnostics.py, advanced_diagnostics.py
├── v8_engine.py … v21_3d_atlas.py   ← analysis modules
├── 01_…, 05_…, … 26_…  (.png + .html)   ← 3D diagrams
├── 2d_….png                   ← 2D charts
└── bar_….png                  ← bar graphs
```

---

## Engineering Scope

- All data is **synthetic**.
- Thermal fields and bearing geometry are **illustrative**.
- Rotor model is educational linear Timoshenko + gyroscopic.
- Bearing coefficients are **user inputs**.
- Never use as the sole basis for real-world maintenance decisions.

**Tags:** `predictive-maintenance` `3d-visualization` `2d-charts` `rotordynamics` `bearing-diagnostics` `digital-twin` `plotly`
