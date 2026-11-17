import libreria

cad = input("Dime un nombre ")
libreria.miFuncion(cad)

num = int(input ("Dame un número: "))
res = libreria.isPar(num)
if res:
    print("Es par")

else :
    print ("Es impar")