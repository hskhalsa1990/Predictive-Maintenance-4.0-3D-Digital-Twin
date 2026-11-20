# V21 — Complete 3D Engineering Atlas

## Purpose
V21 adds a dedicated 3D Engineering Atlas covering the major capabilities accumulated in the v7–v20 project. It complements the existing 2D diagnostic charts; it does not replace their numerical data or engineering interpretation.

## Included 3D diagrams (28)

### Fleet, AI and operations
1. Fleet health digital twin (temperature, vibration, health)
2. AI risk probability space
3. Maintenance priority cube
4. Sensor anomaly map
5. ML holdout decision space
6. 3D confusion matrix
7. Model explainability (permutation importance)

### Vibration and bearing diagnostics
8. Shaft geometry and orbit
9. FFT harmonic peak map
10. STFT spectrogram surface
11. Thermal hotspot field
12. Rolling-bearing 3D assembly with FTF/BSF/BPFO/BPFI labels
13. Envelope spectrum evolution
14. Rotational-order map across RPM slices
15. Signal condition-indicator trajectory (RMS, crest factor, kurtosis)
16. Spectral band energy map

### Rotor, FEM and dynamics
17. Gyroscopic Campbell branches (forward/backward)
18. Bode amplitude-phase response
19. RPM waterfall spectrum
20. FE modal shape family
21. Timoshenko shaft/bending envelope
22. Concentrated disk mass and inertia geometry
23. Linearized bearing stiffness surface
24. Cross-coupled bearing force field
25. Synchronous unbalance response
26. Rotor stability map
27. Numerical vs experimental modal comparison placeholder (experimental series remains empty until measurements are uploaded)

### Data quality and reporting
28. Sensor data quality profile across current telemetry channels

## Implementation
- New module: `src/v21_3d_atlas.py`
- New dashboard: `app/fleet_monitor_v21.py`
- New tab: `Complete 3D Engineering Atlas v21`
- New requirements file: `requirements-v21.txt`
- New tests: `tests/test_v21_3d_atlas.py`
- All charts are Plotly 3D traces (Scatter3d/Surface) with rotate, zoom and hover.

## Important engineering scope
- Most diagrams use existing synthetic telemetry and reproducible numerical models.
- The thermal field and bearing geometry are illustrative visualizations, not measured thermal maps or CAD.
- The ML model is trained on rule-generated synthetic labels; its plots do not demonstrate validated failure prediction.
- Rotordynamic plots use the included educational linear Timoshenko/gyroscopic model and supplied linearized bearing coefficients.
- Experimental modal comparison intentionally does not invent experimental values; upload measured modal results to populate the experimental series.
- No live sensor integration, certified CAD/FEA, CFD/Reynolds bearing solution, or industrial safety validation is claimed.
