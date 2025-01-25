#Ejercicio 1: 
#Suma de los elementos de un arreglo.
#Descripción:
#Crea una función que reciba un arreglo de enteros y retorne la suma de todos sus elementos.
#Debe tener la función para crear el arreglo e imprimirlo.
#No se pueden usar funciones propias

def crear_arreglo(tamano):
    arreglo = [0] * tamano  
    for i in range(tamano):
        while True:
            try:
                arreglo[i] = int(input(f"ingresa el numero {i+1}: "))
                break
            except ValueError:
                print("ingrese un numero entero")
    return arreglo

def imprimir_arreglo(arreglo):
    print("Los elementos del arreglo son: ")
    for i in arreglo:
        print(i, end="")

def suma_elementos(arreglo):
    suma = 0
    for i in arreglo:
        suma += i 
    return suma

tamano = int(input("cuantos elementos quieres en el arreglo: "))
arreglo = crear_arreglo(tamano)
imprimir_arreglo(arreglo)
print("\nla suma de los elementos es: ", suma_elementos(arreglo))




   






