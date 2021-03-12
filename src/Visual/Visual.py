import matplotlib.pyplot as plt
import numpy as np

from Ajedrez.Tablero import Ficha


class visualizer:
	@staticmethod
	def show():
		plt.show()
	
	@staticmethod
	def plain_board():
		n = 8
		image = np.array([[0 if (i + j) % 2 == 0 else 1 for j in range(n)] for i in range(n)], dtype=float)
		return image
	
	@staticmethod
	def board(board):
		n = 8
		fig, ax = plt.subplots()
		row_labels = range(1, n + 1)
		col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
		ax.matshow(board, cmap='gist_ncar')
		plt.xticks(range(n), col_labels)
		plt.yticks(range(n), row_labels)

		return fig, ax

	@staticmethod
	def piece(piece: Ficha):
		image = visualizer.plain_board()
		for c in piece.lista_posibles_jugadas:
			i, j = c.posicion
			image[j - 1, i - 1] = 0.7

		i, j = piece.casilla.posicion
		image[j - 1, i - 1] = 0.3

		visualizer.board(image)
