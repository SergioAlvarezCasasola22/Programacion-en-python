# 1. Validar que sea un número (usando try/except)

def pedir_entero():
    while True:
        entrada = input("Introduce un número entero: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Error: eso no es un número entero válido. Inténtalo de nuevo.")

edad = pedir_entero()
print(f"Tu edad es {edad}")


#2. Validar que esté dentro de un rango

def pedir_edad():
    while True:
        entrada = input("Introduce tu edad (0-120): ")
        try:
            edad = int(entrada)
        except ValueError:
            print("Error: debes introducir un número entero.")
            continue

        if 0 <= edad <= 120:
            return edad
        else:
            print("Error: la edad debe estar entre 0 y 120.")

edad = pedir_edad()

# 3. Validar letras/texto (solo caracteres alfabéticos)

def pedir_nombre():
    while True:
        nombre = input("Introduce tu nombre (solo letras): ")
        if nombre.isalpha():
            return nombre
        else:
            print("Error: el nombre solo puede contener letras.")

nombre = pedir_nombre()

#Nota: isalpha() no acepta espacios. Si quieres permitir nombres compuestos ("Juan Pérez"), usa algo como nombre.replace(" ", "").isalpha().

# 4. Validar que esté dentro de un conjunto de opciones válidas

def pedir_opcion():
    opciones_validas = ["s", "n"]
    while True:
        respuesta = input("¿Continuar? (s/n): ").lower()
        if respuesta in opciones_validas:
            return respuesta
        else:
            print("Error: responde con 's' o 'n'.")

respuesta = pedir_opcion()
