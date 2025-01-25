###Ejercicio 3:
def Leernumero(mensaje):
    while True:
        try:
            a = int(input(mensaje))
            return a
        except ValueError:
            print("No se puede ingresar letras, intentelo de nuevo.")
        except Exception as e:
            print("Ha ocurrido un error inesperado al convertir el número.")         
def iniciarMatriz(columnas, filas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]
def CrearMatriz():
    try:
        filas = Leernumero("Ingrese el número de filas: ")
        columnas = Leernumero("Ingrese el número de columnas: ")
        matriz = iniciarMatriz(columnas, filas)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = Leernumero(f"Ingrese el número para la posición {i},{j}: ")
        return matriz
    except ValueError:
        print("No se puede ingresar letras, intentelo de nuevo.")
    except IndexError:
        print("Error al recorrer matriz.")
    except Exception as e:
        print("Ocurrió un error inesperado.")
    finally:
        print("¡Gracias por usar el sistema!")
def ImprimirMatriz(matriz):
    if matriz:
        for fila in matriz:
            print(fila)
    else:
        print("La matriz está vacía.")
def CalcularPromedio(matriz):
    if matriz:
        total = 0
        elementos = 0
        for fila in matriz:
            for valor in fila:
                total += valor
                elementos += 1
        promedio = total / elementos if elementos > 0 else 0
        promedio_redondeado = round(promedio)
        print(f"El promedio de los elementos de la matriz es: {promedio_redondeado}")
    else:
        print("La matriz está vacía.")
print("Bienvenido a su mecanismo de promedio")
print("Ingrese una de las siguientes opciones:")
menu = {
    1: "Crear matriz",
    2: "Imprimir matriz",
    3: "Sacar promedio",
    4: "Salir"
}
matriz = [] 
while True:
    try:
        print("\nMenú:")
        for opcion, descripcion in menu.items():
            print(f"{opcion}. {descripcion}")
        
        seleccion = Leernumero("Seleccione una opción: ")

        match seleccion:
            case 1:
                matriz = CrearMatriz()
            case 2:
                ImprimirMatriz(matriz)
            case 3:
                CalcularPromedio(matriz)
            case 4:
                print("¡Hasta luego!")
                break
    except ValueError:
        print("no es una opcion valida, intetelo denuevo.")
    except Exception:
        print("ocurrio un fallo inesperado, intentalo denuevo.")

