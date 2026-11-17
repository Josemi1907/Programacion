import random
numero_humano = int(input("¿Cuantas piedras quieres enseñar (0 al 5): "))
numero_maquina = random.randint (0, 5)
par = False
impar = False

while numero_humano < 0 or numero_humano > 5 :
    numero_humano = int(input("Numero no valido. ¿Cuantas piedras quieres enseñar (0 al 5): "))

respuesta = input ("¿Par o impar?(P o I): ")
suma = numero_humano + numero_maquina

if respuesta == "p" or respuesta == "P" :
    if suma % 2 == 0 :
        par = True

    else:
        par = False

elif respuesta == "i" or respuesta == "I" :
    if suma % 2 != 0 :
        impar = True

    else:
        impar = False

print (suma)
if par  or impar:
    print ("Humano ha ganado la ronda")

else :
    print ("Maquina ha ganado la ronda")