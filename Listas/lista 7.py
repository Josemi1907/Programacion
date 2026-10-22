lista = []
minimo = [0]
maximo = [0]

while len (lista) < 10 :
    numero = int(input())
    lista.append (numero)
    for i in range (1, len(lista)) :
        if lista[i] >= maximo[i]:
            maximo.append(numero)
        else:
            minimo.append(numero)


print (lista)
print ("maximo:", maximo)
print ("minimo:", minimo)