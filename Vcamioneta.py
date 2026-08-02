from Vehiculo import Vehiculo


class Camioneta(Vehiculo):
    ##Mismo que clase auto, diccionario que pide
    modelos_catalogo = {"Ford Raptor":{
        "marca": "Ford", "precio_diario": 90.0, "capacidad_personas": 5,
        "tipo_traccion": "4x4", "rendimiento_km": 10.5, "tipo_motor": "V8 Turbo"
    },
    "Hummer H3":{
        "marca": "Hummer", "precio_diario": 100.0, "capacidad_personas": 5,
        "tipo_traccion": "4x4", "rendimiento_km": 11, "tipo_motor": "V8 Militar a prueba de balas"
    
    }
    }
    def __init__(self, modelo="Ford Raptor"):
        if modelo not in self.modelos_catalogo:
            modelo = list(self.modelos_catalogo.keys())[0]
        m = self.modelos_catalogo[modelo]
        super().__init__(m["marca"], modelo, m["precio_diario"], m["capacidad_personas"], m["tipo_traccion"], "Nieve o Playa", m["rendimiento_km"], m["tipo_motor"])

    def calcular_cotizacion(self, dias, **asd):
        seguro_4x4_diario = 20.0
        tarifa_total = (self.get_precio_diario() + seguro_4x4_diario) * dias
        detalle = print(f"Tarifa base ${self.get_precio_diario():.2f} + Seguro 4x4 ${seguro_4x4_diario}/dia x {dias} dias")
        return tarifa_total, detalle


