from Ajedrez.Tablero import *
from Ajedrez.Ficha import *


class casilla(object):
    """docstring for casilla"""

    def __init__(self, nombre, posicion, ocupacion, tablero: Tablero):
        super(casilla, self).__init__()
        self.nombre = nombre
        self.posicion = posicion
        self.ocupacion = ocupacion
        self.tablero = tablero
        self.casilla_adyacentes = {}

    def llenar_casillas_adyacentes(self, direccion):
        ''' resive un objeto casilla una direccion y devuelve la posicion de la caslla adyacente'''
        casilla_adyacente = []

        if direccion == "U":
            casilla_adyacente = [ str( dic_nl self.posicion[0]), str(self.posicion[1] + 1)]
            return casilla_adyacente
        elif direccion == "D":
            casilla_adyacente = [self.posicion[0], self.posicion[1] - 1]
            return casilla_adyacente
        elif direccion == "R":
            casilla_adyacente = [self.posicion[0] + 1, self.posicion[1]]
            return casilla_adyacente
        elif direccion == "L":
            casilla_adyacente = [self.posicion[0] - 1, self.posicion[1]]
            return casilla_adyacente
        elif direccion == "UR":
            casilla_adyacente = [self.posicion[0] + 1, self.posicion[1] + 1]
            return casilla_adyacente
        elif direccion == "UL":
            casilla_adyacente = [self.posicion[0] - 1, self.posicion[1] + 1]
            return casilla_adyacente
        elif direccion == "DR":
            casilla_adyacente = [self.posicion[0] + 1, self.posicion[1] - 1]
            return casilla_adyacente
        elif direccion == "DL":
            casilla_adyacente = [self.posicion[0] - 1, self.posicion[1] - 1]
            return casilla_adyacente
        else:
            return "esa direccion no es valida"