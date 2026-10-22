import random
lista1 = []
cuadrado = []
cubo = []
listaColumna = []
x = 0

while len(lista1) <20:
    aleatorio = random.randint (0,100)
    lista1.append(aleatorio)
    numeroCuadrado = aleatorio ** 2
    cuadrado.append(numeroCuadrado)
    numeroCubo = aleatorio ** 3
    cubo.append(numeroCubo)
    listaColumna.append ([lista1[x], cuadrado[x], cubo[x]])
    print (listaColumna[x])
    x = x + 1
    
