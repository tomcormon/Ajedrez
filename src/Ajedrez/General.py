global dic_nl, dic_ln, lista_1_al_n

def lista_1_al_n(n):
	i=1
	L=[]
	while i<=n:
		L.append(i)
		i+=1
	return L
dic_nl = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
dic_ln = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}



casillas=[]
for m in lista_1_al_n(8): 
	for n in lista_1_al_n(8):
		casillas.append([m,n])
casillas_posicion=[]
casillas_posicion+=casillas


casillasLetra=[]
for m in lista_1_al_n(8): 
	for n in lista_1_al_n(8):
		casillasLetra.append([dic_nl[m],n])
casillas_nombres=[]
for i in casillasLetra:
	casillas_nombres.append(str(i[0])+str(i[1]))

direcciones=["U","D","R","L","UR","UL","DR","DL"]

def casilla_adyacente_posicion_posicion(posicion,direccion):
	casilla_adyacente=[]
	
	if direccion=="U":
		casilla_adyacente=[posicion[0],posicion[1]+1]
		return casilla_adyacente
	elif direccion=="D":
		casilla_adyacente=[posicion[0],posicion[1]-1]
		return casilla_adyacente
	elif direccion=="R":
		casilla_adyacente=[posicion[0]+1,posicion[1]]
		return casilla_adyacente
	elif direccion=="L":
		casilla_adyacente=[posicion[0]-1,posicion[1]]
		return casilla_adyacente
	elif direccion=="UR":
		casilla_adyacente=[posicion[0]+1,posicion[1]+1]
		return casilla_adyacente
	elif direccion=="UL":
		casilla_adyacente=[posicion[0]-1,posicion[1]+1]
		return casilla_adyacente
	elif direccion=="DR":
		casilla_adyacente=[posicion[0]+1,posicion[1]-1]
		return casilla_adyacente
	elif direccion=="DL":
		casilla_adyacente=[posicion[0]-1,posicion[1]-1]
		return casilla_adyacente
	else:
		return "esa direccion no es valida"

class casilla(object):
	"""docstring for casilla"""
	def __init__(self, nombre, posicion, ocupacion):
		super(casilla, self).__init__()
		self.nombre = nombre
		self.posicion =posicion
		se
		self.ocupacion = ocupacion

	def casilla_adyacente(self,direccion):
		''' resive un objeto casilla una direccion y devuelve la posicion de la caslla adyacente'''
		casilla_adyacente=[]
		
		if direccion=="U":
			casilla_adyacente=[self.posicion[0],self.posicion[1]+1]
			return casilla_adyacente
		elif direccion=="D":
			casilla_adyacente=[self.posicion[0],self.posicion[1]-1]
			return casilla_adyacente
		elif direccion=="R":
			casilla_adyacente=[self.posicion[0]+1,self.posicion[1]]
			return casilla_adyacente
		elif direccion=="L":
			casilla_adyacente=[self.posicion[0]-1,self.posicion[1]]
			return casilla_adyacente
		elif direccion=="UR":
			casilla_adyacente=[self.posicion[0]+1,self.posicion[1]+1]
			return casilla_adyacente
		elif direccion=="UL":
			casilla_adyacente=[self.posicion[0]-1,self.posicion[1]+1]
			return casilla_adyacente
		elif direccion=="DR":
			casilla_adyacente=[self.posicion[0]+1,self.posicion[1]-1]
			return casilla_adyacente
		elif direccion=="DL":
			casilla_adyacente=[self.posicion[0]-1,self.posicion[1]-1]
			return casilla_adyacente
		else:
			return "esa direccion no es valida"


			
casillas_como_objetos=[]
casillas_como_objetos+=casillas_nombres
for i in lista_1_al_n(64):
	casillas_como_objetos[i-1]=casilla(casillas_como_objetos[i-1],casillas[i-1],[])



class ficha(object):
	def __init__(self, color, posicion):
		self.color = color
		self.posicion = posicion

	def posibles_jugadas(self):
		...		
class rey(ficha):
	def __init__(self):
		super(self).__init__()
	def posibles_jugadas(self):
		pass



