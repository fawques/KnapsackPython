class ComparableMixin(object):
    def _compare(self, other, method):
        try:
            return method(self._cmpkey(), other._cmpkey())
        except (AttributeError, TypeError):
            # _cmpkey not implemented, or return different type,
            # so I can't compare with "other".
            return NotImplemented

    def __lt__(self, other):
        return self._compare(other, lambda s,o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s,o: s <= o)

    def __eq__(self, other):
       return self._compare(other, lambda s,o: s == o)

    def __ge__(self, other):
        return self._compare(other, lambda s,o: s >= o)

    def __gt__(self, other):
        return self._compare(other, lambda s,o: s > o)

    def __ne__(self, other):
        return self._compare(other, lambda s,o: s != o)

class ObjetoMochila(ComparableMixin):
	"""Objeto para el algoritmo de la mochila.
	Guarda un peso, un valor y un nombre"""
	def __init__(self, nombre,valor,peso):
		self.nombre = nombre
		self.valor = float(valor)
		self.peso = float(peso)

	def _cmpkey(self):
		return self.valor/self.peso

	def __repr__(self):
		return "<%s - valor %s - peso %s>\n" % (self.nombre,self.valor,self.peso)


		