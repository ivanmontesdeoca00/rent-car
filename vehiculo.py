class Vehiculo:
    def __init__(self, marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_km, tipo_motor)
        self.marca = marca
        self.modelo = modelo
        self.precio_diario = precio_diario
        self.capacidad_personas = capacidad_personas
        self.tipo_traccion = tipo_traccion
        self.terreno_ideal = terreno_ideal
        self.rendimiento_km = rendimiento_km
        self.tipo_motor = tipo_motor

    
    ##Encapsulamiento: Aca voy a poner los gets y sets de las funciones que no quiero que sean publicas

    def get_precio_diario(self):
        return self.__precio_diario
    
    def set_precio_diario(self, precio)
        if precio <= 0:
            print ("Precio no puede ser menor a 0. Asignado tarifa base por defecto de $500 pesos.")
            self.__precio_diario = 500
        else:
            self.__precio_diario = float(precio)
    

    def get_capacidad_personas(self):
        return self.__capacidad_personas
    
    def get_tipo_traccion(self):
        return self.__tipo_traccion
    
    
    def get_terreno_ideal(self):
        return self.__terreno_ideal

    def get_rendimiento_km(self):
        return self.__rendimiento_km
    
    def get_tipo_motor(self):
        return self.__tipo_motor
    
    def mostrar_ficha_tecnica(self):
        print("\n" + "="* 50)
        print(" --------------------- FICHA TECNICA DEL VEHICULO")
        print("=" * 50)
        print(f"Marca y Modelo:  {self.marca} {self.modelo}")
        print(f"Motor : {self.tipo_motor}")
        print(f"Capacidad maxima de personas:  {self.capacidad_personas} pasajeros")
        print(f"Tipo de Traccion: {self.tipo_traccion} ")
        print(f"Terreno ideal: {self.terreno_ideal}")
        print(f"Rendimiento: {self.rendimiento_km} ")
        print(f"Tarifa Diaria: ${self.get_precio_diario():.2f} ")
        print("=" * 50)
    

    def calcular_cotizacion(self, dias, **asd):
        raise NotImplementedError ("Este metodo tiene que ser implementado por las clases hijas")


class Auto(Vehiculo): 
    ## Aca es donde hago los dos diccionarios que pide en la tarea
    modelo_catalogo = {
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
    def __init__(self, modelo="Hyndai Accent"):
        if modelo not in self.modelos_catalogo:
            modelo = list(self.modelos_catalogo.keys())[0]

        m = self.modelos_catalogo[modelo] ##Llamando a la hija con el "super()" asi no hay necesidad de hacerlo unico
        super().__init__(m["marca"], modelo, m["precio_diario"], m["capacidad_personas"], m["tipo_traccion"], "Ciudad", m["rendimiento_km"], m["tipo_motor"])

    def calcular_cotizacion(self, dias, **asd):
        precio_base = self.get_precio_diario() * dias
        if dias > 7:
            descuento = precio_base * 0.10
            total = precio_base - descuento
            return total, print(f"Subtotal: $ {precio_base:.2f} -- Descuento de 10% por reservar mas de 7 dias: -${descuento:.2f}")
        return precio_base, print(f"Subtotal: ${precio_base:.2f} -- Sin descuento aplicable")

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

    def calcular_cotizacion(self, dias, **asd):
        seguro_4x4_diario = 20.0
        tarifa_total = (self.get_precio_diario() + seguro_4x4_diario) * dias
        detalle = print(f"Tarifa base ${self.get_precio_diario():.2f} + Seguro 4x4 ${seguro_4x4_diario}/dia x {dias} dias")
        return tarifa_total, detalle


class Camion(Vehiculo):
    modelos_catalogo = {
        "FH VOLVO"{
            "marca": "Volvo", "precio_diario": 150.0, "capacidad_personas": 3,
            "tipo_traccion": "6x4", "rendimiento_km": 5.5, "tipo_motor": "6.7L Turbo"

        },
        "Mercedes Benz Actros"{
            "marca": "Mercedes Benz", "precio_diario": 140.0, "capacidad_personas": 3,
            "tipo_traccion": "4x2", "rendimiento_km": 6.0, "tipo_motor": "7.7 L 1100HP "
        }
    }

    def __init__(self, modelo="FH VOLVO"):
        if modelo not in self.modelos_catalogo:
            modelo = list(self.modelos_catalogo.keys())[0]
        
        m = self.modelos_catalogo[modelos]

        super().__init__(m["marca"], modelo, m["precio_diario"], m["capacidad_personas"], m["tipo_traccion"], "Trabajo pesado", m["rendimiento_km"], m["tipo_motor"])

    
    def calcular_cotizacion(self,dias, **asd):
        impuesto_carga_pesada = 100.0
        tarifa_total = (self.get_precio_diario() * dias) + impuesto_carga_pesada
        detalle = print(f"Alquiler base {dias} dias: ${self.get_precio_diario() * dias:.2f} + Impuestos de carga pesada: ${impuesto_carga_pesada:.2f} ")
        return tarifa_total, detalle