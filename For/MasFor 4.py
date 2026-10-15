print("dime un numero")
numero = int(input())

for j in range (numero):
    cadena = ""
    segunda_cadena = ""
    for j in range (numero) :
        cadena = "*" + cadena

    for j in range (numero):
        if j == 0 or j == numero :
            segunda_cadena = segunda_cadena + "*"

        elif j != 0 or j != numero:
            segunda_cadena = segunda_cadena + " "
            
    print (cadena)
    print (segunda_cadena)