import parte1
import parte2
import parte3
from funciones import limpiar_pantalla

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n=======================================")
    print("¡Bienvenido a nuestro portal de peajes!")
    print("=======================================")
    print("¿Qué número de opción desea realizar? Elija un número entre el 1 y el 4.\n")
    print("1.- Agregar vehículo(s) y visualizarlos por pantalla.")
    print("2.- Visualizar otros tipos de vehículos y confirmar las instancias.")
    print("3.- Revisar la información de vehículos.")
    print("4.- Salir.")

def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada por el usuario."""
    if opcion == 1:
        parte1.main()  # Ejecuta la lógica de la parte 1
    elif opcion == 2:
        parte2.main()  # Ejecuta la lógica de la parte 2
    elif opcion == 3:
        parte3.ejecutar_parte3()  # Llama a la función en parte3.py
    elif opcion == 4:
        limpiar_pantalla()
        print("\n¡Hasta pronto!\n")
    else:
        print("Opción inválida. Intente nuevamente.\n")

def main():
    """Función principal que controla el flujo del menú."""
    while True:
        try:
            mostrar_menu()
            opcion = int(input("\nIngrese su opción entre 1 y 4: "))
            if opcion == 4:
                ejecutar_opcion(opcion)
                break  # Salir del bucle al seleccionar la opción de salir
            elif opcion in [1, 2, 3]:
                ejecutar_opcion(opcion)
            else:
                print("\nDebe ingresar un número entre 1 y 4.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")

#Este ciclo va agregado en los módulos en caso que se requiera llamar externamente.
if __name__ == "__main__":
    main()

#ccm