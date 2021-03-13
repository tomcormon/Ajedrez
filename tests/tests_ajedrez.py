import Ajedrez
from Ajedrez.Tablero import Tablero, Casilla, Ficha
from Visual.Visual import visualizer as vis


def test_visual():
    mi_tablero=Tablero()
    f = mi_tablero.fichas[Tablero.D][Tablero.pawns[2]]
    vis.piece_attacked(f)
    vis.show()


def test_board():
    mi_tablero=Tablero()
    mi_tablero.mostrar_casillas()

    for i in mi_tablero.casillas.values():
        print(i.nombre, i.atacado[True], i.atacado[False])

    for i in [Ajedrez.Tablero.Tablero.D, Ajedrez.Tablero.Tablero.W]:
        for j in mi_tablero.fichas[i].values():
            print(j)
            print(j.casillas_atacadas())


if __name__ == '__main__':
    test_visual()