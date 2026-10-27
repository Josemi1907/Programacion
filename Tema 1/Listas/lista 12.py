import random
lista = []
impar = []

while len(lista) <20:
    aleatorio = random.randint (0,100)
    if aleatorio % 2 == 0 :
        lista.append(aleatorio)

    if aleatorio % 2 != 0 :
        impar.append(aleatorio)


print ("par", lista)
print ("impar", impar)
lista = lista + impar
print ("fusionado", lista)

