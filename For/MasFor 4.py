print ("Dime un numero")
numero = 6

filaFP = numero * "*"
filaintermedia = "*" + (numero - 2)* " " + "*"

for numFilas in range (0, numero +1) :
    if numFilas == 0 or numFilas == numero:
        print (filaFP)
    else:
        print (filaintermedia)