print("Dime 15 numeros para las lista")
lista = []

while len (lista) < 15 :
    numero = int(input())
    lista.append (numero)

print("Dime un numero para retroceder el numero de veces la lista")
n = int(input())

while n >= len (lista) or n < 0 :
    numero = int(input("Vuelve a darme un numero"))

print (lista)
sublista = lista[len(lista)-n : len(lista)]
sublista2 = lista[0:len(lista)-n]

listaSalida = sublista + sublista2
print (listaSalida)