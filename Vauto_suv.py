from Vehiculo import Vehiculo


class Auto(Vehiculo): 
    ## Aca es donde hago los dos diccionarios que pide en la tarea
    modelos_catalogo = {
        "Hyundai Accent": {
            "marca": "Hyundai", "precio_diario": 60.0, "capacidad_personas": 5,
            "tipo_traccion": "Tiene 4 ruedas con wea", "rendimiento_km": 10.5, "tipo_motor": "1.6 Basico"
        },
        "Suzuki Swift 2.0 Turbo GTI": {
            "marca": "Suzuki", "precio_diario": 40.0, "capacidad_personas": 5,
            "tipo_traccion": "Hace bapbapbappp", "rendimiento_km": 7, "tipo_motor": "1.9 GTI turbo llevado 1000HP arriba"
        }
    }

        ##Aca no sabia como hacer un def init para elegir la opcion de que elija que vehiculo dentro de la flota quiere, asi que lo hice de esta manera
        ## Inicia como defecto el accent.
    def __init__(self, modelo="Hyundai Accent"):
        if modelo not in self.modelos_catalogo:
            modelo = list(self.modelos_catalogo.keys())[0]

        m = self.modelos_catalogo[modelo] ##Llamando a la hija con el "super()" asi no hay necesidad de hacerlo unico
        super().__init__(m["marca"], modelo, m["precio_diario"], m["capacidad_personas"], m["tipo_traccion"], "Ciudad", m["rendimiento_km"], m["tipo_motor"])

    def calcular_cotizacion(self, dias, **asd):
        precio_base = self.get_precio_diario() * dias
        if dias > 7:
            descuento = precio_base * 0.10
            total = precio_base - descuento
            print(f"Subtotal: $ {precio_base:.2f} -- Descuento de 10% por reservar mas de 7 dias: -${descuento:.2f}")
            return total, detalle
        print(f"Subtotal: ${precio_base:.2f} -- Sin descuento aplicable")
        return precio_base, detalle

