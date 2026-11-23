lista = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

def recorreLista (lista):
    for i in range (len(lista)) :
        print (lista[i])

def listaComienzaFinal (lista) :
    for i in range (len(lista)) :
        print (lista[-1 -i])

def listaInvertida (lista):
    for i in range (len(lista)) :
        for x in range (len(lista[i])):
            print (lista[i][-1 -x])

fila = recorreLista (lista)
print ("==================")
filaRevez = listaComienzaFinal (lista)
print ("==================")
filaInvertida = listaInvertida (lista)