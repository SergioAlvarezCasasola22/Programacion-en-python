def introducir_datos():
    """Te pide dos números y un operador, y devuelve los valores introducidos."""
    # Pedir primer número
    while True:
        entrada = input("Introduce el primer número entero: ")
        try:
            numero_uno = int(entrada)
            break
        except ValueError:
            print("Error: eso no es un número entero válido. Inténtalo de nuevo.")

    # Pedir operador
    while True:
        operando = input("Ingrese el operador (+, -, *, /): ")
        if operando in ["+", "-", "*", "/"]:
            break
        else:
            print("Error: el operador debe ser uno de los siguientes: +, -, *, /")

    # Pedir segundo número
    while True:
        entrada = input("Introduce el segundo número entero: ")
        try:
            numero_dos = int(entrada)
            break
        except ValueError:
            print("Error: eso no es un número entero válido. Inténtalo de nuevo.")

    return numero_uno, operando, numero_dos


def calcular():
    """Función principal que realiza la operación matemática."""
    while True:
        numero_uno, operando, numero_dos = introducir_datos()

        error = False

        if operando == "+":
            resultado = numero_uno + numero_dos
        elif operando == "-":
            resultado = numero_uno - numero_dos
        elif operando == "*":
            resultado = numero_uno * numero_dos
        elif operando == "/":
            try:
                resultado = numero_uno / numero_dos
            except ZeroDivisionError:
                print("Error: No se puede dividir entre cero.")
                error = True

        if not error:
            print(f"El resultado de {numero_uno} {operando} {numero_dos} es: {resultado}")
            return resultado


def main():
    """Función principal que controla el flujo del programa."""
    calcular()

if __name__ == "__main__":
    main()