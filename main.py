import mochila, objetoMochila
import csv

def algoritmoMochila(listaObjetos, listaMochilas):
	listaActual = []
	for i,mochila in enumerate(listaMochilas):
		print("%s:" % i)
		listaActual = list(listaObjetos)

		for objeto in listaActual:
			if mochila.addObjeto(objeto):
				listaObjetos.remove(objeto)

		print("",mochila.objetos, "total:",mochila.pesoActual)
	print("Restante:\n",listaObjetos)


listaObjetos = []
with open('objects.csv','r') as f:
	reader = csv.reader(f)
	for row in reader:
		aux = objetoMochila.ObjetoMochila(row[0],row[1],row[2])
		listaObjetos.append(aux)
	listaObjetos.sort(reverse=True)

mochila1 = mochila.Mochila(15)
mochila2 = mochila.Mochila(15)

listaMochilas1 = [mochila1,mochila2]

algoritmoMochila(listaObjetos,listaMochilas1)
