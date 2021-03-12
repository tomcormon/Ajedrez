from itertools import product
from numpy import inf


class Tablero:
    W = True  # Representa blanco
    D = False  # Representa negro
    King = "King"

    def __init__(self):
        self.casillas = {(m, n): Casilla(nombre=Tablero.dar_nombre((m, n)),
                                         posicion=(m, n),
                                         ocupacion=None,
                                         tablero=self) for m in range(1, 9) for n in range(1, 9)}
        for c in self.casillas.values():
            c.llenar_casillas_adyacentes()

        self.fichas = {Tablero.W: {}, Tablero.D: {}}

        # fichas blancas:
        self.fichas[Tablero.W][Tablero.King] = Rey(Tablero.W, self.casillas[(5, 1)])

        # fichas negras:
        self.fichas[Tablero.D][Tablero.King] = Rey(Tablero.D, self.casillas[(5, 8)])

        for i in [Tablero.W, Tablero.D]:
            for j in self.fichas[i].values():
                j.informar_a_las_casillas_que_estan_atacadas()

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

    def __init__(self, nombre, posicion, ocupacion, tablero: Tablero):
        self.nombre = nombre
        self.posicion = posicion
        self.ocupacion = ocupacion
        self.tablero = tablero
        self.casillas_adyacentes = {}
        self.atacado = {Tablero.W: False, Tablero.D: False}

    def __repr__(self):
        return f"nombre: {self.nombre}, posicion:{self.posicion}, ficha:{self.ocupacion}"

    def check_candidato(self, candidato):
        if candidato in self.tablero.casillas.keys():
            return self.tablero.casillas[candidato]

    def llenar_casillas_adyacentes(self):
        dic = {}
        dic["U"] = self.check_candidato((self.posicion[0], self.posicion[1] + 1))
        dic["D"] = self.check_candidato((self.posicion[0], self.posicion[1] - 1))
        dic["L"] = self.check_candidato((self.posicion[0] - 1, self.posicion[1]))
        dic["R"] = self.check_candidato((self.posicion[0] + 1, self.posicion[1]))
        dic["UR"] = self.check_candidato((self.posicion[0] + 1, self.posicion[1] + 1))
        dic["UL"] = self.check_candidato((self.posicion[0] - 1, self.posicion[1] + 1))
        dic["DR"] = self.check_candidato((self.posicion[0] + 1, self.posicion[1] - 1))
        dic["DL"] = self.check_candidato((self.posicion[0] - 1, self.posicion[1] - 1))
        self.casillas_adyacentes = dic

    def cassilla_dir(self, direccion):
        return self.casilla_adyacentes[direccion]


class Ficha:
    def __init__(self, color, casilla: Casilla, tipo, valor):
        self.color = color
        self.casilla = casilla
        self.tipo = tipo
        self.valor = valor
        self.posibles_jugadas = self.posibles_jugadas()

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
        # Devuelve una lista de las casillas atacadas por la pieza
        ...

    def informar_a_las_casillas_que_estan_atacadas(self):
        if self.casillas_atacadas() is not None:
            for i in self.casillas_atacadas():
                i.atacado[self.color] = True

    def posibles_capturas(self):
        ...

    def ataques_indirectos(self):
        ...

    def posibles_jaques(self):
        ...


class Rey(Ficha):
    def __init__(self, color, casilla):
        super().__init__(color, casilla, tipo="Rey", valor=inf)

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
