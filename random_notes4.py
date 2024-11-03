from random import *

########################################
###############METODOS##################

#TODOS LOS OBJETOS TIENEN SUS PROPIOS MÉTODOS

dic = {"clave1":100, "clave2":200, "Clave3":300}

algo = dic.popitem() #elimina y almacena como tupla aparte el ultimo item (LIFO) ##Ctrl+Click va a la descripción

print(algo) #ultimo item
print(dic) #Los primeros

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3, "naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

############################################
#################FUNCIONES##################

#Métodos, informalmente hablando, son funcionaes ya incorporadas por python.
#Funciones es, en pocas palabras, crear bloques de código que pueden ser usados luego.

#def nombre de funcion parentesis y dentro del parentesis una variable
def mi_funcion(nombre):
    #pueden hacerse comentarios simples de una linea con #, si son varias usar tres comillas simples
    """
    Esto es una función simple
    """
    print("Hola " + nombre)
    
mi_funcion("Luis") #Aca le asigno un contenido a la variable "nombre"

def saludar_persona(nombre): #El parametro entre parantesis es el que se necesita para ejecutar el código, en este caso la funcion necesita un nombre para poder ser ejecutada correctamente.
    print("Hola " + nombre)
    
saludar_persona("Fernando") #acá se coloca entre parentesis el parámetro que se necesita.
saludar_persona("Javier")

###########################################
###########FUNCIONES - RETURN##############

def sumar(num1, num2):
    return num1 + num2

sumar(10, 20) #este resultado no se imprime en pantalla con return pero sí puede ser guardado en un variable
resultado = sumar(15, 30) 

def multiplicar(n1, n2):
    total = n1 * n2
    return total #con colocar total, estoy de una vez añadiendo la variable dentro

resultado1 = multiplicar(2,2) #se puede guardar en variables
print(resultado1)

#Normalmente se usan las funciones para el manejo interna de valores

def invertir_palabra(invertido):
    inv = invertido.upper()[::-1]
    return inv
palabra = invertir_palabra("PYTHON")

##############################################
############ESCALAR COMPLEJIDAD###############

def chequear_3_cifras(numero):
    return numero in range(100,1000) #comparacion booleana

suma = 544 + 214

resultado2 = chequear_3_cifras(suma)
print(resultado2)

def chequear_4_cifras(lista):
    for n in lista:
        if n in range(1000,10000): #busca si existe UN NUMERO de 4 cifras dentro de una lista y devuelve true or false
            return True #return tambien termina con la función
    else:
        pass
    return False #se coloca al final para que diga "false" si no se cumple la función, si no se coloca esto, el primer return corta la función y arrojaría un elemento none


def chequear_5_cifras(lista2): #chequear y almacenar solo numero de 5 cifras
    lista_5_cifras = [] #lista vacia
    for n in lista2:
        if n in range(10000,100000):
            lista_5_cifras.append(n)
    else:
        pass
    return lista_5_cifras

resultado3 = chequear_4_cifras([100, 222, 4548, 2]) #true
resultado4 = chequear_4_cifras([1000, 222, 48, 2]) #false
print(resultado3, resultado4)
resultado5 = chequear_5_cifras([10000, 23322, 48, 2])
print(resultado5)

#####################################

def suma_menores(lista):
    suma = 0  # Inicializa la suma en 0
    for n in lista:
        if 0 < n < 1000:  # Verifica si n es mayor a 0 y menor a 1000
            suma += n  # Suma n a la variable suma
    return suma  # Devuelve el resultado de la suma

# Ejemplo de lista
lista_numeros = [150, 2000, 500, -10, 750, 1000]

def cantidad_pares(lista):
    contador = 0  # Inicializa el contador en 0
    for n in lista:
        if n % 2 == 0:  # Verifica si el número es par
            contador += 1  # Incrementa el contador si es par
    return contador  # Devuelve la cantidad de números pares

# Ejemplo de lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

####################################################
###########PRACTICA FUNCION#########################

#codigo normal sin funciones
precios_cafe = [("capuchino", 1.5), ("expreso", 1.2), ("moka", 1.9)]

for cafe,precio in precios_cafe:
    print(precio)
    
precios_cafe2 = [("capuchino", 1.5), ("expreso", 1.2), ("moka", 1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ""
    
    for cafe,precio in lista_precios:
        if precio > precio_mayor: #irá yendo item por item y si encuentra un numero mayor al anterior lo preescribe
            precio_mayor = precio #acá lo preescribe
            cafe_mas_caro = cafe #el str que acompaña al precio en cada tuple
        else:
            pass
    
    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe2) #defino dos variable, las que estan dentro de la funcion

print(f"el café más caro es {cafe} cuyo precio eso {precio}")

###########################################
#########INTERACCION FUNCIONES#############

#EJERCICIO


#Lista Inicial de Palitos
palitos = ["-", "--", "---", "----"]

# Mezclar Palitos
def mezclar(lista):
    shuffle(lista) #el metodo shuffle sirve para hacer lo que dice el nombre
    return lista

#Pedirle al usuario elegir 1 de los 4
def probar_suerte():
    intento = ""
    
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un número del 1 al 4: \n") #se repite el loop si el usuario mete un numero fuera del 1-4
    
    return int(intento)

#comprobar el intento 

def chequear_intento(lista, intento):
    if lista[intento -1] == "-": #esto es porque el usuario ingresará 1,2,3,4. Y cuando lo ingresa, debe tomar en cuenta tambien el primer elemento (empieza desde el index 0). Sin esto, si el usuario ingresa 1, tomara el 2.
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
        
    print(f"Te ha tocado {lista[intento -1]}")
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)

