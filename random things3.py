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