def estaOrdenadaAscendentemente (lista):
    ascendente = True
    i = 0
    while ascendente and i < len(lista) -1 :
        if lista [i] > lista[i + 1] :
         ascendente = False

        else:
           i = i+1
    return ascendente

def cargaLista():
    lista = []
    num = 0
    while num >= 0 and num <= 9 :
            num = int(input("Dime numeros: "))
            lista.append (num)

    return lista

lista = cargaLista()
resultado = estaOrdenadaAscendentemente(lista)
print(resultado)