# Ejercicio 6: Encontrar números pares en un arreglo
# Descripción: Escribe las siguientes funciones
#  - función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números pares.
#  - función que reciba un arreglo de números enteros y retorne un nuevo arreglo con solo los números impares.
# Debe tener la función para crear el arreglo e imprimirlo.
# No se pueden usar funciones propias de listas

def obtener_pares(arreglo):
    arreglo_pares = []
    for numero in arreglo:
        if numero % 2 == 0:  
            arreglo_pares.append(numero)
    return arreglo_pares

def obtener_impares(arreglo):
    arreglo_impares = []
    for numero in arreglo:
        if numero % 2 != 0:  
            arreglo_impares.append(numero)
    return arreglo_impares

def mostrar_arreglo(arreglo):
    print("Arreglo:", arreglo)

def agregar_fila():
    fila = []
    num_elementos = int(input("Ingrese el número de elementos en la fila: "))
    for i in range(num_elementos):
        valor = int(input(f"Ingrese el valor en la posición {i}: "))
        fila.append(valor)
    return fila

def menu():
    print("")
    print("1. Para agregar una fila a la lista")
    print("2. Filtrar números pares")
    print("3. Filtrar números impares")
    print("4. Salir")
    return int(input("Ingrese la opción a realizar: "))

def salida():
    try:
        arreglo = []  
        
        opcion = 0
        while opcion != 4:
            opcion = menu()  
            match opcion:
                case 1:
                    fila = agregar_fila()  
                    arreglo.extend(fila)  
                    mostrar_arreglo(arreglo)  
                case 2:
                    pares = obtener_pares(arreglo) 
                    print("Números pares:", pares)
                case 3:
                    impares = obtener_impares(arreglo)  
                    print("Números impares:", impares)
                case 4:
                    print("¡Adiós!")
                    break
    except ValueError:
        print("Error")
    except Exception as e:
        print("Ha ocurrido un error")

salida()

        