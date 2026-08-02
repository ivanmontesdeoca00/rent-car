from Vehiculo import Vehiculo


class Camion(Vehiculo):
    modelos_catalogo = {
        "FH VOLVO": { "marca": "Volvo", "precio_diario": 150.0, "capacidad_personas": 3,
            "tipo_traccion": "6x4", "rendimiento_km": 5.5, "tipo_motor": "6.7L Turbo"
            },
        
        "Mercedes Benz Actros": {
            "marca": "Mercedes Benz", "precio_diario": 140.0, "capacidad_personas": 3,
            "tipo_traccion": "4x2", "rendimiento_km": 6.0, "tipo_motor": "7.7 L 1100HP "
        }
    }

    def __init__(self, modelo="FH VOLVO"):
        if modelo not in self.modelos_catalogo:
            modelo = list(self.modelos_catalogo.keys())[0]
        
        m = self.modelos_catalogo[modelo]

        super().__init__(m["marca"], modelo, m["precio_diario"], m["capacidad_personas"], m["tipo_traccion"], "Trabajo pesado", m["rendimiento_km"], m["tipo_motor"])

    
    def calcular_cotizacion(self,dias, **asd):
        impuesto_carga_pesada = 100.0
        tarifa_total = (self.get_precio_diario() * dias) + impuesto_carga_pesada
        detalle = print(f"Alquiler base {dias} dias: ${self.get_precio_diario() * dias:.2f} + Impuestos de carga pesada: ${impuesto_carga_pesada:.2f} ")
        return tarifa_total, detalle


