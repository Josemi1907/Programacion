print("¿tiene premium? S/N")
premium = input()
print ("¿Cuanto minutos lleva de reproduccion?")
tiempoDeReproduccion = int(input())

if premium == "N" and tiempoDeReproduccion >= 30 :
    print ("Anuncio")