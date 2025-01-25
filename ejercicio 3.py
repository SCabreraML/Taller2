###EJERCICIO 3
def Leernumero(mensaje):
    while True:
        try:
            a = int(input(mensaje))
            return a
        except ValueError:
            print("No se puede ingresar letras, intentelo de nuevo.")
        except Exception as e:
            print("Ha ocurrido un error inesperado al convertir el número.")
def CrearFila():
    try:
        longitud = Leernumero("Ingrese el número de elementos en la fila: ")
        fila = [0] * longitud
        for i in range(longitud):
            fila[i] = Leernumero(f"Ingrese el número para la posición {i}: ")
        return fila
    except ValueError:
        print("No se puede ingresar letras, intentelo de nuevo.")
    except Exception as e:
        print("Ocurrió un error inesperado.")
    finally:
        print("¡Gracias por usar el sistema!")

def ImprimirFila(fila):
    if fila:
        print(f"Fila: {fila}")
    else:
        print("La fila está vacía.")

def CalcularPromedio(fila):
    if fila:
        total = sum(fila)
        elementos = len(fila)
        promedio = total / elementos if elementos > 0 else 0
        promedio_redondeado = round(promedio)
        print(f"El promedio de los elementos de la fila es: {promedio_redondeado}")
    else:
        print("La fila está vacía.")

print("Bienvenido al sistema de promedio de una fila.")
print("Ingrese una de las siguientes opciones:")
menu = {
    1: "Crear fila",
    2: "Imprimir fila",
    3: "Sacar promedio",
    4: "Salir"
}
fila = [] 
while True:
    try:
        print("\nMenú:")
        for opcion, descripcion in menu.items():
            print(f"{opcion}. {descripcion}")
        
        seleccion = Leernumero("Seleccione una opción: ")

        match seleccion:
            case 1:
                fila = CrearFila()
            case 2:
                ImprimirFila(fila)
            case 3:
                CalcularPromedio(fila)
            case 4:
                print("¡Hasta luego!")
                break
    except ValueError:
        print("No es una opción válida, intentalo de nuevo.")
    except Exception:
        print("Ocurrió un fallo inesperado, intentalo de nuevo.")

