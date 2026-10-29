def definir_sala(filas, columnas):
    """Crea una sala de cine con las dimensiones especificadas."""
    sala = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("L")
        sala.append(fila)
    return sala


def mostrar_sala(sala):
    """Muestra la sala de cine con números de fila y columna, sin usar range()."""
    # Cabecera con los números de columna
    print("  ", end="")
    numero_columna = 1
    while numero_columna <= len(sala[0]):
        print(numero_columna, end="  ")
        numero_columna = numero_columna + 1
    print()

    # Filas con su número delante
    numero_fila = 1
    for fila in sala:
        print(numero_fila, "", end=" ")
        for butaca in fila:
            print(butaca, end="  ")
        print()
        numero_fila = numero_fila + 1

def reservar_butaca(sala, fila, columna):
    """Reserva una butaca si está disponible."""
    if sala[fila][columna] == "L":
        sala[fila][columna] = "R"
        print("Reserva realizada correctamente")
    else:
        print("La butaca está ocupada")


def introducir_numero(numero):
    """Solicita al usuario que introduzca un número entero."""
    while True:
        try:
            valor = int(input(f"Introduce {numero}: "))
            return valor
        except ValueError:
            print("Por favor, introduce un número entero válido.")


def gestionar_reservas(sala):
    """Gestiona el proceso completo de reservas hasta que el usuario decide salir."""
    while True:
        fila = introducir_numero("la fila (1-12, o 0 para salir)")

        if fila == 0:
            print("Saliendo del programa...")
            break

        columna = introducir_numero("la butaca (1-20)")

        fila = fila - 1
        columna = columna - 1

        reservar_butaca(sala, fila, columna)

        mostrar_sala(sala)