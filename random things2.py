#####################################
###########método index##############

mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a", 5, 11)
print(resultado)

mi_texto2 = "Esta es una prueba dos"
resultado2 = mi_texto2.rindex("a")
print(resultado)

#####################################
##########metodo substring###########
frase = "Esta palabra será extraída."
palabra = frase[5:12]
print(palabra)

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = letras[5:12]
print(fragmento)

letras2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento2 = letras2[:12]
print(fragmento2)

letras3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento3 = letras3[:12:3]
print(fragmento3)

######################################
############métodos string############
text = "Este es el texto de Federico"
result = text.upper() #.upper .lower también
print(result)

text2 = "Este es el texto de Federico"
result2 = text2.split("t")  # entre parentesis el separador
print(result2)

variable1 = "Aprender"
variable2 = "es pendejo"
unido = " ".join([variable1, variable2])  #los parametros se ponen como listas []
print(unido)

papa = "tengo hambre y sueño"
resultation = papa.replace("hambre", "sed").replace("sueño", "dolor de cabeza")
print(resultation)

########################################
#######propiedad de los strings#########

nombre = "Carina" #los strings son inmutables
n1 = "Kari"
n2 = "na" #son concatenables
print(n1 + n2)      #(n1 * 2) #son multiplicables
parrafo = """Juventud divino tesoro
te vas para no volver
Cuando quiero llorar, no lloro
y a veces lloro sin querer""" #son multilineales
parrafo2 = "Juventud divino tesoro \nte vas para no volver\nCuando quiero llorar, no lloro\ny a veces lloro sin querer" #son infinitos
print("juventud" in parrafo) #buscar substring result boolean || sensible a mayus
print("luna" not in parrafo2) #buscar si no hay substring result boolean
print(len(parrafo))

#########################################
################listas###################

# se escriben entre []
# pueden hacerse listas de listas
# tienen sus respectivos metodos
# no son inmutables

mi_lista = ["a","b","c"]
otra_lista = ["Hola", 55, 32.3] #soportan varios tipos de datos
extrae = otra_lista[0:2] #extraer por indice
mi_lista[0] = "alfa" # no son inmutables (ya no será a, ahora será alfa)
mi_lista.append("delta") #agregar algo a la lista original
mi_lista.pop(2) #elimina elemento por el index
print(mi_lista+otra_lista) #concatenables
print(len(otra_lista))
print(type(mi_lista))

#########################################
###########metodos listas################

metodolista1 = ["o", "g", "t", "c", "u", "l", "a"]
metodolista1.sort() #ordena elementos, por default alfabetica y/o numericamente
metodolista1.reverse() #lo mismo pero al revés
print(metodolista1) #dicho método no requiere asignación de variable y no devuelve tanda (type none), funciona como está

 ########################################
 #############Diccionarios###############
 
dic = {'c1':'valor1', 'c2':2 , 3:'tres', 'c4':'tres'} #solo los valores pueden repetirse
print(dic)

resultadodic = dic['c1']
print(resultadodic)

client = {'nombre':'Juan', 'apellido':'Fuentes', 'peso':88, 'talla':1.75}
consulta = (client['apellido'])
print(consulta)

dic2 = {'c1':55, 'c2':["manzana", "mango", 77], "edad":"22", "c3":{'s1':100, "s3":"hola"}} #acepta todo tipo de datos
print(dic2["c2"][0]) #busqueda especifica de un indice en una lista dentro de un diccionario
print(dic2["c3"]["s3"]) #busqueda especifica de un elemento en un diccionario dentro de un diccionario

dic3 = {"c1":["a", "b", "c"], "c2":["d", "e", "f"]}
print(dic3["c2"][1].upper()) #metodo aplicado

dic4 = {1:"a", 2:"b"}
print(dic4)
dic4[3] = "c" #agregar elementos al diccionario
print(dic4)
dic4[2] = "B" #sobreescribir elemento existente
print(dic4)
print(dic4.keys()) #muestra claves / elementos
print(dic4.values()) #muestra conceptos / valores
print(dic4.items()) #print mas limpio como los tuples del dic. no le veo uso simplemente podría hacerse print al diccionario per se
print(dic4)

########################################
################TUPLES##################

mi_tuple = (1,2,3,4,(5, 6))
print(mi_tuple[4][0])
print(mi_tuple[-2]) #localizable, en este caso cuenta tambien los negativos (devuelve el 3)
#print(mi_tuple[0] = 5) lanza error, los tuples no pueden ser cambiados
mi_tuple = list(mi_tuple) #casting
print(type(mi_tuple))
tuplex = (5, 5.6, "ff", [22, "hola"], {"c1":"word"}) #acepta todo tipo de dato
tuple2 = (1,2,3,4)
x,y,z,f = tuple2 #(las variables asignadas deben ser la misma cantidad de elementos en el tuple)
print(x,y,z,f)
print(x,y)
tuple3 = (1,2,3,1) #
print(len(tuple3))
print(tuple3.count(1)) # menciona las veces que existe el elemento 1
print(tuple3.index(2)) # consulta cual es el indice asignado al elemento

########################################
##################SET###################

mi_set = set(["a","b","c"]) #no estan ordenados en indices, inmutables, no pueden hacerse listas ni diccionarios dentros.
print(type(mi_set)) #son irrepetibles, 
print(len(mi_set))
print(mi_set)


mi_set2 = set(["c","d","e"])
mi_set.add("f")
mi_set3 = mi_set.union(mi_set2) #unir sets, estos pueden unirse de forma aleatoria
mi_set3.remove("a") #eliminar
mi_set3.discard("d") #descartar / no tomar en cuenta
#mi_set3.pop() #eliminar un elemento aleatorio
mi_set3.clear() #vacia el set
print(mi_set3)


otro_set = {1,2,3,3,3,3} #otra sintaxis, capaz mas comodo
print(type(otro_set)) 
print(otro_set)

#print(type(otro_set[0])) saltará error
#otro_set[0] = 5 saltará error

tuple_set = set((1,2,3,4,(1,2,3),5,5)) #si acepta tuples
print(type(tuple_set))
print(2 in tuple_set) #si 2 esta en tuple_set
print(tuple_set)

########################################
###############BOOLEANOS################

#Every true or false result is considered boolean data type

mi_bool_1 = 4 < 5 #true
mi_bool_2 = 5 < 2+2 # false
print(type(mi_bool_1))
print(mi_bool_1, mi_bool_2) #ambos en un print porque tengo flojera

var1 = True
var2 = False
print(type(var1))

detalle = bool(92==100-8)
print(detalle)

listabool = [1,2,3,4]
control1 = 5 in listabool #false
control2 = 5 not in listabool #true
print(control1)
print(control2)