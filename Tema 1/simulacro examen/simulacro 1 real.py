lista = []
for i in range (0, 3) :
    numero = int(input("Dime un numero: "))
    lista.append (numero)

print (lista)

while lista != [0, 0, 0] :
    if lista [0] < lista [1] < lista [2] :
        print ("Creciente")

    elif lista [0] > lista [1] > lista [2] :
        print ("Decreciente")

    else: 
        print ("Desordenado")

    print ("=========================================")

    for i in range (0, 3) :
        numero = int(input("Dime un numero: "))
        lista [i] = numero

    print (lista)

print("fin")