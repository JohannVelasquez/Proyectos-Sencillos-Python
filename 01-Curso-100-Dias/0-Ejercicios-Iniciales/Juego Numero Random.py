import random
Numero_secreto = random.randint (1,10)
Intentos = 3

print (" Estoy pensabndo en un número de 1 a 10 ¿Puedes adivinarlo?")

while Intentos >0:
  suposicion = int (input (" Ingresa tu suposicion: "))
  if suposicion == Numero_secreto: 
    print ("Felicidades, acertaste el número")
    break
  elif suposicion < Numero_secreto:
    print (" Erroneo, el número es mayor")
  else:
    print("Erroneo, el número es menor")
  Intentos -= 1
if Intentos == 0:
  print ("Lo siento, has agotado tus intentos. El número secreto era:", Numero_secreto)