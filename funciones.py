# Función genérica para limpiar la pantalla.
import os

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola. Usa 'cls' en sistemas Windows y 'clear' en sistemas Unix.
    """
    try:
        comando = 'cls' if os.name == 'nt' else 'clear'
        os.system(comando)
    except Exception as e:
        print(f"Error al intentar limpiar la pantalla: {e}")

# Función genérica para validar entrada de datos de acuerdo al tipo de dato en el módulo parte1.py.

def validar_numerico(mensaje, tipo_dato):
    """
    Solicita al usuario una entrada numérica.
    :parametro mensaje: Mensaje a mostrar al usuario.
    :parametro tipo_dato: Tipo de dato esperado ('int' o 'float').
    :return: El número ingresado por el usuario, asegurado de ser válido.
    """
    while True:
        entrada = input(mensaje)
        try:
            if tipo_dato == 'int':
                return int(entrada)
            elif tipo_dato == 'float':
                return float(entrada)
            else:
                raise ValueError("Tipo de dato no soportado")
        except ValueError:
            input("Error en la entrada de datos. Debe ser un número válido. Presione Enter e ingrese nuevamente el dato.")

def validar_alfanumerico(mensaje):
    """
    Solicita al usuario una entrada que debe contener solo letras y números.
    :parametro mensaje: Mensaje a mostrar al usuario.
    :return: La entrada del usuario, asegurada de ser válida.
    """
    while True:
        entrada = input(mensaje)
        if entrada.strip().isalnum():
            return entrada
        else:
            input("Error en la entrada de datos. Debe contener solo letras y números. Presione Enter e ingrese nuevamente la información.\n")


#ccm