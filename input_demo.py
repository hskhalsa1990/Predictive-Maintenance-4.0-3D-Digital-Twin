#!/usr/bin/env python3
"""Simple CLI / interactive input module demo for bearing coefficients & rotor params."""
from __future__ import annotations
import numpy as np

def get_bearing_inputs():
    print("=== Bearing Linearized Coefficients Input Module ===")
    print("Enter values (or press Enter for defaults)")
    def ask(name, default):
        v = input(f"{name} [{default}]: ").strip()
        return float(v) if v else default
    Kxx = ask("Kxx (N/m)", 1.2e8)
    Kyy = ask("Kyy (N/m)", 1.0e8)
    Kxy = ask("Kxy (N/m)", 2.0e6)
    Kyx = ask("Kyx (N/m)", -1.5e6)
    Cxx = ask("Cxx (N·s/m)", 5e4)
    Cyy = ask("Cyy (N·s/m)", 4.5e4)
    return dict(Kxx=Kxx, Kyy=Kyy, Kxy=Kxy, Kyx=Kyx, Cxx=Cxx, Cyy=Cyy)

def get_rotor_inputs():
    print("\n=== Rotor Geometry Input ===")
    L = float(input("Shaft length L (m) [0.8]: ") or 0.8)
    D = float(input("Shaft diameter (m) [0.05]: ") or 0.05)
    return dict(L=L, D=D)

if __name__ == "__main__":
    b = get_bearing_inputs()
    r = get_rotor_inputs()
    print("\nReceived inputs:")
    print("Bearing:", b)
    print("Rotor:", r)
    print("These can be passed to modules.v20_bearing_response / v19_advanced_rotor")
