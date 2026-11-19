import time
import math


class ParkingError(Exception):
    """Error de negocio del parking (lleno, duplicado, no encontrado...)."""
    pass


class Plaza:
    def __init__(self, numero):
        self.numero = numero
        self.matricula = None
        self.hora_entrada = None

    def esta_libre(self):
        if self.matricula == None:
            return True
        else:
            return False


class Parking:
    def __init__(self):
        self.plazas = []
        for i in range(20):
            self.plazas.append(Plaza(i + 1))
        self.recaudacion = 0

    def normalizar(self, matricula):
        return matricula.upper().replace(" ", "")

    def buscar_plaza_libre(self):
        for p in self.plazas:
            if p.esta_libre():
                return p
        return None

    def entrada(self, matricula, ahora=None):
        matricula = self.normalizar(matricula)
        for p in self.plazas:
            if p.matricula == matricula:
                raise ParkingError("La matricula " + matricula + " ya esta en el parking")
        plaza = self.buscar_plaza_libre()
        if plaza == None:
            raise ParkingError("El parking esta lleno")
        plaza.matricula = matricula
        if ahora == None:
            ahora = time.time()
        plaza.hora_entrada = ahora
        return plaza.numero

    def salida(self, matricula, ahora=None):
        matricula = self.normalizar(matricula)
        plaza = None
        for p in self.plazas:
            if p.matricula == matricula:
                plaza = p
        if plaza == None:
            raise ParkingError("La matricula " + matricula + " no esta en el parking")
        if ahora == None:
            ahora = time.time()
        segundos = ahora - plaza.hora_entrada
        minutos = max(1, math.ceil(segundos / 60))
        importe = minutos * 0.05
        return minutos, importe

    def libres(self):
        contador = 0
        for p in self.plazas:
            if p.esta_libre():
                contador = contador + 1
        return contador

    def estado(self):
        lineas = []
        for p in self.plazas:
            if p.esta_libre() == True:
                lineas.append("Plaza " + str(p.numero) + ": LIBRE")
            else:
                lineas.append("Plaza " + str(p.numero) + ": OCUPADA (" + p.matricula + ")")
        return lineas