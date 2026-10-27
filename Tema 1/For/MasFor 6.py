print ("Dime un numero")
numero = 6

filaFP = "*" + (numero - 2)* "#" + "*"
filaintermedia = numero * "*"

for numFilas in range (0, numero) :
    if numFilas == 0 or numFilas == numero - 1:
        print (filaFP)
    else:
        print (filaintermedia)