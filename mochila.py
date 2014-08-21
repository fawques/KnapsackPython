class Mochila:
	"""Mochila para el algoritmo, guarda los objetos que caben en el peso máximo"""
	def __init__(self, pesoMaximo):
		self.pesoMaximo = pesoMaximo
		self.pesoActual = 0
		self.objetos = []
		
	def addObjeto(self,objeto):
		if self.pesoActual + objeto.peso <= self.pesoMaximo:
			self.pesoActual = self.pesoActual + objeto.peso
			self.objetos.append(objeto)
			return True
		else:
			return False

