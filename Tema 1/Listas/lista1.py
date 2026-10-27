lista = ["elefante", "perro", "gato"]
print ("Diga un animal")
animal = input()
encontrado = False
posicion = 0

while not encontrado and posicion < len(lista) :
    if lista [posicion] == animal :
        encontrado = True
    posicion = posicion + 1

if encontrado == False :
     print ("El", animal, "no esta en la lista")

else:
    print ("El", animal, "si esta en la lista")