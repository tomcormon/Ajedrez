from itertools import product
from typing import List, Any

from numpy import inf


class Tablero:
    W = True  # Representa blanco
    D = False  # Representa negro

    king = 'king'
    queen = 'queen'
    bishop_king = 'bishop_king'
    bishop_queen = 'bishop_queen'
    knight_king = 'knight_king'
    knight_queen = 'knight_queen'
    rook_king = 'rook_king'
    rook_queen = 'rook_queen'
    pawns = [f'pawn_{i}' for i in range(1, 9)]

    def __init__(self):
        self.casillas = {(m, n): Casilla(nombre=Tablero.dar_nombre((m, n)),
                                         posicion=(m, n),
                                         ocupacion=None,
                                         tablero=self) for m in range(1, 9) for n in range(1, 9)}
        for c in self.casillas.values():
            c.llenar_casillas_adyacentes()


        #crea el atributo fichas en el cual tiene
        #las fichas Withe y Dark.

        self.fichas = {Tablero.W: {}, Tablero.D: {}}

        #se crean las fichas blancas i negras y se meten
        #en la lista de fichas del tablero

        # fichas blancas:
        self.fichas[Tablero.W][Tablero.king] = King(Tablero.W, self.casillas[(5, 1)])
        self.fichas[Tablero.W][Tablero.queen] = Queen(Tablero.W, self.casillas[(4, 1)])
        self.fichas[Tablero.W][Tablero.rook_king] = Rook(Tablero.W, self.casillas[(1, 1)], Tablero.rook_queen)
        self.fichas[Tablero.W][Tablero.rook_queen] = Rook(Tablero.W, self.casillas[(8, 1)], Tablero.rook_king)
        self.fichas[Tablero.W][Tablero.bishop_queen] = Bishop(Tablero.W, self.casillas[(3, 1)], Tablero.bishop_queen)
        self.fichas[Tablero.W][Tablero.bishop_king] = Bishop(Tablero.W, self.casillas[(6, 1)], Tablero.bishop_king)
        self.fichas[Tablero.W][Tablero.knight_king] = Knight(Tablero.W, self.casillas[(7, 1)], Tablero.knight_king)
        self.fichas[Tablero.W][Tablero.knight_queen] = Knight(Tablero.W, self.casillas[(2, 1)], Tablero.knight_queen)
        for i in range(1,9):
            self.fichas[Tablero.W][Tablero.pawns[i-1]] = Pawn(Tablero.W, self.casillas[(i,2)], Tablero.pawns[i-1])

        # fichas negras:
        self.fichas[Tablero.D][Tablero.king] = King(Tablero.D, self.casillas[(5, 8)])
        self.fichas[Tablero.D][Tablero.queen] = Queen(Tablero.D, self.casillas[(4, 8)])
        self.fichas[Tablero.D][Tablero.rook_king] = Rook(Tablero.D, self.casillas[(1, 8)], Tablero.rook_king)
        self.fichas[Tablero.D][Tablero.rook_queen] = Rook(Tablero.D, self.casillas[(8, 8)], Tablero.rook_queen)
        self.fichas[Tablero.D][Tablero.bishop_king] = Bishop(Tablero.D, self.casillas[(3, 8)], Tablero.bishop_king)
        self.fichas[Tablero.D][Tablero.bishop_queen] = Bishop(Tablero.D, self.casillas[(6, 8)], Tablero.bishop_queen)
        self.fichas[Tablero.D][Tablero.knight_king] = Knight(Tablero.D, self.casillas[(7, 8)], Tablero.knight_king)
        self.fichas[Tablero.D][Tablero.knight_queen] = Knight(Tablero.D, self.casillas[(2, 8)], Tablero.knight_queen)
        for i in range(1,9):
            self.fichas[Tablero.D][Tablero.pawns[i-1]] = Pawn(Tablero.D, self.casillas[(i,7)], Tablero.pawns[i-1])


        #se llama una funcion que edita el atributo
        # atacado para cada casilla
        for i in [Tablero.W, Tablero.D]:
            for j in self.fichas[i].values():
                j.informar_a_las_casillas_que_estan_atacadas()

        #cada pieza le avisa a su casilla que esta ocupada edita
        #el atributo ocupacion de su casilla
        for i in [Tablero.W, Tablero.D]:
            for j in self.fichas[i].values():
                j.informar_a_las_casillas_que_estan_ocupadas()

        for fW, fD in zip(self.fichas[Tablero.W].values(), self.fichas[Tablero.D].values()):
            fW.lista_posibles_jugadas = fW.posibles_jugadas()
            fD.lista_posibles_jugadas = fD.posibles_jugadas()
            fW.lista_atacadas = fW.casillas_atacadas()
            fD.lista_atacadas = fD.casillas_atacadas()


    @staticmethod
    def dar_nombre(posicion):
        """
        returns the name of a given position.

        Parameters
        ----------
        posicion: tuple
            the position for returning the name.

        Returns
        -------
        str
           The name.

        """
        dic_nl = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
        i, j = posicion
        return f"{dic_nl[i]}{j}"

    @staticmethod
    def dar_posicion(nombre):
        dic_ln = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        n, i = tuple(nombre)
        i = int(i)
        return (dic_ln[n], i)

    def mostrar_casillas(self):
        for c in self.casillas.values():
            print(c)

    def revisar_si_posicion_esta_en_tablero(self, posicion):
        return posicion in self.casillas.keys()


