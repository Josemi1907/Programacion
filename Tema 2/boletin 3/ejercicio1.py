numeroPide = int(input("Dime cuantos numeros desea introducir: "))
lista = []

def guardoLista (lista):
    num = int(input("Dime numeros: "))
    lista.append (num)
    return lista

def listaInversa (lista):
    reversa = []
    for i in range (len(lista)) :
        num = lista[-1 - i]
        reversa.append (num)
    return reversa

for i in range (numeroPide):
    lista = guardoLista (lista)

listaIn = listaInversa (lista)
print (listaIn)