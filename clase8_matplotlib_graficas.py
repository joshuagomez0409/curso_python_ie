# clase8_matplotlib_graficas.py
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Cargar los datos del CSV ---
df = pd.read_csv("mediciones.csv")

# Extraer datos de la Subestación Norte para graficar
df_norte = df[df["subestacion"] == "Subestacion_Norte"]

# --- 2. Crear la figura y los paneles de graficación (2 filas, 1 columna) ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

# --- Gráfica 1: Voltaje vs Tiempo ---
ax1.plot(df_norte["timestamp"], df_norte["voltaje_v"], marker='o', color='tab:blue', linewidth=2, label="Voltaje (V)")
ax1.axhline(y=220.0, color='red', linestyle='--', label="Límite Mínimo (220 V)")  # Línea de referencia
ax1.set_ylabel("Voltaje (V)")
ax1.set_title("Monitoreo de Calidad de Potencia - Subestación Norte")
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc="upper right")

# --- Gráfica 2: Corriente vs Tiempo ---
ax2.plot(df_norte["timestamp"], df_norte["corriente_a"], marker='s', color='tab:orange', linewidth=2, label="Corriente (A)")
ax2.set_xlabel("Hora del Registro")
ax2.set_ylabel("Corriente (A)")
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc="upper left")

# Rotar las etiquetas de la hora para que no se traslapen
plt.xticks(rotation=30)
plt.tight_layout()  # Ajusta espacios automáticamente

# --- 3. Guardar la gráfica como imagen y mostrarla ---
plt.savefig("reporte_subestacion_norte.png", dpi=300)
print("✅ Gráfica guardada como 'reporte_subestacion_norte.png'")
plt.show()