class Casilla:
    up = "U"
    down = "D"
    left = "L"
    right = "R"
    up_right = "UR"
    up_left = "UL"
    down_right = "DR"
    down_left = "DL"

    def __init__(self, nombre, posicion, ocupacion, tablero: Tablero):
        self.nombre = nombre
        self.posicion = posicion
        self.ocupacion = ocupacion
        self.tablero = tablero
        self.casillas_adyacentes = {}
        self.atacado = {Tablero.W: False, Tablero.D: False}

    def __repr__(self):
        return f"nombre: {self.nombre}, posicion:{self.posicion}, ficha:{self.ocupacion}, atacadapor W:{list(self.atacado.values())[0]} D:{list(self.atacado.values())[1]}"

    def check_candidato(self, candidato):
        if candidato in self.tablero.casillas.keys():
            return self.tablero.casillas[candidato]

    def llenar_casillas_adyacentes(self):
        dic = {}
        dic[self.up] = self.check_candidato((self.posicion[0], self.posicion[1] + 1))
        dic[self.down] = self.check_candidato((self.posicion[0], self.posicion[1] - 1))
        dic[self.left] = self.check_candidato((self.posicion[0] - 1, self.posicion[1]))
        dic[self.right] = self.check_candidato((self.posicion[0] + 1, self.posicion[1]))
        dic[self.up_right] = self.check_candidato((self.posicion[0] + 1, self.posicion[1] + 1))
        dic[self.up_left] = self.check_candidato((self.posicion[0] - 1, self.posicion[1] + 1))
        dic[self.down_right] = self.check_candidato((self.posicion[0] + 1, self.posicion[1] - 1))
        dic[self.down_left] = self.check_candidato((self.posicion[0] - 1, self.posicion[1] - 1))
        self.casillas_adyacentes = dic

    def casilla_dir(self, direccion):
        return self.casillas_adyacentes[direccion]


class Ficha:

    def __init__(self, color, casilla: Casilla, tipo, valor):
        self.color = color
        self.casilla = casilla
        self.tipo = tipo
        self.valor = valor
        self.lista_posibles_jugadas = self.posibles_jugadas()
        self.lista_atacadas = self.casillas_atacadas()
        self.image = None

    def __repr__(self):
        col = "Negro"
        if self.color:
            col = "Blanco"
        return f"{self.tipo} {col}, posicion:{self.casilla.nombre}"

    def posibles_jugadas(self):
        """

        Returns
        -------

        """

        ...

    def casillas_atacadas(self):
        """
        Computes the list of attacked squares.

        Returns
        -------
        list
            The list with the attacked squares.
        """
        ...

    def dar_rayos_posibles_jugadas(self, direcciones):
        pos_jug = []
        for i in direcciones:
            casilla_variable = self.casilla.casilla_dir(i)
            while casilla_variable:
                if casilla_variable.ocupacion:
                    if casilla_variable.ocupacion.color != self.color:
                        pos_jug.append(casilla_variable)
                    break
                else:
                    pos_jug.append(casilla_variable)
                casilla_variable = casilla_variable.casilla_dir(i)
        return pos_jug

    def dar_rayos_ataques(self, direcciones):
        pos_jug = []
        for i in direcciones:
            casilla_variable = self.casilla.casilla_dir(i)
            while casilla_variable:
                if casilla_variable.ocupacion:
                    pos_jug.append(casilla_variable)
                    break
                else:
                    pos_jug.append(casilla_variable)
                casilla_variable = casilla_variable.casilla_dir(i)
        return pos_jug

    def informar_a_las_casillas_que_estan_atacadas(self):
        if self.casillas_atacadas() is not None:
            for i in self.casillas_atacadas():
                try:
                    i.atacado[self.color] = True
                except:
                    print("que putas")

    def informar_a_las_casillas_que_estan_ocupadas(self):
        self.casilla.ocupacion = self

    def posibles_capturas(self):
        ...

    def ataques_indirectos(self):
        ...

    def posibles_jaques(self):
        ...


