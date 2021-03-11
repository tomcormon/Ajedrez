from Ajedrez.Tablero import *
from Ajedrez.Casilla import *
from Ajedrez.Casilla import *


class ficha(object):
	def __init__(self, color, posicion):
		self.color = color
		self.posicion = posicion

	def __repr__(self):
		return f"{self.posicion}-{self.color}"

	def __call__(self):
		pass


	def posibles_jugadas(self):
		...


class rey(ficha):
	def __init__(self):
		super(self).__init__()
	def posibles_jugadas(self):
		pass

