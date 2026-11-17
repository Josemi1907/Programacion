import random
numero_humano = 6
numero_maquina = random.randint (0, 5)
par = False
impar = False
partidas = 0
humano = 0
maquina = 0
Apuesta_Par = 0
Apuesta_Impar = 0

while numero_humano != numero_maquina :
    numero_humano = int(input("¿Cuantas piedras quieres enseñar (0 al 5): "))

    while numero_humano < 0 or numero_humano > 5 :
        numero_humano = int(input("Numero no valido. ¿Cuantas piedras quieres enseñar (0 al 5): "))

    numero_maquina = random.randint (0, 5)
    suma = numero_humano + numero_maquina

    respuesta = input ("¿Par o impar? (P o I): ")

    if respuesta == "p" or respuesta == "P" :
        Apuesta_Par = Apuesta_Par + 1

        if suma % 2 == 0 :
            par = True
            impar = False
            humano = humano + 1

        else:
            par = False
            maquina = maquina + 1

    if respuesta == "i" or respuesta == "I" :
        Apuesta_Impar = Apuesta_Impar + 1
        if suma % 2 != 0 :
            impar = True
            par = False
            humano = humano + 1

        else:
            impar = False
            maquina = maquina + 1
            
    print ("Maquina ha sacado", numero_maquina)
    print ("La suma es", suma)
    if par or impar:
        print ("Humano ha ganado la ronda")

    else :
        print ("Maquina ha ganado la ronda")

    partidas = partidas + 1

if Apuesta_Par > Apuesta_Impar:
    print ("El humano ha apostado mas por el Par con un total de", Apuesta_Par, "veces.")

if Apuesta_Par < Apuesta_Impar:
    print ("El humano ha apostado mas por el Impar con un total de", Apuesta_Impar, "veces.")

if Apuesta_Par == Apuesta_Impar:
    print("Ha sacado el humano la misma cantidad de veces par que impar")

print ("El humano ha ganado", humano, "partidas")
print ("La maquina ha ganado", maquina, "partidas")
print("Han jugado un total de", partidas, "en total")
print ("FIN")