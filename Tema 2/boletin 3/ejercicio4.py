lista = []
def numerosLista (lista):
    num = int(input("Dime cuantos numeros tendra la lista: "))
    for i in range (num):
        num2 = int(input("Dime numeros: "))
        lista.append (num2)

def estaOrdenadaAscendentemente (lista):
    numerosLista(lista)
    print (lista)
    asc = True
    i = 0
    while asc and i < len(lista) :
        if lista[i] > lista[i +1]:
            asc = False

        else:
            i = i + 1

    return asc

print(estaOrdenadaAscendentemente(lista))