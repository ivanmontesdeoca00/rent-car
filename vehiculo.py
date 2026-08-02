class Vehiculo:
    def __init__(self, marca, modelo, precio_diario, capacidad_personas, tipo_traccion, terreno_ideal, rendimiento_km, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.set_precio_diario(precio_diario)
        self.capacidad_personas = capacidad_personas
        self.tipo_traccion = tipo_traccion
        self.terreno_ideal = terreno_ideal
        self.rendimiento_km = rendimiento_km
        self.tipo_motor = tipo_motor

    
    ##Encapsulamiento: Aca voy a poner los gets y sets de las funciones que no quiero que sean publicas

    def get_precio_diario(self):
        return self.__precio_diario
    
    def set_precio_diario(self, precio):
        if precio <= 0:
            print ("Precio no puede ser menor a 0. Asignado tarifa base por defecto de $500 pesos.")
            self.__precio_diario = 500
        else:
            self.__precio_diario = float(precio)
    

    
    def mostrar_ficha_tecnica(self):
        print("\n" + "="* 50)
        print(" --------------------- FICHA TECNICA DEL VEHICULO ------------------")
        print("=" * 50)
        print(f"Marca y Modelo:  {self.marca} {self.modelo}")
        print(f"Motor : {self.tipo_motor}")
        print(f"Capacidad maxima de personas:  {self.capacidad_personas} pasajeros")
        print(f"Tipo de Traccion: {self.tipo_traccion} ")
        print(f"Terreno ideal: {self.terreno_ideal}")
        print(f"Rendimiento: {self.rendimiento_km} ")
        print(f"Tarifa Diaria: ${self.get_precio_diario():.2f} ")
        print("=" * 50)
    

    def calcular_cotizacion(self, dias, **asd): ## el **asd cumple la funcion de agregado, por ejemplo si quiero agregar pasajeros y demas
        raise NotImplementedError ("Este metodo tiene que ser implementado por las clases hijas") ## Esto aca significa que no hay una formula general, la clase hija tiene la obligacion de escribir su calculo


