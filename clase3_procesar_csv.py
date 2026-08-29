# clase3_procesar_csv.py
import csv

def cargar_mediciones(ruta_archivo: str) -> list[dict]:
    """Lee un archivo CSV con lecturas de tiempo, voltaje y corriente,
    y devuelve una lista de diccionarios con los valores convertidos a numérico.
    """
    datos = []
    
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertimos los datos de texto (string) a float
            datos.append({
                "tiempo": float(fila["tiempo_s"]),
                "voltaje": float(fila["voltaje_v"]),
                "corriente": float(fila["corriente_a"])
            })
            
    return datos


# --- Ejecución del Análisis ---
registros = cargar_mediciones("mediciones.csv")

# 1. Uso de List Comprehension para calcular Potencia Activa (P = V * I) de cada registro
potencias = [r["voltaje"] * r["corriente"] for r in registros]

# 2. Uso de List Comprehension con Filtro: filtrar solo registros de ALTA POTENCIA (> 1200 W)
potencias_criticas = [
    f"{r['tiempo']}s: {r['voltaje'] * r['corriente']:.2f}W" 
    for r in registros 
    if (r["voltaje"] * r["corriente"]) > 1200.0
]

print(f"Todas las potencias calculadas (W): {potencias}")
print("\nRegistros que superan los 1200 W:")
for item in potencias_criticas:
    print(f" - {item}")