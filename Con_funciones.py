print("--------------------------------")
print("- BUSCAR UN NUMERO EN CONJUNTO -")
print("--------------------------------")

#Definicion de la funcion
def buscarDatosEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

#Entrada
dato = int(input("Numero a buscar: ")) #se recibe al dato del usuario

#Procesamiento
lista = [1,2,3,4,5] #Se almacena una lista de datos
if buscarDatosEnLista(dato, lista):
    print("Lo encontre")
else:
    print("No lo encontre")

#Salida
print("\nEso era...")