def calculaMayoresQueNumero(lista, numero) :
    mayores = []
    for i in range (len(lista)) :
        if lista [i] > numero :
            mayores.append(lista[i])
    return (mayores)

listaMayores = calculaMayoresQueNumero([2,3,4,7, 9, 10 ,2], 5)

print (listaMayores)