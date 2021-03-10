

class Nodo():
	def __init__(self,nombre,papas,hijos):
		self.papas = papas
		self.hijos = hijos
		self.nombre = nombre

	def agregar_hijos(self, L):
		self.hijos+=L
		for i in L:
			i.papas.append(self)

	def listar_hijos(self):
		hijos=[]
		for i in self.hijos:
			hijos.append(i.nombre)
		return hijos	

	def listar_papas(self):
		papas=[]
		for i in self.papas:
			papas.append(i.nombre)
		return papas



n1=Nodo("n1",[],[])
n2=Nodo("n2",[],[])
n3=Nodo("n3",[],[])
n4=Nodo("n4",[],[])

n1.agregar_hijos([n2,n3,n4])

print(n3.listar_papas())

print(n1.listar_hijos())

L=[1,5,"djd",[3,4]]

diccionario={3:4,5:6,"si":"ok","no":True}

print(diccionario["como"])




"""
https://realpython.com/python-metaclasses/
"""








