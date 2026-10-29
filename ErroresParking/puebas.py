"""Pruebas del parking (Fase 2 de la ficha).

Ejecuta:  python pruebas.py
Cada prueba debe acabar en OK. Completa las que dicen PENDIENTE.
Pista: usa el parametro `ahora` (segundos) para simular el paso del tiempo.
"""

from parking import Parking, ParkingError


def prueba_ejemplo():
    """Ejemplo resuelto: primer coche, duplicado y cobro a los 61 segundos."""
    p = Parking()

    # El primer coche va a la plaza 1
    assert p.entrada("1234 abc", ahora=0) == 1

    # La misma matricula escrita de otra forma debe dar error
    try:
        p.entrada("1234ABC", ahora=0)
        assert False, "deberia haber dado error de duplicado"
    except ParkingError:
        pass

    # A los 61 segundos hay que cobrar 2 minutos (redondeo hacia arriba)
    minutos, importe = p.salida("1234ABC", ahora=61)
    assert minutos == 2
    assert float(importe) == 0.10


def prueba_1_minimo_un_minuto():
    """Salir a los 0 segundos cuesta 1 minuto (0,05 euros)."""
    raise NotImplementedError("Escribe esta prueba")


def prueba_2_redondeo_hacia_arriba():
    """A los 60 segundos: 1 minuto. A los 60,1 segundos: 2 minutos."""
    raise NotImplementedError("Escribe esta prueba")


def prueba_3_parking_lleno():
    """Con 20 coches dentro, el 21.o recibe un error de parking lleno."""
    raise NotImplementedError("Escribe esta prueba")


def prueba_4_plaza_se_libera():
    """Cuando un coche sale, su plaza queda libre y la usa el siguiente."""
    raise NotImplementedError("Escribe esta prueba")


def prueba_5_recaudacion():
    """Tras varias salidas, la recaudacion es la suma de todos los importes."""
    raise NotImplementedError("Escribe esta prueba")


PRUEBAS = [
    prueba_ejemplo,
    prueba_1_minimo_un_minuto,
    prueba_2_redondeo_hacia_arriba,
    prueba_3_parking_lleno,
    prueba_4_plaza_se_libera,
    prueba_5_recaudacion,
]


if __name__ == "__main__":
    for prueba in PRUEBAS:
        try:
            prueba()
            print("OK        " + prueba.__name__)
        except NotImplementedError:
            print("PENDIENTE " + prueba.__name__)
        except AssertionError as e:
            print("FALLO     " + prueba.__name__ + " -> " + str(e))