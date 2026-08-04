Rent-Car System

¡Bienvenido a **Rent-Car**! Un sistema modular y escalable desarrollado en **Python** aplicando los pilares de la Programación Orientada a Objetos (POO). Este proyecto simula una plataforma inteligente de asesoría, recomendación y cotización de alquiler de vehículos según las necesidades del usuario (capacidad de pasajeros, tipo de terreno y días de alquiler).

---

##  Características Principales

- **Arquitectura Limpia y Modular**: Las clases hijas están separadas en archivos independientes (`Vehículo` como clase base y herencias específicas para cada categoría).
- **Programación Orientada a Objetos (POO)**: Uso avanzado de herencia, polimorfismo (`calcular_cotizacion` adaptado a cada tipo de vehículo) y encapsulamiento (getters y setters para tarifas seguras).
- **Asesoría Inteligente**: Evaluación automática de la capacidad de pasajeros. Si el grupo excede la capacidad del vehículo seleccionado, el sistema sugiere automáticamente una alternativa adecuada (como un transporte de pasajeros).
- **Cálculos Dinámicos**: Tarifas especiales, descuentos por cantidad de días (en autos), seguros de tracción (en camionetas) e impuestos de carga pesada (en camiones).

---

##  Estructura del Proyecto

```text
rent-car/
│
├── Vehiculo.py        # Clase base (Padre) con atributos y métodos comunes
├── Vauto_suv.py       # Clase hija: Autos y SUVs (con descuentos por días)
├── Vcamioneta.py      # Clase hija: Camionetas 4x4 (con seguro 4x4)
├── Vcamion.py         # Clase hija: Camiones de carga (con impuestos específicos)
├── Vtransporte.py     # Clase hija: Transporte de pasajeros (Sprinter / Buses)
└── main.py            # Menú interactivo de consola y flujo de negocio

flowchart TD
    A[Inicio: menu_interactivo] --> B[Paso 1: Ingresar cantidad de pasajeros]
    B -->|Pasajeros <= 0| B1[Error: Mostrar aviso y reintentar] --> B
    B -->|Pasajeros > 0| C[Seleccionar Terreno / Opción 1 al 4]
    
    C -->|1. Ciudad| D1[Instanciar Auto]
    C -->|2. Nieve/Playa| D2[Instanciar Camioneta]
    C -->|3. Trabajo pesado| D3[Instanciar Camion]
    C -->|4. Transporte| D4[Instanciar Transporte]
    C -->|Opción inválida| C1[Reiniciar cuestionario] --> C

    D1 --> E[Ingresar días de alquiler]
    D2 --> E
    D3 --> E
    D4 --> E

    E -->|Días <= 0| E1[Error: Días inválidos] --> E
    E -->|Días > 0| F[Paso 2: Evaluación de capacidad de gente]

    F -->|Pasajeros > Capacidad del Vehículo| G[Aviso: Capacidad excedida]
    G --> H[Sugerir vehículo alternativo: Transporte]
    H --> I{¿Desea cotizar la opción amplia?}
    
    I -->|Sí| J[Actualizar vehículo a Transporte] --> K
    I -->|No| L{¿Desea hacer otra consulta?}
    L -->|Sí| A
    L -->|No| FIN[Fin del programa]

    F -->|Pasajeros <= Capacidad| K[Paso 3: Verificación exitosa]
    J --> K

    K --> M[Mostrar Ficha Técnica del Vehículo]
    M --> N[Calcular Cotización según el tipo de vehículo]
    N --> O[Mostrar Desglose Final y Total a Pagar]
    
    O --> P{¿Desea hacer otra cotización?}
    P -->|Sí| A
    P -->|No| FIN2[Gracias por preferirnos - Fin]



classDiagram
    class Vehiculo {
        +String marca
        +String modelo
        -float __precio_diario
        +int capacidad_personas
        +String tipo_traccion
        +String terreno_ideal
        +float rendimiento_km
        +String tipo_motor
        +__init__(...)
        +get_precio_diario() float
        +set_precio_diario(precio)
        +mostrar_ficha_tecnica()
        +calcular_cotizacion(dias, **asd)*
    }

    class Auto {
        +dict modelos_catalogo
        +__init__(modelo)
        +calcular_cotizacion(dias, **asd)
    }

    class Camioneta {
        +dict modelos_catalogo
        +__init__(modelo)
        +calcular_cotizacion(dias, **asd)
    }

    class Camion {
        +dict modelos_catalogo
        +__init__(modelo)
        +calcular_cotizacion(dias, **asd)
    }

    class Transporte {
        +dict modelos_catalogo
        +__init__(modelo)
        +calcular_cotizacion(dias, cantidad_pasajeros, **asd)
    }

    Vehiculo <|-- Auto : Hereda
    Vehiculo <|-- Camioneta : Hereda
    Vehiculo <|-- Camion : Hereda
    Vehiculo <|-- Transporte : Hereda
