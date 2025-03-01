#Ejercicio 2: 
#Buscar el número más grande y más pequeño en un arreglo bidimensional
#Descripción: 
#Escribe una función que reciba una matriz y retorne el número más grande y el más pequeño.
#Debe tener la función para crear la matriz e imprimirlo.
#No se pueden usar funciones propias de listas.

def crear_matriz(filas, columnas):
    matriz = [[0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            while True:
                try:
                    matriz[i][j] = int(input(f"ingresa el numero para la posicion [{i+1}, {j+1}]: "))
                    break
                except ValueError:
                    print("los numeros son iguales")
                except IndexError:
                    print("matriz no encontrada")
                except Exception as e:
                    print(f"ha ocurrido un error {e}")
    return matriz

def imprimir_matriz(matriz):
    print("la matriz es:")
    for fila in matriz:
        print(*fila) 


def encontrar_menor_y_mayor(matriz):
    mayor = matriz[0][0]
    menor = matriz[0][0]

    for fila in matriz:
        for valor in fila:  
            if valor > mayor:
                mayor = valor  
            if valor < menor:
                menor = valor  
            
    return menor, mayor

filas = int(input("cuantas filas tendra la matriz: "))
columnas = int(input("cuantas columnas tendra la matriz: "))
matriz = crear_matriz(filas, columnas)
imprimir_matriz(matriz)
menor, mayor = encontrar_menor_y_mayor(matriz)
print(f"\nel numero mas pequeño es: {menor}")
print(f"el numero mas grande es: {mayor}")











                         
                        
