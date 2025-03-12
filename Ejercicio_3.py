#Construir una funcion que recita como parametro una lista de datos numericos y retome la suma de dichos datos

import random


print("--------------------------------")
print("------- SUMA LISTA DATOS -------")
print("--------------------------------")

#Definicion de la funcion 
def sumar_lista_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

#Entrada
#Creamos una lista vacia
lista = []
#Tamaño de la lista
n = int(input("Digite el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1,9)
    lista.append(num)

#procesesamiento
print("Lista: ",lista)
print("La suma es: ", sumar_lista_datos(lista))

#Salida
print("\nEso era...")