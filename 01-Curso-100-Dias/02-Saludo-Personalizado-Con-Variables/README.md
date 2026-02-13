# 🎂 Proyecto Día 2: Saludo Personalizado y Cálculo de Edad

Este proyecto marca el segundo día de mi reto de 100 días de Python. En esta etapa, me enfoqué en la interacción dinámica con el usuario y el manejo de tipos de datos.

## 🚀 Funcionalidades
* **Entrada de Datos Dinámica:** Captura nombre, año de nacimiento y color favorito del usuario.
* **Cálculo de Edad Automático:** Utiliza la librería `datetime` para obtener el año actual del sistema, asegurando que el cálculo sea siempre vigente.
* **Personalización Avanzada:** Genera un mensaje de bienvenida detallado utilizando el color favorito del usuario.
* **Confirmación de Carrera:** Un mensaje motivador final para iniciar el camino como desarrollador.

## 🛠️ Conceptos y Herramientas Aplicadas
* **Librerías del Sistema:** Uso de `from datetime import date` para trabajar con fechas reales.
* **Manejo de f-strings:** Implementación de cadenas con formato `f"{variable}"` para imprimir mensajes limpios y legibles.
* **Casting de Datos:** Conversión de la entrada de usuario (`str`) a entero (`int`) para realizar operaciones matemáticas.
* **Concatenación y Estructura:** Organización visual del output en consola mediante separadores y saltos de línea.

## 💻 Ejemplo de Ejecución
```text
¿Cuál es tu nombre? Johann
Ingresa tu año de nacimiento: 1995
¿Cuál es tu color favorito? Azul

------------------ Bienvenid@ ------------------
Hola Johann, ¡es un gusto que estés aquí!
Veo que tienes 29 años de edad.
Tu color favorito es el Azul; de hecho, el Azul es un color espectacular.
Johann, ¿estás preparado para iniciar tu carrera como Desarrollador?