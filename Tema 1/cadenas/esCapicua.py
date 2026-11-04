numero = input ("Dime un numero: ")
capicua = True

for i in range (len(numero)) :
    if numero [i] == numero[len(numero) -1 -i] and capicua == True:
        capicua = True

    else :
        capicua = False

if capicua:
    print ("Es capicua")

else :
    print ("No es capicua")

