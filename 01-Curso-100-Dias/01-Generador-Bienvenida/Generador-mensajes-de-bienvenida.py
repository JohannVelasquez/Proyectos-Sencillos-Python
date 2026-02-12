# =========================================================
# PROYECTO DÍA 1: Generador de Bienvenida Personalizado
# Autor: Johann Velasquez
# Descripción: Captura datos básicos y muestra un mensaje
#              motivacional para nuevos programadores.
# =========================================================

# --- SECCIÓN: CAPTURA DE DATOS ---
# Solicitamos información al usuario mediante la consola

NombreUsuario = input ("¿Cúal es tu nombre? ")
Edad = input ("¿Cúal es tu edad? ")
Nacionalidad = input ("¿De que país eres? ")

# --- SECCIÓN: PRESENTACIÓN DE DATOS ---

print ("")
print ("      ----- Mensaje de Bienvenida-----    ")
print ("")
print ("      DATOS PERSONALES ")
print ("")
print ("Nombre = ", NombreUsuario )
print ("Edad = ", Edad )
print ("País = ", Nacionalidad )
print ("")
print ("-----------------------------------------------------------------------------")

# --- SECCIÓN: MENSAJE FINAL MOTIVACIONAL ---
# Usamos la coma en print para concatenar el nombre y el emoji de saludo

print ( "Hola,! ", NombreUsuario ,"\U0001F44B")
print (" Bienvenido a la programacion en Python ")
print (" Espero este nuevo camino que inicias este cargado de mucho conocimiento,")
print (" de buenas practicas y cada proyecto que realices sea con amor y dedicación,")
print (" recuerda que ahora estas un paso mas cerca a ser un gran Desarrollador.")



