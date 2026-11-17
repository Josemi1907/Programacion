def calcularMax (listaNum):
    max = listaNum [0]
    for i in range (1, len(listaNum)):
        if listaNum[i] > max :
            max = listaNum [i]

    return (max)

def calculaLista ():
    lista = []
    for i in range (10):
        num = int (input("Dime un numero: "))
        lista.append(num)
        maximo = calcularMax(lista)
        print (maximo)
    return (lista)

ListaCalculada = calculaLista ()
