# clase5_numpy_fasores.py
import numpy as np

# --- 1. Parámetros del Circuito ---
frecuencia = 60.0  # Hz
omega = 2 * np.pi * frecuencia  # Velocidad angular w = 2*pi*f

R = 10.0      # Resistencia en Ohms
L = 0.05      # Inductancia en Henrios (50 mH)
C = 0.0001    # Capacitancia en Faradios (100 uF)

# Voltaje de la fuente: 120 V con ángulo de 0 grados (Fasor V = 120 + 0j)
V_fuente = 120.0 + 0j

# --- 2. Cálculo de Reactancias e Impedancias ---
X_L = omega * L               # Reactancia inductiva
X_C = 1 / (omega * C)         # Reactancia capacitiva

# Impedancia compleja Z = R + j(X_L - X_C)
Z_total = R + 1j * (X_L - X_C)

# --- 3. Ley de Ohm Fasorial (I = V / Z) ---
I_fasor = V_fuente / Z_total

# Convertir la corriente de rectangular a polar (Magnitud y Ángulo)
I_magnitud = np.abs(I_fasor)                  # Magnitud en Amperios
I_angulo_rad = np.angle(I_fasor)              # Ángulo en radianes
I_angulo_deg = np.rad2deg(I_angulo_rad)       # Convertir radianes a grados

# --- 4. Caídas de Voltaje en cada componente ---
V_R = I_fasor * R
V_L = I_fasor * (1j * X_L)
V_C = I_fasor * (-1j * X_C)

# --- Impresión de Resultados ---
print(f"Impedancia Total Z: {Z_total:.2f} Ω")
print(f"Corriente Fasorial I: {I_magnitud:.2f} A ∠ {I_angulo_deg:.2f}°")
print(f"Voltaje en R: {np.abs(V_R):.2f} V")
print(f"Voltaje en L: {np.abs(V_L):.2f} V")
print(f"Voltaje en C: {np.abs(V_C):.2f} V")