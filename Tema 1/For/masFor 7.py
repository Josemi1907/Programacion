print("Dime un numero")
numero = 5

filaFP = "*" + (numero - 2) * "#" + "*"
filaintermedia = "*@*@*"

for numFilas in range(0, numero):
    if numFilas == 0 or numFilas == numero - 1 or numFilas == 2:
        print(filaFP)
    else:
        print(filaintermedia)