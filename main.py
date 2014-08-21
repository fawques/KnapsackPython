import mochila, objetoMochila

def algoritmoMochila(listaObjetos, listaMochilas):
	listaObjetos.sort(reverse=True)
	listaActual = []
	for i,mochila in enumerate(listaMochilas):
		print("%s:" % i)
		listaActual = list(listaObjetos)

		for objeto in listaActual:
			if mochila.addObjeto(objeto):
				listaObjetos.remove(objeto)

		print("",mochila.objetos)
	print("Restante:\n",listaObjetos)


# sacar del archivo los objetos pendientes
obj1 = objetoMochila.ObjetoMochila("obj1",100,10)
obj2 = objetoMochila.ObjetoMochila("obj2",100,5)
obj3 = objetoMochila.ObjetoMochila("obj3",1000,15)
obj4 = objetoMochila.ObjetoMochila("obj4",1000,5)
obj5 = objetoMochila.ObjetoMochila("obj5",1,5)

mochila1 = mochila.Mochila(15)
mochila2 = mochila.Mochila(15)

listaObjetos1 = [obj1,obj2,obj3,obj4,obj5]
listaMochilas1 = [mochila1,mochila2]

algoritmoMochila(listaObjetos1,listaMochilas1)
