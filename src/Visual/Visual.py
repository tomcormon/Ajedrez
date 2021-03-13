from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from Ajedrez.Tablero import Ficha, Tablero


class visualizer:
	@staticmethod
	def show():
		plt.show()
	
	@staticmethod
	def plain_board():
		n = 8
		image = np.array([[1 if (i + j) % 2 == 0 else 0 for j in range(n)] for i in range(n)], dtype=float)
		return image
	
	@staticmethod
	def board(board):
		n = 8
		fig, ax = plt.subplots()
		row_labels = list(range(1, n + 1))[:: -1]
		col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
		ax.matshow(board, cmap='gist_ncar')
		plt.xticks(range(n), col_labels)
		plt.yticks(range(n), row_labels)

		return fig, ax

	@staticmethod
	def piece_reach(piece: Ficha, reach):
		image = visualizer.plain_board()
		for c in reach:
			i, j = c.posicion
			image[j - 1, i - 1] = 0.7

		fig, ax = visualizer.filled_board(piece.casilla.tablero, image)
		visualizer.plot_figure(ax, piece)

	@staticmethod
	def plot_figure(ax, piece: Ficha):
		arr_lena = mpimg.imread(piece.image)
		imagebox = OffsetImage(arr_lena, zoom=0.3)
		i, j = piece.casilla.posicion
		ab = AnnotationBbox(imagebox, (i - 1, 8 - j), frameon=False)
		ax.add_artist(ab)
		plt.draw()

	@staticmethod
	def filled_board(board: Tablero, img_board=None):
		if img_board is None:
			img_board = visualizer.plain_board()
		fig, ax = visualizer.board(img_board)
		for fw, fb in zip(board.fichas[Tablero.W].values(), board.fichas[Tablero.D].values()):
			visualizer.plot_figure(ax, fw)
			visualizer.plot_figure(ax, fb)

		return fig, ax
