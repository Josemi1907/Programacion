lista = []
numero = int(input("Dime un numero: "))
suma = 0

while numero > 7 :
    numero = int(input("Numero invalido, vuelva a repetir: "))

while numero <= 7 :
    lista.append (numero)
    suma = suma + numero
    print(numero)
    numero = numero + 1

print(lista)
print("suma: ", suma)