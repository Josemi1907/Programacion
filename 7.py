def calcularMaxMin(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

numeros = []

for i in range(10):
    num = int(input("Introduce un número: "))
    numeros.append(num)

maximo, minimo = calcularMaxMin(numeros)

print("El máximo es:", maximo)
print("El mínimo es:", minimo)