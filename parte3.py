import csv
from clases_vehiculos import *
from funciones import *

''' Al ejecutar por primera vez este módulo, se crea el archivo .csv'''
class SistemaVehiculos:
    
    @staticmethod
    def guardar_datos_csv(vehiculos, nombre_archivo):
        try:
            with open(nombre_archivo, 'w', newline='') as archivo:
                writer = csv.writer(archivo)
                for vehiculo in vehiculos:
                    tipo = str(type(vehiculo))
                    datos = str(vehiculo.__dict__)
                    writer.writerow([tipo, datos])
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    @staticmethod
    def leer_datos_csv(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                reader = csv.reader(archivo)
                for row in reader:
                    tipo, atributos = row
                    tipo_nombre = tipo.split('.')[-1].split("'")[0]
                    print(f"Lista de Vehiculos {tipo_nombre}")
                    print(f"{atributos} \n")
                    
        except Exception as e:
            print(f"Error al leer los datos: {e}")

def ejecutar_parte3():
    """Función que envuelve el código principal de parte3.py. para ser llamada desde el menu_principal.py"""
    # Crear instancias de los vehículos
    limpiar_pantalla()
    particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    # Lista de vehículos
    vehiculos = [particular, carga, bicicleta, motocicleta]

    # Guardar datos
    SistemaVehiculos.guardar_datos_csv(vehiculos, 'vehiculos.csv')

    # Leer datos
    SistemaVehiculos.leer_datos_csv('vehiculos.csv')

if __name__ == "__main__":
    ejecutar_parte3()


#ccm