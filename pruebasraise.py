"""
EJEMPLO1
def dividir(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        resultado = a / b
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    else:
        print(f"El resultado es: {resultado}")


dividir(10, 2)
dividir(10, 0)
"""
"""
EJEMPLO2
def validar_edad():
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Error: debes introducir un número entero")
        return

    try:
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if edad > 100:
            raise ValueError("Esa edad no es realista")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        print(f"Edad válida: {edad} años")


validar_edad()
"""
#EJEMPLO3
def sacar_dinero(saldo):
    try:
        importe = int(input("Introduce la cantidad a retirar: "))
    except ValueError:
        print("Error: debes introducir un número entero")
        return saldo

    try:
        if importe < 0:
            raise ValueError("No se puede retirar una cantidad negativa")
        if importe > saldo:
            raise ValueError("Saldo insuficiente para esa retirada")
    except ValueError as error:
        print(f"Error: {error}")
    else:
        saldo = saldo - importe
        print(f"Retirada realizada. Saldo actual: {saldo}")
    finally:
        print("Operación finalizada.")

    return saldo


saldo = 100
saldo = sacar_dinero(saldo)