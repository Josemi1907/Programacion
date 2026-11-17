texto = input("Escrbe un texto: ")
def ConvertirEspaciado (texto):
    for i in range (len(texto)):
        espacio = ""
        espacio = espacio + texto [i] + " "

    return (espacio)

resultado = ConvertirEspaciado(texto)
print(resultado)