from funciones import *
from clases_vehiculos import * 

limpiar_pantalla()

class Automovil:
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return (f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc.")

def main():
    try:
        num_vehiculos = validar_numerico("¿Cuántos vehículos desea insertar?: ", 'int')
        if num_vehiculos <= 0:
            print("El número de vehículos debe ser positivo.")
            return

        vehiculos = []

        for i in range(num_vehiculos):
            #limpiar_pantalla()  # Limpia la pantalla antes de cada entrada
            print(f"\nDatos del automóvil número {i + 1}\n")
            marca = validar_alfanumerico("1.- Inserte la marca del automóvil: ")
            modelo = validar_alfanumerico("2.- Inserte el modelo: ")
            numero_ruedas = validar_numerico("3.- Inserte el número de ruedas: ", 'int')
            velocidad = validar_numerico("4.- Inserte la velocidad en km/h: ", 'float')
            cilindrada = validar_numerico("5.- Inserte el cilindraje en cc: ", 'int')

            automovil = Automovil(marca, modelo, numero_ruedas, velocidad, cilindrada)
            vehiculos.append(automovil)

        #limpiar_pantalla()  # Limpia la pantalla antes de mostrar los resultados
        print("\nImprimiendo por pantalla los Vehículos:\n")
        for index, vehiculo in enumerate(vehiculos, start=1):
            print(f"Datos del automóvil {index} :")
            print(vehiculo)

    except ValueError as e:
        print(f"Error en la entrada de datos: {e}")

if __name__ == "__main__":
    main()
