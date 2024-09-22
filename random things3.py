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
    
#########################################
################LOOPS####################

#si quiero imprimir, por ejemplo, un "Hola" por cada elemento de una listA:

nombres = ["Juan", "Ana", "Carlos", "Fran"]

#diría "por cada nombre imprimir hola" lo cual se traduce como

for element in nombres:
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