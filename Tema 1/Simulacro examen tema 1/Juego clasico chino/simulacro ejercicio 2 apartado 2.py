import random
numero_humano = 6
numero_maquina = random.randint (0, 5)
par = False
impar = False

while numero_humano != numero_maquina :
    numero_humano = int(input("¿Cuantas piedras quieres enseñar (0 al 5): "))
    while numero_humano < 0 or numero_humano > 5 :
        numero_humano = int(input("Numero no valido. ¿Cuantas piedras quieres enseñar (0 al 5): "))

    numero_maquina = random.randint (0, 5)
    suma = numero_humano + numero_maquina

    respuesta = input ("¿Par o impar? (P o I): ")

    if respuesta == "p" or respuesta == "P" :
        if suma % 2 == 0 :
            par = True
            impar = False

        else:
            par = False

    if respuesta == "i" or respuesta == "I" :
        if suma % 2 != 0 :
            impar = True
            par = False

        else:
            impar = False
            
    print ("Maquina ha sacado", numero_maquina)
    print ("La suma es", suma)
    if par or impar:
        print ("Humano ha ganado la ronda")

    else :
        print ("Maquina ha ganado la ronda")

print ("FIN")