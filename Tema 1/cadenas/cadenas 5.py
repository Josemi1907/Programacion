cadena = input("Dime una cadena: ")
subcadena = input ("Dime una subcadena: ")
coincide = True

if len(subcadena) > len(cadena):
    coincide = False

else:
    for i in range (len(subcadena)) :
        if  cadena[i] != subcadena[i] :
            coincide = False
    

if coincide:
    print("empieza con subcadena")

else:
    print("No empieza por subcadena")