# clase6_numpy_mallas.py
import numpy as np

# --- 1. Definición de las Matrices del Sistema (A * X = B) ---

# Matriz de Resistencias (Ohms)
# Fila 1: [R11, R12] -> Malla 1
# Fila 2: [R21, R22] -> Malla 2
R_matriz = np.array([
    [15.0, -5.0],
    [-5.0, 25.0]
])

# Vector de Fuentes de Voltaje (Volts)
V_vector = np.array([12.0, -6.0])

# --- 2. Resolución del Sistema Lineal ---
# np.linalg.solve resuelve el sistema A * X = B encontrando el vector X (corrientes)
corrientes_malla = np.linalg.solve(R_matriz, V_vector)

I1 = corrientes_malla[0]
I2 = corrientes_malla[1]

# --- 3. Salida de Resultados ---
print("--- Resultados del Análisis de Mallas ---")
print(f"Corriente de Malla 1 (I1): {I1:.4f} A")
print(f"Corriente de Malla 2 (I2): {I2:.4f} A")

# Corriente que pasa por la resistencia compartida (R_compartida = R12 = 5 Ohms)
I_compartida = I1 - I2
print(f"Corriente en la resistencia compartida (I1 - I2): {I_compartida:.4f} A")