#Mi primer programa en python
operador_uno = float(input("Ingrese el primer operador: "))
operando = input("Ingrese el operador (+, -, *, /): ") 
operador_dos = float(input("Ingrese el segundo operador: "))
error = False

if operando == "+":
    resultado = operador_uno + operador_dos
    
elif operando == "-":
    resultado = operador_uno - operador_dos
    
elif operando == "*":
    resultado = operador_uno * operador_dos
    
elif operando == "/":
    if operador_dos == 0:
        print("Error: No se puede dividir entre cero.")
        error = True
    else:
        resultado = operador_uno / operador_dos
else:
    print(f"Operador no válido: {operando}")
    error = True

if not error:
    print(f"El resultado de {operador_uno} {operando} {operador_dos} es: {resultado}")