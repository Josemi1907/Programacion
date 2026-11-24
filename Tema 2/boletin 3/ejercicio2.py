lista = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
matriz = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

def recorreLista (lista):
    for i in range (len(lista)) :
        print (lista[i])

def listaComienzaFinal (lista) :
    for i in range (len(lista)) :
        print (lista[-1 -i])

def listaInvertida (lista):
    for filaIn in lista :
        print (filaIn[::-1])

def imprimeMatrizInvertida (matriz):
    for i in range (len(matriz)) :
        print (matriz[i], matriz[len(matriz)-1-i][::-1])

def dameColumna (matriz):
    for i in range (len(matriz)) :
        columna = []
        for x in range (len(matriz)) :
            columna.append(matriz[x][i])
        print (columna)

def columnaNumeros (lista):
    dameColumna(lista)

fila = recorreLista (lista)
print ("==================")
filaRevez = listaComienzaFinal (lista)
print ("==================")
filaInvertida = listaInvertida (lista)
print ("==================")
matrizIn = imprimeMatrizInvertida (matriz)
print ("==================")
columna = dameColumna (matriz)
print ("==================")
columnaNum = columnaNumeros (lista)