# proyecto_final_monitoreo.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AnalizadorRedElectrica:
    """Clase para el procesamiento y diagnóstico de telemetría en redes eléctricas."""
    
    def __init__(self, ruta_csv: str):
        self.ruta_csv = ruta_csv
        self.df = None

    def cargar_datos(self) -> None:
        """Carga los datos desde un CSV y calcula parámetros eléctricos."""
        self.df = pd.read_csv(self.ruta_csv)
        # Potencia aparente S (kVA)
        self.df["potencia_kva"] = (self.df["voltaje_v"] * self.df["corriente_a"]) / 1000.0

    def obtener_diagnostico(self) -> dict:
        """Calcula estadísticas clave del sistema utilizando NumPy y Pandas."""
        v_promedio = np.mean(self.df["voltaje_v"])
        v_minimo = np.min(self.df["voltaje_v"])
        p_maxima = np.max(self.df["potencia_kva"])
        
        # Filtro de sobrecorriente o bajo voltaje
        alertas = self.df[(self.df["voltaje_v"] < 220.0) | (self.df["corriente_a"] > 60.0)]
        
        return {
            "voltaje_promedio": v_promedio,
            "voltaje_minimo": v_minimo,
            "potencia_maxima_kva": p_maxima,
            "total_alertas": len(alertas)
        }

    def generar_reporte_grafico(self, nombre_salida: str = "reporte_final_red.png") -> None:
        """Genera una gráfica profesional exportable con las mediciones de la red."""
        fig, ax1 = plt.subplots(figsize=(10, 5))
        
        # Eje Y1: Voltaje
        color = 'tab:blue'
        ax1.set_xlabel('Timestamp')
        ax1.set_ylabel('Voltaje (V)', color=color)
        ax1.plot(self.df['timestamp'], self.df['voltaje_v'], color=color, marker='o', label='Voltaje (V)')
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.axhline(y=220.0, color='red', linestyle='--', label='Límite Mínimo V')
        plt.xticks(rotation=45)
        
        # Eje Y2 doble: Potencia Aparente
        ax2 = ax1.twinx()  
        color = 'tab:orange'
        ax2.set_ylabel('Potencia (kVA)', color=color)
        ax2.plot(self.df['timestamp'], self.df['potencia_kva'], color=color, marker='s', linestyle=':', label='Potencia (kVA)')
        ax2.tick_params(axis='y', labelcolor=color)
        
        plt.title("Diagnóstico Integral de Operación - Red Eléctrica")
        fig.tight_layout()
        plt.savefig(nombre_salida, dpi=300)
        print(f"✅ Gráfica del proyecto exportada como '{nombre_salida}'")
        plt.show()

# --- Ejecución Principal ---
if __name__ == "__main__":
    sistema = AnalizadorRedElectrica("mediciones.csv")
    sistema.cargar_datos()
    
    resumen = sistema.obtener_diagnostico()
    
    print("==================================================")
    print("      REPORTE DE DIAGNÓSTICO ENERGÉTICO           ")
    print("==================================================")
    print(f"Voltaje Promedio:    {resumen['voltaje_promedio']:.2f} V")
    print(f"Voltaje Mínimo:      {resumen['voltaje_minimo']:.2f} V")
    print(f"Potencia Máxima:     {resumen['potencia_maxima_kva']:.2f} kVA")
    print(f"Eventos de Alerta:   {resumen['total_alertas']} registros críticos")
    print("==================================================")
    
    sistema.generar_reporte_grafico()