from vehiculo import *

def menu_interactivo():
    print("=" *60)
    print("Sistema de recomendacion y cotizacion de vehiculos")
    print("=" *60)

    while True:
        print("---- PASO 1: ASESORIA ---")

        try:
            pasajeros = int(input("Cuantas personas van a viajar?: "))
            if pasajeros <= 0:
                print("Elegi un numero valido mayor a 0")
                continue
        except ValueError:
            print ("Entrada invalida, ingresa numeros.")
            continue

        print(" Que tipo de Terreno va a transitar?")
        print("1) Ciudad (Auto-Suv)")
        print("2) Nieve o Playa (Camioneta 4x4)")
        print("3) Trabajo pesado (Camion)")
        print("4) Traslado de gente (Transporte)")

        terreno_opcion = input("Elija una opcion 1 a 4: ").strip()

        if terreno_opcion == "1":
            vehiculo = Auto("Hyundai Accent")
        elif terreno_opcion == "2":
            vehiculo = Camioneta("Ford Raptor")
        elif terreno_opcion == "3":
            vehiculo = Camion("FH VOLVO")
        
        elif terreno_opcion == "4":
            vehiculo = Transporte("Mercedes Benz Sprinter")
        else:
            print("Opcion no valida, reiniciando cuestionario")
            continue

        try:
            dias = int(input("Cuantos dias va a desear alquilar?"))
            if dias <= 0:
                print("El numero debe ser mayor a 0")
                continue
        except ValueError:
            print("Entrada invalida, ingrese un numero")
            continue


            print("--- PASO 2: Evaluacion de capacidad de gente ---")
            if pasajeros > vehiculo.get_capacidad_personas():
                print (f"El vehiculo elegido {vehiculo.marca} {vehiculo.modelo} esta en su capacidad maxima de pasajeros.")
                print ("El vehiculo elegido no tiene capacidad suficiente para tus acompañantes")

                vehiculo_sugerido = Transporte("Mercedes Benz Sprinter")
                print(f"Vehiculo alternativo sugerido: {vehiculo_sugerido.marca} {vehiculo_sugerido.modelo} Capacidad: {vehiculo_sugerido.get_capacidad_personas()} de pasajeros")


                respuesta = input("Desea cotizar  la opcion mas amplia? SI-NO : ").strip().lower()
                if respuesta in ["si", "Si", "s", "Yes", "yes", "Y"]:
                    vehiculo = vehiculo_sugerido
                    print("Perfecto, generando cotizacion con vehiculo sugferido")
                
                else:
                    print("Operacion cancelada")
                    continuar = input ("Desea hacer otra consulta? SI-NO : ").strip().lower()
                    if continuar not in ["si", "sí", "s", "yes", "y"]:
                        print("Gracias por usar el sistema, nos vemos")
                        break
                    continue
            else:
                print("Verificacion exitosa, el vehiculo cumple con las condiciones.")


            print("--- PASO 3: Ficha tecnica y cotizacion ----")

            vehiculo.mostrar_ficha_tecnica()

            total, detalle = vehiculo.calcular_cotizacion(dias, cantidad_pasajeros=pasajeros)

            print("=" *50)

            print(" COTIZACION FINAL: DESGLOSE")
            print("=" * 50)
            print(f"Dias de alquiler : {dias}")

            ##Esto es una funcion de py que sirve para verificar si el objeto almacenado en la variable hija pertenece a su clase padre
            if isinstance(vehiculo, Transporte):
                print(f"Pasajeros base: {pasajeros}")    
            
            print (f"Detalle del calculo: {detalle}")
            print(f"TOTAL A PAGAR: $ {total:.2f}") ##EL 2F Significa que aca va a haber un resultado con 2 decimales y los tiene que tener en consideracion para que no se rompa el calculo
            print("=" *50)


            otra_opcion = input("Desea hacer otra cotizacion? SI-NO: ").strip().lower()
            if otra_opcion not in ["si", "sí", "s", "yes", "y"]:
                print("gracias por preferir nuestra empresa, buen viaje")
                break




if __name__ == "__main__":
    menu_interactivo()