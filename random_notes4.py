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