class tablero(object):
	def __init__(self):
		self.casillas={}
		self.fichas={}
		dic_nl={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
		dic_ln={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}


		casillas=[]
		for m in lista_1_al_n(8): 
			for n in lista_1_al_n(8):
				casillas.append([m,n])
		casillas_posicion=[]
		casillas_posicion+=casillas


		casillasLetra=[]
		for m in lista_1_al_n(8): 
			for n in lista_1_al_n(8):
				casillasLetra.append([dic_nl[m],n])
		casillas_nombres=[]
		for i in casillasLetra:
			casillas_nombres.append(str(i[0])+str(i[1]))
		
		self.agregar_casillas(ldldl)



	def agregar_casillas(self,lista_nombre,lista_casilla):
		'''toma una lista de casillas (obj) y una lista de nombres (str como h7) y los asigna respectivamente en un diccionario'''
		for i in lista_1_al_n(len(lista_nombre)):
			self.casillas[lista_nombre[i-1]]=lista_casilla[i-1]

	def mostrar_casillas(self):
		for i in casillas_nombres:
			print(self.casillas[i].nombre, self.casillas[i].casilla, self.casillas[i].ocupacion)
	def mostrar_casilla(self, nombre):
		print(self.casillas[nombre].nombre, self.casillas[nombre].casilla, self.casillas[nombre].ocupacion)

	def revisar_si_casilla_esta_en_tablero(self, casilla):
		'''recibe objeto casilla devuelve True o False'''
		for i in self.casillas.values():
			if casilla==i:
				return casilla==i
		for i in self.casillas.values():
			if casilla==i:
				return casilla==i
			else:
				return False
	def revisar_si_posicion_esta_en_tablero(self, posicion):
		posiciones=[]

		for i in self.casillas.values():
			posiciones.append(i.casilla)

		for i in posiciones:
			if posicion==i:
				return True
		for i in posiciones:
			if posicion==i:
				return True
			else:
				return False

	def casillas_adyacentes(self, casilla):
		casillas_adyacentes_posiciones=[]
		cascasillas_adyacentes_posiciones_en_tablero=[]
		casillas_adyacentes_nombres=[]
		casillas_adyacentes_objetos=[]

		for i in direcciones:
			casillas_adyacentes_posiciones.append(self.casillas[casilla].casilla_adyacente(i))

		for i in casillas_adyacentes_posiciones:
			if self.revisar_si_posicion_esta_en_tablero(i)==True:
				cascasillas_adyacentes_posiciones_en_tablero.append(i)		
		
		for i in cascasillas_adyacentes_posiciones_en_tablero:
			casillas_adyacentes_nombres.append(str(dic_nl[i[0]])+str(i[1]))

		for i in casillas_adyacentes_nombres:
			casillas_adyacentes_objetos.append(self.casillas[i])
		return casillas_adyacentes_objetos
		
	def cruz(self, casilla):
		casillas_cruz_posiciones=[]
		cascasillas_cruz_posiciones_en_tablero=[]
		casillas_cruz_nombres=[]
		casillas_cruz_objetos=[]

		posicion_variable=[]
		posicion_variable+=self.casillas[casilla].casilla


		for i in ["U","D","L","R"]:
			T=0
			if self.revisar_si_posicion_esta_en_tablero(posicion_variable)==False:
						posicion_variable=[]
						print(posicion_variable)
						posicion_variable+=self.casillas[casilla].casilla
						print(posicion_variable)

			while self.revisar_si_posicion_esta_en_tablero(posicion_variable)==True and T<100:
				posicion_variable=casilla_adyacente_posicion_posicion(posicion_variable,i)
				if self.revisar_si_posicion_esta_en_tablero(posicion_variable)==True:
					cascasillas_cruz_posiciones_en_tablero.append(casilla_adyacente_posicion_posicion(posicion_variable,i))
				
				T+=1
				print(posicion_variable)
				print(cascasillas_cruz_posiciones_en_tablero)



		for i in cascasillas_cruz_posiciones_en_tablero:
			casillas_cruz_nombres.append(str(dic_nl[i[0]])+str(i[1]))

		for i in casillas_cruz_nombres:
			casillas_cruz_objetos.append(self.casillas[i])
		return casillas_cruz_objetos


	def equis(self, casilla):
		pass
	def circulo_caballo(self, casilla):
		pass














