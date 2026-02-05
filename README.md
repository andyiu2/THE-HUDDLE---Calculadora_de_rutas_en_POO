<img width="300" height="499" alt="image" src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*zhGrynju2hCeoHVKwdsazg.gif" />


# 🧭 Calculadora de Rutas con Programación Orientada a Objetos

Este proyecto implementa una calculadora de rutas en un mapa utilizando el algoritmo de **Dijkstra**, aplicando conceptos de **Programación Orientada a Objetos (POO)** en Python.

El objetivo principal es refactorizar un programa originalmente procedural a una solución modular, clara y mantenible basada en clases y objetos.

---

## 🎯 Objetivos del Proyecto

- Aplicar correctamente los principios básicos de POO.
- Separar responsabilidades entre clases.
- Implementar un algoritmo de búsqueda de caminos.
- Validar entradas del usuario.
- Mantener el código legible y escalable.

---

## 🧱 Estructura del Proyecto

├── main.py - # Flujo principal del programa\
├── mapa.py - # Clase Mapa\
├── calculadora.py - # Clase CalculadoraDeRutas (Dijkstra)\
├── constantes.py - # Constantes y configuraciones\
└── README.md


---

## 🧠 Diseño Orientado a Objetos

### Clase `Mapa`
Encargada de representar el mapa y su estado.

Funciones principales:
- Crear el mapa.
- Mostrar el mapa en consola.
- Validar coordenadas.
- Determinar celdas accesibles.
- Proveer vecinos válidos para el algoritmo.
- Marcar inicio, salida y rutas.

---

### Clase `CalculadoraDeRutas`
Encargada de calcular la ruta más corta entre dos puntos.

Funciones principales:
- Implementar el algoritmo de Dijkstra.
- Calcular la ruta más corta.
- Reconstruir la ruta final.

---

### Archivo `constantes.py`
Contiene valores compartidos por todo el sistema:
- Tipos de celdas.
- Costos de movimiento.
- Símbolos visuales.

---

## 🔁 Funcionamiento General

1. El usuario ingresa el tamaño del mapa.
2. Se crea el mapa.
3. El usuario ingresa las coordenadas de inicio y salida.
4. Se calcula la ruta más corta.
5. Se agregan obstáculos.
6. Se recalcula la ruta evitando los nuevos obstáculos.

---

## 🧪 Validaciones

- Las coordenadas deben estar dentro del mapa.
- No se permite seleccionar edificios u obstáculos como inicio o salida.
- Inicio y salida no pueden coincidir.

---

## 📚 Conceptos Aplicados

- Programación Orientada a Objetos
- Encapsulamiento
- Separación de responsabilidades
- Atributos de clase y de instancia
- Algoritmo de Dijkstra

---

