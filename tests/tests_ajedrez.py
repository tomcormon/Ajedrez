import Ajedrez
from Ajedrez.Tablero import Tablero, Casilla, Ficha


mi_tablero=Tablero()
mi_tablero.mostrar_casillas()

for i in mi_tablero.casillas.values():
    print(i.nombre, i.atacado[True], i.atacado[False])


for i in [Ajedrez.Tablero.Tablero.D, Ajedrez.Tablero.Tablero.W]:
    for j in mi_tablero.fichas[i].values():
        print(j)
        print(j.casillas_atacadas())