class King(Ficha):
    def __init__(self, color, casilla):
        super().__init__(color, casilla, tipo=Tablero.king, valor=inf)
        c = 'w' if self.color else 'd'
        self.image = f'figures/{c}_king.png'

    def posibles_jugadas(self):
        pos_jug = []
        for i in self.casilla.casillas_adyacentes.values():
            if i is not None:
                if not i.atacado[not self.color]:
                    if i.ocupacion is None:
                        pos_jug.append(i)
                    elif i.ocupacion.color != self.color:
                        pos_jug.append(i)
        return pos_jug

    def casillas_atacadas(self):
        cas_ata = []
        for i in self.casilla.casillas_adyacentes.values():
            if i is not None:
                cas_ata.append(i)
        return cas_ata


class Bishop(Ficha):
    def __init__(self, color, casilla, tipo):
        super().__init__(color, casilla, tipo=tipo, valor=3)
        c = 'w' if self.color else 'd'
        self.image = f'figures/{c}_bishop.png'

    def posibles_jugadas(self):
        return self.dar_rayos_posibles_jugadas([Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])

    def casillas_atacadas(self):
        return self.dar_rayos_ataques([Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])


class Rook(Ficha):
    def __init__(self, color, casilla, tipo):
        super().__init__(color, casilla, tipo, valor=5)
        c = 'w' if self.color else 'd'
        self.image = f'figures/{c}_rook.png'

    def posibles_jugadas(self):
        return self.dar_rayos_posibles_jugadas([Casilla.up, Casilla.down, Casilla.left, Casilla.right])

    def casillas_atacadas(self):
        return self.dar_rayos_ataques([Casilla.up, Casilla.down, Casilla.left, Casilla.right])


class Queen(Ficha):
    def __init__(self, color, casilla):
        super().__init__(color, casilla, tipo=Tablero.queen, valor=9)
        c = 'w' if self.color else 'd'
        self.image = f'figures/{c}_queen.png'

    def posibles_jugadas(self):
         return self.dar_rayos_posibles_jugadas([Casilla.up, Casilla.down, Casilla.left, Casilla.right,
                  Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])

    def casillas_atacadas(self):
        return self.dar_rayos_ataques([Casilla.up, Casilla.down, Casilla.left, Casilla.right,
                  Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])


class Pawn(Ficha):
    def __init__(self, color, casilla, tipo):
        super().__init__(color, casilla, tipo, valor=1)
        c = 'w' if self.color else 'd'
        self.image = f'figures/{c}_pawn.png'

    def posibles_jugadas(self):
        if self.color:
            return [self.casilla.casilla_dir(Casilla.up)]
        elif not self.color:
            return [self.casilla.casilla_dir(Casilla.down)]

    def casillas_atacadas(self):
        cas_ata=[]
        if self.color:
            if self.casilla.casilla_dir(Casilla.up_left):
                cas_ata.append(self.casilla.casilla_dir(Casilla.up_left))

            if self.casilla.casilla_dir(Casilla.up_right):
                cas_ata.append(self.casilla.casilla_dir(Casilla.up_right))

        else:
            if self.casilla.casilla_dir(Casilla.down_left):
                cas_ata.append(self.casilla.casilla_dir(Casilla.down_left))
            if self.casilla.casilla_dir(Casilla.down_right):
                cas_ata.append(self.casilla.casilla_dir(Casilla.down_right))
        return cas_ata


class Knight(Ficha):
    def __init__(self, color, casilla, tipo):
        super().__init__(color, casilla, tipo,  valor=3)
        c = 'w' if self.color else 'd'
        self.image = f'figures/{c}_knight.png'

    def posibles_jugadas(self):
        pos_jug = []
        for i in [Casilla.up, Casilla.down]:
           for j in [Casilla.right, Casilla.left]:
                if i != j:
                     if self.casilla.casilla_dir(i):
                         if self.casilla.casilla_dir(i).casilla_dir(i):
                             if self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j):
                                pos_jug.append(self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j))
        for i in [Casilla.right, Casilla.left]:
           for j in [Casilla.up, Casilla.down]:
                if i != j:
                     if self.casilla.casilla_dir(i):
                         if self.casilla.casilla_dir(i).casilla_dir(i):
                             if self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j):
                                pos_jug.append(self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j))
        return pos_jug

    def casillas_atacadas(self):
        pos_jug = []
        for i in [Casilla.up, Casilla.down]:
           for j in [Casilla.right, Casilla.left]:
                     if self.casilla.casilla_dir(i):
                         if self.casilla.casilla_dir(i).casilla_dir(i):
                             if self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j):
                                if self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j).ocupacion == None :
                                    pos_jug.append(self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j))

        for i in [Casilla.right, Casilla.left]:
           for j in [Casilla.up, Casilla.down]:
                     if self.casilla.casilla_dir(i):
                         if self.casilla.casilla_dir(i).casilla_dir(i):
                             if self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j):
                                 if self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j).ocupacion == None:
                                    pos_jug.append(self.casilla.casilla_dir(i).casilla_dir(i).casilla_dir(j))

        return pos_jug



