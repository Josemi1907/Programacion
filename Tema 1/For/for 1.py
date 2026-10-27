print ("Introduzca un numero")
numeroLeido = int (input())
i = 0

if numeroLeido > 0 :
    for i in range (1, numeroLeido) :
        print (i)
        i = i +1
        
else :
    print ("Numero erroneo, vuelva a introducir un numero")