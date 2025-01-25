###Ejercicio 4
def Leernumero(mensaje):
    while True:
        try:
            a = int(input(mensaje))
            return a
        except ValueError:
            print("No se puede ingresar letras, intentelo de nuevo.")
        except Exception as e:
            print("Ha ocurrido un error inesperado al convertir el número.")
def CrearArreglo():
    try:
        longitud = Leernumero("Ingrese el número de elementos en el arreglo: ")
        arreglo = [0] * longitud 
        for i in range(longitud):
            arreglo[i] = Leernumero(f"Ingrese el número para la posición {i}: ")
        return arreglo
    except ValueError:
        print("No se puede ingresar letras, intentelo de nuevo.")
    except Exception as e:
        print("Ocurrió un error inesperado.")
    finally:
        print("¡Gracias por usar el sistema!")
def ImprimirArreglo(arreglo):
    if arreglo:
        print(f"Arreglo: {arreglo}")
    else:
        print("El arreglo está vacío.")
def ContarNumero(arreglo, numero):
    contador = 0
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            contador += 1
    return contador
print("Bienvenido al sistema para contar elementos en un arreglo.")
print("Ingrese una de las siguientes opciones:")
menu = {
    1: "Crear arreglo",
    2: "Imprimir arreglo",
    3: "Contar cuántas veces aparece un número",
    4: "Salir"
}
arreglo = [] 
while True:
    try:
        print("\nMenú:")
        for opcion, descripcion in menu.items():
            print(f"{opcion}. {descripcion}")
        seleccion = Leernumero("Seleccione una opción: ")
        match seleccion:
            case 1:
                arreglo = CrearArreglo()
            case 2:
                ImprimirArreglo(arreglo)
            case 3:
                numero = Leernumero("Ingrese el número para contar cuántas veces aparece: ")
                cantidad = ContarNumero(arreglo, numero)
                print(f"El número {numero} aparece {cantidad} veces en el arreglo.")
            case 4:
                print("¡Hasta luego!")
                break
    except ValueError:
        print("No es una opción válida, intentalo de nuevo.")
    except Exception:
        print("Ocurrió un fallo inesperado, intentalo de nuevo.")
