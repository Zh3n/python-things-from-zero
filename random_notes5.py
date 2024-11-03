import os
from pathlib import Path, PureWindowsPath
from os import system

#######################################
##########GESTION DE ARCHIVOS##########

mi_archivo = open('texto1.txt')

#print(mi_archivo) #solo mostrara detalles del archivo
#mi_archivo.read() #lee el archivo sin mostrar

print(mi_archivo.read())


mayusculas = mi_archivo.readline() #este metodo solo lee linea por linea hasta los puntos o saltos de lineas.
print(mayusculas.upper()) #se pueden usar metodos

#se puede iterar

for linea in mi_archivo:
    print("Aquí dice:" + linea)

todas = mi_archivo.readlines() #da una lista con las lineas
print(todas)

#es buena practica que al abrir un archivo, cerrarlo con:

mi_archivo.close()


##############################################################
#################CREAR Y ESCRIBIR ARCHIVOS####################

#mi_archivo2 = open("texto.txt", "r") #el segundo argumento define el modo
#leer (r) ya esta por defecto si no se coloca argumento
#escribir (w)
#escribir (a) pero luego del contenido existente a = after

mi_archivo2 = open("texto2.txt", "w") #si se pone sobre un archivo existente, lo sobreescribe por completo
mi_archivo2.write("este es el nuevo texto")
mi_archivo2.close()

mi_archivo3 = open("texto1.txt", "a") #reescribrio despues del contenido 
mi_archivo3.write("Linea 4")
mi_archivo3.write('''Esta es otra
de poder escribir
sin tener que unas la n como salto de linea
buenas tardes''')
mi_archivo3.writelines(["hola", "mundo", "aquí", "estoy"]) #meh nada practico
mi_archivo3.close()

##########################################################
###############Archivos ubicacion diferente###############

#para windows se una las barras invertidas dobles \\
#para macos se usan las normales /

ruta = os.getcwd() #get current working directory
ruta = os.chdir("/home/jin/Documents/Projects/Alternative")
#ruta = os.makedirs("/home/jin/Documents/Projects/Alternative/nombre_directorio_nuevo")
#os.rmdir("/home/jin/Documents/Projects/Alternative/nombre_directorio_nuevo") remover
mi_archivo4 = open("texto3.txt")
print(mi_archivo4.read())

mi_archivo4.close()

otro_archivo = open("/home/jin/Documents/Projects/Alternative/texto3.txt")
print(otro_archivo.read())
otro_archivo.close()

carpeta1 = Path("/home/jin/Documents/Projects/Alternative") #de esta forma puedes hacerlo en todos los os
directorio = carpeta1 / "texto3.txt" #existe

mi_archivo5 = open(directorio)
print(mi_archivo5.read())
mi_archivo5.close()

#########################################################
########################PATHLIB##########################

carpeta2 = Path("/home/jin/Documents/Projects/Alternative/texto5.txt")

ruta_windows = PureWindowsPath(carpeta2)

print(ruta_windows)

if not carpeta2.exists():
    print("Este archivo no existe")
else:
    print("Genial")

print(carpeta2.stem)

#########################################################
#########################Path############################

base = Path.home()
guia = Path(base, "Europa", "España", "Barcelona", "Sagrada_Familia.txt")
guia2 = guia.with_name("La_Pedrera.txt") #agrega algo neuvo al final
print(guia.parent.parent) #Devuelve el directorio antecesor mas inmediato, se puede repetir
print(guia)

#for txt in Path(guia).glob("**/*.txt"): aca es una iteracion global dentro de un directorio buscando todos los txt

#ruta absoluta es como lo hemos estado haciendo

##########################################################
##################Limpiar Consola#########################

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
system("clear")
print(f"Tu nombre es {nombre} y tienes {edad} años.")


########################################################
##############Archivos y funciones######################

