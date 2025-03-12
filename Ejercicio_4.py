#Construir una funcion que reciba como parametro una lista de datos numericos y que retorne el 

import random

print("--------------------------------")
print("------- PROMEDIO LISTA DATOS -------")
print("--------------------------------")

#Definicion de la funcion
def calcular_promedio_lista(lista):
    suma = 0 
    for i in lista:
        suma = suma = i
    promedio = suma /len(lista)
    return promedio

#Entrada
# Creamos una lista vacia 
lista = []
#Tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(14,18)
    lista.append(num)

#Procesamiento
print("Lista: ",lista)
print("El promedio de la lista es: ", calcular_promedio_lista(lista))

#Salida
print("\nEso era...")