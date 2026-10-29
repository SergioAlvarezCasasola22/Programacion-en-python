from parking import Parking


def mostrar_menu():
    print("")
    print("===== PARKING =====")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Estado del parking")
    print("4. Salir")


def main():
    parking = Parking()
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            matricula = input("Matricula: ")
            try:
                numero = parking.entrada(matricula)
                print("Coche aparcado en la plaza " + str(numero))
            except ParkingError as e:
                print("Error: " + str(e))
        elif opcion == "2":
            matricula = input("Matricula: ")
            try:
                minutos, importe = parking.salida(matricula)
                print("Tiempo: " + str(minutos) + " minutos")
                print("Importe a pagar: " + str(importe) + " euros")
            except ParkingError as e:
                print("Error: " + str(e))
        elif opcion == "3":
            for linea in parking.estado():
                print(linea)
            print("Plazas libres: " + str(parking.libres()))
        elif opcion == "4":
            print("Recaudacion total: " + str(parking.recaudacion) + " euros")
        else:
            print("Opcion no valida")


main()