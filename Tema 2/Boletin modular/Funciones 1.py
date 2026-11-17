def obtieneYValidaDatosDeEntrada () :
    numero = int(input("Dime un numero: "))
    while numero < 0 :
        numero = int(input("Dime un numero: "))

    return (numero)

positivo = obtieneYValidaDatosDeEntrada()

print (positivo)