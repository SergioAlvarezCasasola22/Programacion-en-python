"""Realiza la operación matemática según el operador proporcionado."""


def calcular(num1, operador, num2):
    """Realiza la operación matemática según el operador proporcionado."""
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
            return None
