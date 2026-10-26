lista = []

while len (lista) < 15 :
    numero = int(input())
    lista.append (numero)

print (lista)
ultimo = lista[len(lista)-1]

for i in range (14, 0, -1) :
    lista [i] = lista [i -1]

lista [0] = ultimo
print (lista)

