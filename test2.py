##ANALIZADOR DE TEXTO
################################### DEFINICIÓN DE VARIABLES
texto = input("Ingresa un texto:\n")
letras = []

texto = texto.lower()
letras.append(input("Ingresa la primera letra:\n").lower())
letras.append(input("Ingresa la segunda letra:\n").lower())
letras.append(input("Ingresa la tercera letra:\n").lower())

###################################CANTIDAD DE LETRAS
print("\n")
print("Cantidad de Letras")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces.")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces.")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces.")

####################################CANTIDAD DE PALABRAS
print("\n")
print("Cantidad de palabras")
palabras = texto.split()
print(f"Hemos encontrado '{len(palabras)}' palabras en tu texto.")

####################################LETRAS DE INICIO Y FIN
print("\n")
print("Letras de inicio y fin")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra de inicio de '{letra_inicio}' y la letra del final es '{letra_fin}' en el texto suministrado.")

################################## INVERTIDO LETRA POR LETRA
print("\n")
print("Texto al revés")
invertido = texto[::-1]
print(f"Si ordenamos la oración al revés, sería:\n {invertido}")

################################# INVERTIDO PALABRA POR PALABRA
print("\n")
print("Texto al revés palabra por palabra")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(texto_invertido)

##################################BUSCANDO UNA PALABRA
print("Buscando la palabra Python")
print("\n")
buscar_python = "python" in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto.")
