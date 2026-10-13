suma = 0
total = 0
print ("Introduce numero")
n = int(input ())

if n > 0:

    for suma in range (1, n +1) :
        print (total, "+", suma)
        total = total + suma
        print (total)
        suma = suma + 1

else :
    print ("Numero erroneo, vuelva a introducir un numero")