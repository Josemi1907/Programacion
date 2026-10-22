lista = []
listaInversa = []
resta = 0
print("introduce 10 numero")
while len(lista) <10:
    numero = int(input())
    lista.append(numero)

while len(listaInversa ) <10 :
    inverso = (lista[len(lista)-1] ) - resta
    listaInversa.append (inverso)
    resta = resta + 1

print(lista)
print (listaInversa)
   