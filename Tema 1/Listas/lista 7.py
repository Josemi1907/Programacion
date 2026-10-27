lista = []

while len (lista) < 10 :
    numero = int(input())
    lista.append (numero)

minimo = lista [0]
maximo = lista [0]

for i in range (1, len(lista)) :
    if lista[i] < minimo :
        minimo = lista [i]

    if lista[i] > maximo:
        maximo = lista [i]


print (lista)
print ("maximo:", maximo)
print ("minimo:", minimo)