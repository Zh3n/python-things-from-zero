from random import *

##################################
#########OPS COMPARADORES#########


# == compara igualdad con exactitud
mi_bool = 10 == 25 #saldrá bool falso
print(mi_bool)
mi_boolv = 10 == 10 #saldrá bool verdadero
print(mi_boolv)

bool_str = "blanco"=="negro"
print(bool_str)

bool_try = "blanco" == "Blanco".lower() #Acepta métodos
print(bool_try)

bool_types = "100" == 100
print(bool_types)

bool_types2 = 100.0 == 100
print(bool_types2)

# != dieferencia (significa "no es")

dif = 100 != 99 #saldrá true porque 100 NO ES 99
print(dif)

#se pueden usar <> y sus variantes

bool1 = 100 < 99
bool2 = 100 > 99
bool3 = 100 <= 99
bool4 = 100 >= 99

print(bool1, bool2, bool3, bool4)

###########################################
#######COMPRACION VARIAS VARIABLES#########

#Operadores lógicos
#and - or - not

booleando = 4 < 5 < 6 #estará correcto
booleando2 = 4 < 5 > 6 # no preciso
print(booleando, booleando2)

ops_logico = 4 < 5 and 5 > 6 #no se cumplen ambas, entonces dará falso
print(ops_logico)
ops_logico2 = 4 < 5 or 5 > 6 #se cumple una de las dos, entonces dará positivo
print(ops_logico2)

texto = "esta frase es breve"
texto1 = ("frase" in texto) and ("breve" in texto)
print(texto1)

negacion = not "a" == "a" #una especie de comparacion inversa igual que "!="
print(negacion)

##########################################
############control de flujo##############

#if #elif #else

if 10 > 9:
    print("Es correcto")
    
if 5 == 2:
    print("Es correcto")
else:
    print("No es correcto")
    
mascota = "perro"
if mascota == "gato": ##primero
    print("tienes un gato")
elif mascota == "perro": ##segunda
    print("tienes un perro") 
else: ##opcion final
    print("No tienes un gato")
    
habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif (not habla_ingles) and (not sabe_python):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")
    

serie = "N-01"

#if serie == "N-02":
#    print("Samsung")
#elif serie == "N-01":
#    print("Nokia")
#elif serie == "N-03":
#    print("Motorola")
#else:
#    print("No existe este producto")

match serie:
    case "N-02":
        print("Samsung")
    case "N-01":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe este producto")

cliente9 = {"nombre":"Federico", "edad": 45, "ocupacion":"instructor"}

pelicula = {"pelicula":"Matrix", "ficha_tecnica": {"protagonista":"Keany Reeves", "director":"Lana y Lilly"}}

