# Ejercicio 5: Invertir un arreglo
# Descripción: Escribe una función que reciba un arreglo de números 
# enteros y retorne otro arreglo con los elementos en orden inverso.
# Debe tener la función para crear el arreglo e imprimirlo.
# No se pueden usar funciones propias de listas


def menu():
    
    print("")
    print("1. Para agregar una fila a la lista")
    print("2. Invertir arreglo")
    print("3. Salir")
    

def arreglo():
    for i in range(len(MatrizA)):
        for j in range(len(MatrizA[i])):
            valor = int(input(f"Ingrese el valor en la posición {i},{j}: "))
            MatrizA[i][j] = valor
    print("")
    for i in range(len(MatrizA)):
        print(MatrizA[i])


def invertir_arreglo(arreglo):
    arreglo_invertido = []
    for i in range(len(arreglo)-1, -1, -1):
        arreglo_invertido.append(arreglo[i])
    return arreglo_invertido


try:
    opcion = 0
    while opcion!=3:
        menu()
        opcion = int(input("Ingrese la opción a realizar: "))

        match opcion:
            case 1: 
                filas = int(input("Ingrese el numero de filas: "))
                MatrizA = [[0 for _ in range(filas)] for _ in range(1)]
                arreglo()
            
            case 2:
                print("")
                for i in range(len(MatrizA)):
                    MatrizA[i] = invertir_arreglo(MatrizA[i])  
            
                for f in MatrizA:
                    print(f)
                
            case 3:
                break
except ValueError:
        print("Error al convertir")
except Exception as e:
        print("Ha ocurrido un error inesperado")
        