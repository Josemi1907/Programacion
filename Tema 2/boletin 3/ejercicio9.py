import random
lista = []
salir = False

def numeroAleatorio (lista) :
    for i in range (100) :
        num = random.randint (0, 1000)
        lista.append (num)
    return lista

def menu (salir):
    numeroAleatorio(lista)
    print ("============== MENU ============")
    print ("Devuelve el mayor (a)")
    print ("Devuelve el menor (b)")
    print ("Devuelve la suma de todos (c)")
    print ("Devuelve la media (d)")
    print ("Sustituye un numero de la lista por otro (e)")
    print ("Mostrar todos los numeros (f)")
    print ("Salir de menu (g)")
    correcto = eleccionCorrecta ()
    match correcto:
        case "a" :
            mayor = numeroMayor (lista)     
            print(mayor)
    
        case "b" :
            menor = numeroMenor (lista)
            print(menor)
    
        case "c" :
            sumaTotal = numeroSuma(lista)
            print(sumaTotal)
    
        case "d" :
            media = mediaNumero(lista)
            print (media)

        case "e" :
            sustituir = numeroSustituir (lista)
            print(lista[sustituir])

        case "f" :
            print (lista)

        case "g" :
            salir = True

    return salir


def eleccionCorrecta () :
    good = False
    while good == False :
        eleccion = input("->").lower()
        match eleccion:
            case "a" | "b" | "c" | "d" | "e" | "f" | "g":
                good = True
            case _:
                print ("Eleccion incorrecta, vuelva a decir")
    return eleccion

def numeroMayor (lista):
    mayorNum = lista [0]
    for i in range (len(lista )) :
        if lista[i] > mayorNum :
            mayorNum = lista[i]
    return mayorNum

def numeroMenor (lista):
    menorNum = lista [0]
    for i in range (len(lista)) :
        if lista[i] < menorNum:
            menorNum = lista[i]
    return menorNum

def numeroSuma (lista):
    suma = 0
    for i in range (len(lista)) :
        suma = suma + lista [i]
    return suma

def mediaNumero (lista) :
    suma = 0
    for i in range (len(lista)):
        suma = suma + lista [i]
    mediaNum = suma / len(lista)
    return mediaNum

def numeroSustituir (lista) :
    valorLista = int(input("Dime que elemento quieres sutituir(0 al 99): "))
    while valorLista < 0 or valorLista > 99 :
        valorLista = int(input("Incorrecto, Dime que elemento quieres sutituir(0 al 100): "))
    numeroAñadido = int(input("Dime que numero vas a añadir: "))
    lista [valorLista] = numeroAñadido
    return valorLista

salida = menu (salir)
while salida == False :
    salida = menu (salir)