#############EJERCICIOS##################

from random import *

def lanzar_dados():
    dado_1 = randint(1,6)
    dado_2 = randint(1,6)
    return dado_1, dado_2
    
def evaluar_jugada(dado_1, dado_2):
    suma_dados = dado_1 + dado_2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    else:
        pass
    
###############EJERCICIOS###################

def reducir_lista(lista):
    lista_sin_duplicados = list(set(lista))
    lista_sin_max = lista_sin_duplicados
    lista_sin_max.remove(max(lista_sin_duplicados))
    return lista_sin_max
    
def promedio(lista_sin_max):
    suma_total = sum(lista_sin_max)
    total_elementos = len(lista_sin_max)
    return suma_total / total_elementos

lista_numeros = [1, 2, 15, 7, 2]
lista_reducida = reducir_lista(lista_numeros)
resultado_promedio = promedio(lista_reducida)

###################EJERCICIOS#####################


def lanzar_moneda():
    moneda = choice(["Cara", "Cruz"])
    return moneda
    
def probar_suerte(moneda, lista):
    if moneda == "Cara": 
        print(f"La lista se autodestruirá")
        lista.clear()
        return lista
    else:
        print(f"La lista fue salvada")
    return lista
    
lista_numeros = [1, 2, 3, 4, 5]
suerte = lanzar_moneda()
Resultado = probar_suerte(suerte, lista_numeros)

#################################################
########ARGUMENTOS INDEFINIDOS (*args)###########

#*args basicamente es utilizado para argumentos variables, no tiene limites de argumentos en las funciones

def suma0(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma0(5,6,5,8,7,9,6))

def suma09(*args):
    return sum(args) #esto es mejor

print(suma09(5,6,5,8,7,9,6))

#########################################

def suma_cuadrados(*args):
    return sum(arg**2 for arg in args)
    
print(suma_cuadrados(1,2,3))

def suma_absolutos(*args):
    return sum(abs(arg) for arg in args)


############################################
###########ARGUMENTOS **kwargs##############

def suma(**kwargs):
    print(type(kwargs))
    
suma(x=3, y=5, z=2) #cambia a diccionario

def pruebasuma(num1, num2, *args, **kwargs): #orden correcto
    
    print(f"el primera valor es {num1}")
    print(f"el segundo valor es {num2}")
    
    for arg in args:
        print(f"arg = {arg}")
    
    for clave, valor in kwargs.items(): #por cada uno de los items del diccionario
        print(f"{clave} = {valor}")
    
args = [5, 50, 100, 300]
kwargs = {"x":"uno", "y":"dos", "z":"tres"}

pruebasuma(15, 20, *args, **kwargs)

#Práctica sobre Argumentos Indefinidos (**kwargs) 1
#Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    return len(kwargs)

#Práctica sobre Argumentos Indefinidos (**kwargs) 2
#Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    return list(kwargs.values())

#otra cosa...
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for atributo, valor in kwargs.items(): #se entiendo que kwargs son "diccionarios", por lo tanto, declara "atributo" y "valor" respectivamente, 
        print(f"{atributo}: {valor}")
        
################################################
#############PROBLEMAS PRÁCTICOS################
#1
def devolver_distintos(int1, int2, int3):
    sumaaaa = sum(int1, int2, int3)
    if sumaaaa > 15:
        return max(int1, int2, int3)
    elif sumaaaa < 10:
        return min(int1, int2, int3)
    else:
        return sorted(int1, int2, int3)[1]
    
#2

def loquesea(palabra):
    letras11 = set(palabra)
    return sorted(letras11)

resultado09 = loquesea("pythonnngop")
print(resultado09)

#3 

def diosmio(*args):
    contador = 0
    # Recorremos todos los argumentos que se pasaron a la función
    for i in args:
        if contador + 1 == len(args):
            return False
        # Comprobamos si el argumento actual y el siguiente son ambos cero
        elif args[i] == 0 and args[i + 1] == 0:
            return True  # Si encontramos ceros consecutivos, devolvemos True
        else:
            contador += 1
    return False  # Si no encontramos ceros consecutivos, devolvemos False

#4

def bastaya(numero):
    primos = [2]
    iteracion = 3
    
    if numero < 2:
        return 0
    
    while iteracion <= numero:
        
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    
    print(primos)
    return len(primos)

print(bastaya(50))


#Dios aun no entiendo bien las funciones jaja
#