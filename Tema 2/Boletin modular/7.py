def calcularMaxMin(lista):
    max = lista [0]
    for i in range (1, len(lista)):
        if lista[i] > max :
            max = lista [i]

    min = lista [0]
    for i in range (1, len(lista)):
        if lista[i] < min :
            min = lista [i]

    return max, min

numeros = []
for i in range(10):
    num = int(input("Introduce un número: "))
    numeros.append(num)

maximo, minimo = calcularMaxMin(numeros)
print("El máximo es:", maximo)
print("El mínimo es:", minimo)