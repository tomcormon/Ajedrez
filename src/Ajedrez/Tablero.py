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

        # fichas negras:
        self.fichas[Tablero.D][Tablero.king] = King(Tablero.D, self.casillas[(5, 8)])
        self.fichas[Tablero.D][Tablero.queen] = Queen(Tablero.D, self.casillas[(4, 8)])
        self.fichas[Tablero.D][Tablero.rook_king] = Rook(Tablero.D, self.casillas[(1, 8)], Tablero.rook_king)
        self.fichas[Tablero.D][Tablero.rook_queen] = Rook(Tablero.D, self.casillas[(8, 8)], Tablero.rook_queen)
        self.fichas[Tablero.D][Tablero.bishop_king] = Bishop(Tablero.D, self.casillas[(3, 8)], Tablero.bishop_king)
        self.fichas[Tablero.D][Tablero.bishop_queen] = Bishop(Tablero.D, self.casillas[(6, 8)], Tablero.bishop_queen)

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

    def cassilla_dir(self, direccion):
        return self.casillas_adyacentes[direccion]


class Ficha:

    def __init__(self, color, casilla: Casilla, tipo, valor):
        self.color = color
        self.casilla = casilla
        self.tipo = tipo
        self.valor = valor
        self.lista_posibles_jugadas = self.posibles_jugadas()
        self.lista_atacadas = self.casillas_atacadas()

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
            casilla_variable = self.casilla.cassilla_dir(i)
            while casilla_variable:
                if casilla_variable.ocupacion:
                    if casilla_variable.ocupacion.color != self.color:
                        pos_jug.append(casilla_variable)
                    break
                else:
                    pos_jug.append(casilla_variable)
                casilla_variable = casilla_variable.cassilla_dir(i)
        return pos_jug

    def dar_rayos_ataques(self, direcciones):
        pos_jug = []
        for i in direcciones:
            casilla_variable = self.casilla.cassilla_dir(i)
            while casilla_variable:
                if casilla_variable.ocupacion:
                    pos_jug.append(casilla_variable)
                    break
                else:
                    pos_jug.append(casilla_variable)
                casilla_variable = casilla_variable.cassilla_dir(i)
        return pos_jug

    def informar_a_las_casillas_que_estan_atacadas(self):
        if self.casillas_atacadas() is not None:
            for i in self.casillas_atacadas():
                i.atacado[self.color] = True

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

    def posibles_jugadas(self):
        return self.dar_rayos_posibles_jugadas([Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])

    def casillas_atacadas(self):
        return self.dar_rayos_ataques([Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])


class Rook(Ficha):
    def __init__(self, color, casilla, tipo):
        super().__init__(color, casilla, tipo, valor=5)

    def posibles_jugadas(self):
        return self.dar_rayos_posibles_jugadas([Casilla.up, Casilla.down, Casilla.left, Casilla.right])

    def casillas_atacadas(self):
        return self.dar_rayos_ataques([Casilla.up, Casilla.down, Casilla.left, Casilla.right])


class Queen(Ficha):
    def __init__(self, color, casilla):
        super().__init__(color, casilla, tipo=Tablero.queen, valor=9)

    def posibles_jugadas(self):
         return self.dar_rayos_posibles_jugadas([Casilla.up, Casilla.down, Casilla.left, Casilla.right,
                  Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])

    def casillas_atacadas(self):
        return self.dar_rayos_ataques([Casilla.up, Casilla.down, Casilla.left, Casilla.right,
                  Casilla.up_left, Casilla.down_right, Casilla.down_right, Casilla.up_right])


class Pawn(Ficha):
    def __init__(self, color, casilla, tipo):
            super().__init__(color, casilla, tipo, valor=1)

    def posibles_jugadas(self):
        if self.color:
            return [self.casilla.casillas_adyacentes(Casilla.up)]
        else:
            return [self.casilla.casillas_adyacentes(Casilla.down)]

    def casillas_atacadas(self):
        if self.color:
            return [self.casilla.casillas_adyacentes(Casilla.up_left),elf.casilla.casillas_adyacentes(Casilla.up_right)]
        else:
            return [self.casilla.casillas_adyacentes(Casilla.down_left),elf.casilla.casillas_adyacentes(Casilla.down_right)]


class Knith():
    def __init__(self, color, casilla, tipo):
            super().__init__(color, casilla, tipo,  valor=3)

    def posibles_jugadas(self):
        if self.color:
            return [self.casilla.casillas_adyacentes(Casilla.up)]
        else:
            return [self.casilla.casillas_adyacentes(Casilla.down)]

    def casillas_atacadas(self):
        if self.color:
            return [self.casilla.casillas_adyacentes(Casilla.up_left),elf.casilla.casillas_adyacentes(Casilla.up_right)]
        else:
            return [self.casilla.casillas_adyacentes(Casilla.down_left),elf.casilla.casillas_adyacentes(Casilla.down_right)]




