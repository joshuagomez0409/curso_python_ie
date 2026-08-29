# clase9_caida_voltaje.py
import numpy as np

def calcular_caida_voltaje(longitud_km: float, corriente_a: float, r_por_km: float = 0.15, x_por_km: float = 0.08, fp: float = 0.9) -> dict:
    """Calcula la caída de voltaje monotásica en una línea de transmisión."""
    theta = np.acos(fp)
    z_linea = complex(r_por_km * longitud_km, x_por_km * longitud_km)
    i_fasor = corriente_a * complex(np.cos(theta), -np.sin(theta))
    
    v_caida_fasor = i_fasor * z_linea
    v_caida_magnitud = np.abs(v_caida_fasor)
    
    return {
        "impedancia_linea_ohms": z_linea,
        "caida_voltaje_v": v_caida_magnitud,
        "porcentaje_caida_220v": (v_caida_magnitud / 220.0) * 100
    }

# --- Prueba del módulo ---
resultado = calcular_caida_voltaje(longitud_km=2.5, corriente_a=40.0)

print("--- ANÁLISIS DE CAÍDA DE VOLTAJE EN LÍNEA ---")
print(f"Impedancia de línea: {resultado['impedancia_linea_ohms']:.2f} Ω")
print(f"Caída de voltaje: {resultado['caida_voltaje_v']:.2f} V")
print(f"Pérdida porcentual (base 220V): {resultado['porcentaje_caida_220v']:.2f}%")