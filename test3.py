from random import randint

Nombre = input("¿Cuál es tu nombre?: \n")
print(f"Hola, {Nombre}. He pensado un número del 1 al 100, solo \ntienes 8 intentos para acertar.") #Input nombre
        
numero_bajo = 1 #limite inferior
numero_alto = 100 #limite superior
intentos = 0
adivina = 0

numero_rand = randint(numero_bajo, numero_alto) #Se especifica el número aleatorio entre los limites establecidos


while intentos < 8:
    adivina = int(input(f"Adivina un número entre {numero_bajo} y {numero_alto}.\n"))
    intentos += 1

    if adivina not in range(1,101):
        print(f"Tu número no se encuentra en el rango establecido.")
    elif adivina > numero_rand:
        print("Estuviste cerca, el número es menor.\n")
    elif adivina < numero_rand:
        print("Estuviste cerca, el número es mayor.\n")
    else:
        print(f"¡Adivinaste! Felicidades {Nombre}. ¡Has adivinado en {intentos} intentos!")
        break

if adivina != numero_rand:
    print(f"Los siento, se han acabado los intentos. El número secreto era {numero_rand}.")