elementos = [cliente9, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('es un cliente')
            print(nombre, edad, ocupacion)
        case {'titulo': titulo,
              'ficha_tecnica}':{'protagonista': protagonista,
                                'director': director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print('no se que es esto')

########################################
################LOOPS####################

#si quiero imprimir, por ejemplo, un "Hola" por cada elemento de una listA:

nombres66 = ["Juan", "Ana", "Carlos", "Fran"]

#diría "por cada nombre imprimir hola" lo cual se traduce como

for element in nombres66:
    print("Hola " + element)
    
#en este caso "element" es una variable interna creada y usada para referirse a dichos elementos, pero podria usar cualquier otra

lista = ["a", "b", "c", "d", "e"]

for letra in lista:
    numero_letra = lista.index(letra) + 1 #no empieza desde el index 0 sino desde 1
    print(f"Letra {numero_letra}: {letra}") #imprime el index por letra 
    
lista2 = ["Juan", "Ana", "Carlos", "Fran", "laura", "Luis"]

for nombre in lista2:
    if nombre.startswith("l"): #chequea si el elemento al que se hace referencia empieza por la letra l
        print(nombre) #si el nombre empieza por la letra l, es impresa
    else:
        print ("No es un nombre que comience con L")
        
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor) #por cada vuelta, la variable "mi_valor" va sumando cada numero. 0+1+2+3+4+5 = 15
    
Palabra = "python"

for n in Palabra: #en "Palabra" tambien pudiese escribir "python" y funciona directamente
        print(n) #por linea
        
for objeto in [[1,2,], [3,4], [5,6]]:
    print(objeto) #imprimte directamente la lista y sus elemtnos

for a,b in [[1,2,], [3,4], [5,6]]:
    print(a) #imprime el objeto a de cada elemento
    #print(b) #imprime el objeto b de cada elemento

dicccionario = {"clave1":"a", "clave2":"b", "clave3":"c"}

for n1 in dicccionario:
    print(n1) #imprime el concepto/entrada de cada elemento pero no los valores por defecto
    
for item in dicccionario.items():
    print(item) #imprime el concepto/entrada con su valor
    
for item in dicccionario.values():
    print(item) #imprime solo el valor de cada item
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero
        
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")

######################################################
#####################ZIP##############################

#Junta listas entrelazandolas, las convierte en tuples

nombre000 = ["ana", "hugo", "valeria"]
edades = [54,34,22]
ciudades = ["lima", "caracas", "madrid"]

#Debe estar casteado como lista
combinade = list(zip(nombre000, edades, ciudades))

#combinación de loop con zip
for nombre, edad, ciudad in combinade:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
    
#########################################################
################MIN - MAX###############################

#Detectan valores bajos y altos

menor = min(58,95,45,44,36) #busca el numero mas bajo
mayor = max(58,95,45,44,36) #busca el numero mas alto

lista22 = [58,41,64,99,441,15]
#print(max(lista22))
print(f"El menor es {min(lista22)} y el mayor es {max(lista22)}") #implementa print con la funcion

nombres02 = ["juan", "pablo", "carlos"] #tambien con strings pero los ordena alfabéticamente
print(min(nombres02))

nombre01 = "Carlos" #Busca primero la letras mayuscula, si esta todo en minuscula buscará el orden alfabético
print(min(nombre01))

diccionario99 = {"C1":45, "C2":11}
print(min(diccionario99)) #busca el valor mas bajo a nivel de claves
print(min(diccionario99.values())) #busca el valor mas bajo a nivel de valores

#################################################
##################RANDINT#########################

#significa RANDOM INTEGER

aleatorio = randint(1, 50) #integer random
print(aleatorio)

aleatorio2 = round(uniform(1, 5),2) #con decimales random, se usa "round" para definir cuantos decimales
print(aleatorio2)

aleatorio3 = random() #no se pone nada, busca entre 0 y 1
print(aleatorio3)

colores = ["azul", "rojo", "verde", "amarillo"]
aleatorio4 = choice(colores) #con listas
print(aleatorio4)

numerosrr = list(range(5,100,5))
shuffle(numerosrr) #combina todo de forma aleatoria de una lista LISTA
print(numerosrr)

################################################
#############COMPRENSION DE LISTAS##############

palabra22 = "python"

lista22 = []

for letra in palabra22:
    lista22.append(letra)
    
print(lista22)
############################### todo esto puede ser hecho de mejor forma

palabra23 = "python"

lista23 = [letra for letra in palabra23] #re incomodo esto

print(lista23)

listanum = [numero for numero in range(0,21,3)]
print(listanum)

esquizo = [n / 2 for n in range(0,21,2)] #esto se supone que va de 2 en 2 hasta el 20 pero lo que se verá es la división de cada numero entre 2
print(esquizo)

esquizo2 = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ] #Aca tomara en cuenta los numeros que al multiplicarlos por 2 sean mayor que 10, los otros los pondra 'no'... no tiene sentido pero es logico
print(esquizo2)

pies = [10,20,30,40,50]
metros = [round(p / 3.281 , 2) for p in pies] #uso round para fijar 2 decimales
print(metros)

