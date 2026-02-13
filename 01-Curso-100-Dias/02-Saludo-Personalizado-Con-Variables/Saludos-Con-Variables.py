# Agregamos Librerias
from datetime import date 

# Programa de Saludo Personalizado

#Paso 1 : Solicitar detalle al usuario y declaracion de variables

Nombre = input ("¿Cúal es tu nombre?  ")
Nacimiento = int ( input ("Ingresa tu año de nacimiento  "))
Color = input ("¿Cúal es tu color favorito?  ")
anio_actual = date.today (). year
Edad = anio_actual - Nacimiento

#Paso 2: Generador de mensaje de saludo

print ("\n ------------------ Bienvenid@ ------------------ ")
print (f"Hola {Nombre} ¡Es un gusto que estes aqui!")
print (f"Veo que tienes {Edad} años de edad y tu color favorito" )
print (f"es el {Color}. De hecho, el {Color} es un color espectacular !!")
print (f"{Nombre} , ¿estás preparado para iniciar tu carrera como Desarrollador?")