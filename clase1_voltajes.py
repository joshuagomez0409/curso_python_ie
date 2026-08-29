# clase1_voltajes.py

def filtrar_sobrevoltajes(lecturas: list[float], umbral: float = 220.0) -> list[float]:
    """Recibe una lista de lecturas de voltaje y devuelve solo 
    aquellas que superan el umbral definido (por defecto 220V).
    """
    voltajes_altos = []
    
    for lectura in lecturas:
        if lectura > umbral:
            voltajes_altos.append(lectura)
            
    return voltajes_altos


# --- Prueba del script ---
mediciones_subestacion = [210.5, 225.0, 219.8, 240.1, 215.3, 228.7]

excesos = filtrar_sobrevoltajes(mediciones_subestacion)

print(f"Todas las mediciones: {mediciones_subestacion}")
print(f"Lecturas críticas (> 220V): {excesos}")