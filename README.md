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
