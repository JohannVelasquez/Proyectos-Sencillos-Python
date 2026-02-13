## Importacion de librerias 

from datetime import date

# Datos del usuario

print ("----- CALCULADORA DE EDAD INTELIGENTE -----")

Nombre = input("Por favor ingresa tu nombre = ")
Anio = int (input(" Ingresa tu año de nacimiento = "))
Mes = int ( input(" Ingresa tu mes de nacimiento = "))
Dia = int (input(" Ingresa tu día de nacimiento = "))
FNacimiento = date(Anio,Mes,Dia)
# Obtener fecha actual
hoy = date.today()
# Calcular edad 
Edad = hoy.year - Anio

# Ajustar edad par saber si ya cumplio años

ha_pasado_cumple = (hoy.month,hoy.day) >= (Mes,Dia)

if not ha_pasado_cumple:
    Edad -=1

# Lógica para saber si falta poco (ej: en los próximos 15 días)

PCumple = date (hoy.year, Mes,Dia)
DiasCumple = (PCumple - hoy).days

# Si el cumpleaños ya paso

if DiasCumple < 0:
    PCumple = date(hoy.year + 1, Mes, Dia )
    DiasCumple = (PCumple - hoy).days

# Resultados

print ("-" * 30) 
print (f" Tienes {Edad} años.")   

if hoy.month == Mes and hoy.day == Dia:
    print("¡FELIZ CUMPLEAÑOS! 🎂🎈")
elif 0 < DiasCumple <= 15:
    print(f"¡Atención! Tu cumple es en {DiasCumple} días. 🎁")