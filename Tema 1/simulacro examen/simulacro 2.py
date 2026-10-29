lista = []
numero = 1
creciente = True
decreciente = True
contador = 0

while numero != 0 :
    numero = int(input("Dime un numero: "))
    if numero != 0 :
        lista.append (numero)

for i in range(0, len(lista) - 1):
    if lista[i] > lista[i + 1]:
        creciente = False
    if lista[i] < lista[i + 1]:
        decreciente = False
        
    contador = contador + lista[i]

media = contador / len(lista)

print (lista)
if creciente:
    print("creciente")

elif decreciente:
    print("decreciente")

else:
    print("desordenados")

print ("la media de la lista es:", media)
print("se han introducido:", len(lista)+1, "numeros")
print ("FIN")