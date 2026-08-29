# clase7_pandas_analisis.py
import pandas as pd

# --- 1. Cargar datos directamente a un DataFrame ---
df = pd.read_csv("mediciones.csv")

# --- 2. Crear columnas calculadas instantáneamente ---
# Calculamos la potencia aparente (S = V * I) en kVA para cada fila
df["potencia_kva"] = (df["voltaje_v"] * df["corriente_a"]) / 1000.0

# --- 3. Filtrar eventos críticos (Bajo voltaje < 220V) ---
bajo_voltaje = df[df["voltaje_v"] < 220.0]

# --- 4. Estadísticas agrupadas por Subestación ---
resumen = df.groupby("subestacion").agg(
    voltaje_promedio=("voltaje_v", "mean"),
    potencia_maxima_kva=("potencia_kva", "max"),
    frecuencia_minima=("frecuencia_hz", "min")
)

# --- Salida de Resultados ---
print("--- DATAFRAME COMPLETO CON POTENCIA CALCULADA ---")
print(df)

print("\n--- REGISTROS CON BAJO VOLTAJE (< 220 V) ---")
print(bajo_voltaje[["timestamp", "subestacion", "voltaje_v"]])

print("\n--- RESUMEN EJECUTIVO POR SUBESTACIÓN ---")
print(resumen)