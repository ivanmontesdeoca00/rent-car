from Vehiculo import Vehiculo

class Transporte(Vehiculo):
    modelos_catalogo = {
        "Mercedes Benz Sprinter" : {
            "marca": "Mercedes Benz", "precio_diario": 190.0, "capacidad_personas": 16,
            "tipo_traccion": "4x2", "rendimiento_km": 9.0, "tipo_motor": "2.0L CDI"

        },
        "Hyundai H1 BUS": {
            "marca": "Hyundai", "precio_diario": 185.0, "capacidad_personas": 19,
            "tipo_traccion": "4x3", "rendimiento_km": 11.0, "tipo_motor": "2.7L TURBO"
        }
    }

    def __init__(self,modelo="Mercedes Benz Sprinter"):
        if modelo not in self.modelos_catalogo:
            modelo = list(self.modelos_catalogo.keys())[0]
        
        m= self.modelos_catalogo[modelo]
        super().__init__(m["marca"], modelo, m["precio_diario"], m["capacidad_personas"], m["tipo_traccion"], "Traslado de gente", m["rendimiento_km"], m["tipo_motor"])

    
    def calcular_cotizacion(self,dias, cantidad_pasajeros= 1, **asd):
        tarifa_total = (self.get_precio_diario() * dias) + cantidad_pasajeros
        detalle = print(f"Alquiler base {dias} dias: $ {self.get_precio_diario() * dias:.2f} + Tasa por la cantidad de pasajeros: $ {cantidad_pasajeros}")
        return tarifa_total, detalle
        