# clase4_poo_transformador.py

class Transformador:
    """Representa un transformador eléctrico monofásico en una red de distribución."""
    
    def __init__(self, identificador: str, v_primario: float, v_secundario: float, potencia_nominal_kva: float):
        # Atributos (Características del objeto)
        self.identificador = identificador
        self.v_primario = v_primario
        self.v_secundario = v_secundario
        self.potencia_nominal_kva = potencia_nominal_kva
        self.cargabilidad_actual_kva = 0.0  # Inicia sin carga
        
    @property
    def relacion_transformacion(self) -> float:
        """Calcula la relación de transformación a = V1 / V2."""
        return self.v_primario / self.v_secundario

    def registrar_carga(self, carga_kva: float) -> None:
        """Actualiza la carga actual del transformador."""
        self.cargabilidad_actual_kva = carga_kva

    def estado_operacion(self) -> str:
        """Determina si el transformador opera normal o con sobrecarga."""
        porcentaje = (self.cargabilidad_actual_kva / self.potencia_nominal_kva) * 100
        
        if porcentaje > 100.0:
            return f"⚠️ ALERTA: Sobrecargado al {porcentaje:.1f}% de su capacidad."
        else:
            return f"✅ NORMAL: Operando al {porcentaje:.1f}% de su capacidad."
        
    def calcular_corriente_secundaria_maxima(self) -> float:
        "Calculo de corriente maxima secundaria"
        return (self.potencia_nominal_kva*1000)/self.v_secundario
        

# --- Prueba de la Clase (Creación de Objetos) ---

# Instanciamos dos transformadores reales
trafo_subestacion = Transformador("TR-01", v_primario=13800.0, v_secundario=220.0, potencia_nominal_kva=75.0)
trafo_industrial = Transformador("TR-02", v_primario=13800.0, v_secundario=480.0, potencia_nominal_kva=150.0)

# Consultamos propiedades
print(f"Relación de transformación {trafo_subestacion.identificador}: {trafo_subestacion.relacion_transformacion:.2f}")

# Simulamos cargas registradas
trafo_subestacion.registrar_carga(60.0)   # 60 kVA en un trafo de 75 kVA
trafo_industrial.registrar_carga(180.0)  # 180 kVA en un trafo de 150 kVA

# Revisamos estado
print(f"{trafo_subestacion.identificador}: {trafo_subestacion.estado_operacion()}")
print(f"{trafo_industrial.identificador}: {trafo_industrial.estado_operacion()}")
i2_max = trafo_subestacion.calcular_corriente_secundaria_maxima()
print(i2_max)