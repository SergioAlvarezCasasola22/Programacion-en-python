"""Modulo encargado de pedir datos al usuario."""


def pedir_numero(msg):
    """Te pide un número y devuelve el valor introducido."""
    # Pedir unu número
    while True:
        entrada = input(msg)
        try:
            numero = int(entrada)
            break
        except ValueError:
            print("Error: eso no es un número entero válido. Inténtalo de nuevo.")

    return numero


def pedir_operando():
    """Te pide un operador y devuelve el valor introducido."""
    while True:
        operando = input("Ingrese el operador (+, -, *, /): ")
        if operando in ["+", "-", "*", "/"]:
            return operando
        else:
            print("Error: el operador debe ser uno de los siguientes: +, -, *, /")
        
