from funciones import *
from clases_vehiculos import * 


def imprimir_vehiculos() -> None:
    try:
        # Crear las instancias de los diferentes vehículos
        limpiar_pantalla()
        print("\nImpresión de los vehículos, parte 2: \n")
        particular = Particular("Ford", "Fiesta", 4, 180.0, 500, 5)
        carga = Carga("Daft Trucks", "G 38", 10, 120.0, 1000, 20000)
        bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
        motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

        # Imprimir las instancias solicitadas
        print(particular)
        print(carga)
        print(bicicleta)
        print(motocicleta)

        # Verificar las relaciones de la instancia motocicleta
        print("\nVerificación de las instancias, parte 2: \n")
        print(f"1.- Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
        print(f"2.- Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
        print(f"3.- Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
        print(f"4.- Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, Carga)}")
        print(f"5.- Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
        print(f"6.- Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")
    except Exception as e:
        print(f"Error al procesar los vehículos: {e}")

def main():
    imprimir_vehiculos()

if __name__ == "__main__":
    main()

#ccm