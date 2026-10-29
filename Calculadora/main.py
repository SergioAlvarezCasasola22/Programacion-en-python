"""Programa principal: pide datos, realiza la operación y muestra el resultado."""


from entrada import pedir_numero, pedir_operando
from operaciones import calcular


def main():
    """Función principal que controla el flujo del programa."""
    num1 = pedir_numero("Ingrese el primer número: ")
    operador = pedir_operando()
    num2 = pedir_numero("Ingrese el segundo número: ")

    resultado = calcular(num1, operador, num2)

    if resultado is not None:
        print(f"El resultado de {num1} {operador} {num2} es: {resultado}")

if __name__ == "__main__":
    main()
