"""
Example execution script for the KCTAN Fluid Engine.
Generates sample fluid vectors to demonstrate coordinate transformation and boundary slip.
"""

import numpy as np
from kctan_engine import run_kctan_3d_pi_fluid_engine, apply_quantum_slip_boundary

def main():
    print("=" * 60)
    print(" KCTAN FLUID ENGINE - SIMULATION DEMONSTRATION")
    print("=" * 60)

    # --- DEMONSTRATION 1: Standard Coordinate Transformation ---
    print("\n[1] Running Coordinate Transformations:")
    
    # Define a collection of varying input profiles: (u_x, u_y, u_z, pressure)
    test_profiles = [
        (3.0, 4.0, 1.5, 101325.0),   # Linear velocity profile A
        (-2.5, 6.0, 0.5, 101325.0),  # Linear velocity profile B
        (0.0, 0.0, 0.0, 101325.0),   # Zero/Static state edge case
    ]

    for i, (ux, uy, uz, p) in enumerate(test_profiles, 1):
        kx, ky, kz = run_kctan_3d_pi_fluid_engine(ux, uy, uz, p)
        magnitude = np.sqrt(ux**2 + uy**2 + uz**2)
        
        print(f"\n  Profile #{i}: Input Velocity Magnitude = {magnitude:.2f} m/s")
        print(f"    Input  Vectors -> Ux: {ux:>5.1f} | Uy: {uy:>5.1f} | Uz: {uz:>5.1f}")
        print(f"    KCTAN Outputs  -> Kx: {kx:>5.4f} | Ky: {ky:>5.4f} | Kz: {kz:>5.4f}")

    # --- DEMONSTRATION 2: Quantum Slip Boundary Condition ---
    print("\n" + "=" * 60)
    print("[2] Evaluating Boundary Layer Slip Conditions:")
    
    p_radius = 0.841e-15  # Proton radius threshold in meters
    u_initial = 10.0      # Base fluid flow speed
    
    # Test distances: one far away, one exactly at the boundary limit
    test_distances = [1.0e-12, 5.0e-16] 

    for dist in test_distances:
        u_final = apply_quantum_slip_boundary(u_initial, dist, p_radius)
        status = "CRITICAL (Slip Triggered)" if dist <= p_radius else "NORMAL (No Slip)"
        
        print(f"\n  Distance to Wall: {dist:.2e} meters [{status}]")
        print(f"    Initial Flow Velocity : {u_initial:.2f} m/s")
        print(f"    Resulting Wall Velocity: {u_final:.4f} m/s")

    print("\n" + "=" * 60)
    print(" Execution Completed Successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()
