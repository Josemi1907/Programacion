año = int(input("Dime un año: "))
bisiesto = False

while año >= 0 :

    if año % 4 == 0 :
        bisiesto = True
    else :
        bisiesto = False

    if año % 100 == 0 :
        bisiesto = False

    if año % 400 == 0 :
        bisiesto = True


    if bisiesto == True :
        print ("El año es bisiesto")

    else:
        print("El año no es bisiesto")

    año = int(input("Dime un año: "))

print ("Fin")
    