lista = ["hola", "adios", "hola", "perro", "gato", "perro"]
def sinCadenasRepetidas (lista) :
    lista2 = []
    for palabra in lista:
        if palabra not in lista2:
            lista2.append(palabra)

    return lista2

def listaCadena(lista):
    resultado = sinCadenasRepetidas (lista)

    print("Lista original:", lista)
    print("Lista sin repetidas:", resultado)

listaCadena (lista)