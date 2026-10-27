numero = int(input("Dime un numero: "))
elevado = int(input("Dime un numero para elevar el anterior: "))

while numero < 0 and elevado < 0 :
    print("Error, vuelva a repetir los numero")
    numero = int(input("Dime un numero: "))
    elevado = int(input("Dime un numero para elevar el anterior: "))

resultado = numero

for i in range (1, elevado):
    resultado = resultado * numero

print (resultado)