'''Este módulo contiene las clases y subclases solicitadas que se utilizarán en el proyecto'''

# Clase padre Vehiculo
class Vehiculo:
    def __init__(self, marca: str, modelo: str, numero_ruedas: int):
        self.marca: str = marca
        self.modelo: str = modelo
        self.numero_ruedas: int = numero_ruedas

    def __str__(self) -> str:
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas"


# Clase Automovil que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: float, cilindrada: int):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad: float = velocidad
        self.cilindrada: int = cilindrada

    def __str__(self) -> str:
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.numero_ruedas} ruedas, {self.velocidad:.1f} Km/h, {self.cilindrada} cc"


# Clase Particular que hereda de Automovil
class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: float, cilindrada: int, numero_puestos: int):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos: int = numero_puestos

    def __str__(self) -> str:
        return f"{super().__str__()} Puestos: {self.numero_puestos}"


# Clase Carga que hereda de Automovil
class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, numero_ruedas: int, velocidad: float, cilindrada: int, peso_carga: float):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga: float = peso_carga

    def __str__(self) -> str:
        return f"{super().__str__()} Carga: {self.peso_carga} Kg"


# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    TIPOS = ["Urbana", "Carrera", "Deportiva"] #Aquí se agrega Deportiva para que sea heredada por Motocicleta.

    def __init__(self, marca: str, modelo: str, numero_ruedas: int, tipo: str):
        super().__init__(marca, modelo, numero_ruedas)
        if tipo not in Bicicleta.TIPOS:
            raise ValueError(f"Tipo inválido. Debe ser uno de {Bicicleta.TIPOS}")
        self.tipo: str = tipo

    def __str__(self) -> str:
        return f"{super().__str__()}, Tipo: {self.tipo}"


# Clase Motocicleta que hereda de Bicicleta
class Motocicleta(Bicicleta):

    def __init__(self, marca: str, modelo: str, numero_ruedas: int, tipo: str, motor: str, cuadro: str, nro_radios: int):
        super().__init__(marca, modelo, numero_ruedas, tipo)

        self.tipo: str = tipo
        self.motor: str = motor
        self.cuadro: str = cuadro
        self.nro_radios: int = nro_radios

    def __str__(self) -> str:
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"


''' Ejemplo de uso:

# bicicleta_urbana = Bicicleta("Giant", "Escape 3", 2, "Urbana")
# bicicleta_carrera = Bicicleta("Specialized", "Tarmac SL7", 2, "Carrera")

# print(bicicleta_urbana)
# print(bicicleta_carrera)

'''

#ccm
