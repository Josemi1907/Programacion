#problema hecho con if
numero = int(input ())
print (numero)

if numero == 0 :
    valorNumero = "CERO"

elif numero == 1 :
    valorNumero = "UNO"

elif numero == 2 :
    valorNumero = "DOS"

else :
    valorNumero = "OTRAS"

print (valorNumero)

#problema hecho con match
numero = int(input ())
print (numero)
match numero:
    case 0:
        valorNumero = "CERO"
    case 1:
        valorNumero = "UNO"
    case 2:
        valorNumero = "DOS"
    case _:
        valorNumero = "OTRAS"

print (valorNumero)