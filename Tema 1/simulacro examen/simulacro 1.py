lista = []
while len(lista) < 3 :
    numero = int(input("dime un numero"))
    lista.append (numero)

while lista [0] != 0 or lista[1] != 0 or lista [2] != 0 :
    if  lista [0] != 0 :
        lista [0] = lista [0] - 1

    if lista [1] != 0 :
        lista [1] = lista [1] - 1

    if lista [2] != 0 :
        lista [2] = lista [2] - 1

    print (lista)