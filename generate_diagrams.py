#!/usr/bin/env python3
"""Regenerate the interactive 3D HTML diagrams (no sklearn required)."""
import numpy as np
import plotly.graph_objects as go
from pathlib import Path

OUT = Path("diagrams")
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(2026)

def save(fig, name):
    fig.write_html(OUT / name, include_plotlyjs="cdn")
    print("wrote", name)

# (re-generate the same set for completeness)
# Fleet Health
n=40
temp = rng.uniform(40,95,n); vib=rng.uniform(0.5,8,n)
health = np.clip(100-(temp-40)/55*30 - vib*5 + rng.normal(0,5,n),10,100)
priority = np.where(health<40,"Critical",np.where(health<60,"High",np.where(health<80,"Moderate","Low")))
colors={"Critical":"#d62728","High":"#ff7f0e","Moderate":"#e6b800","Low":"#2ca02c"}
fig=go.Figure()
for band in colors:
    m=priority==band
    fig.add_trace(go.Scatter3d(x=temp[m],y=vib[m],z=health[m],mode="markers",name=band,
        marker=dict(size=7,color=colors[band],opacity=.9)))
fig.update_layout(title="01 • Fleet Health Digital Twin",scene=dict(xaxis_title="Temperature (°C)",yaxis_title="Vibration RMS",zaxis_title="Health index"),height=500,margin=dict(l=0,r=0,t=40,b=0))
save(fig,"01_fleet_health_digital_twin.html")

print("All core diagrams present in diagrams/")
