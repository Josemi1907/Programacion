cadena = input("Dime una cadena: ")
subcadena = input ("Dime una subcadena: ")
coincide = True
if len(subcadena) > len(cadena):
        coincide = False

else:
    for i in range (len(subcadena)) :
        if  cadena [-len(subcadena) +i] != subcadena[i] :
            coincide = False

if coincide:
    print("finaliza con subcadena")

else:
    print("No termina por subcadena")