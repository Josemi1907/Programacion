cadena = input("Dame una cadena con 4 caracteres: ")
longitud_cadena = len(cadena)
def calcula_subcadena (cadena, posInicio, posFin):
    print("llamo a la subcadena")
    subcadena = cadena [posInicio: posFin + 1]
    print(subcadena)

while longitud_cadena != 4:
    cadena = cadena = input("Dame una cadena con 4 caracteres")
    longitud_cadena = len(cadena)

numero = int(input("Introduce un numero: "))

if numero %2 == 0 :
    calcula_subcadena (cadena, 2, 4)

elif numero %3 == 0 :
    calcula_subcadena (cadena, 1, 2)

elif numero %7 == 0 :
    calcula_subcadena (cadena, 0, 3)