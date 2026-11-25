lista = []
def menu(lista) :
    llamadaNumeros(lista)
    print ("============== MENU ============")
    print ("Devuelve la media (a)")
    print ("Devuelve cuántos son pares (b)")
    print ("Devuelve cuántos son negativos (c)")
    print ("Devuelve la suma de todos los números introducidos (d)")
    correcto = eleccionCorrecta ()
    match correcto:
        case "a" :
            media = mediaNumero(lista)
            print (media)

        case "b" :
            pares = paresNumero(lista)
            print (pares)

        case "c" :
            negativos = negativoNumeros(lista)
            print ("hay", negativos, "numeros negativos")

        case "d" :
            sumaTotal = sumaNumeros(lista)
            print (sumaTotal)

def llamadaNumeros (lista) :
    num = int(input("Dime numero: "))
    print ("Dime un total de", num, "numeros: ")
    for i in range (num):
        num2 = int(input("-> "))
        lista.append (num2)
    print (lista)
 
def eleccionCorrecta () :
    good = False
    eleccion = input("->").lower()
    while good == False :
        if eleccion != "a" and  eleccion != "b" and  eleccion != "c" and  eleccion != "d" :
            print ("Eleccion incorrecta, vuelva a decir")
            eleccion = input("->").lower()
        else:
            good = True

        return eleccion

def mediaNumero (lista) :
    suma = 0
    for i in range (len(lista)):
        suma = suma + lista [i]
    mediaNum = suma / len(lista)
    return mediaNum

def paresNumero (lista) :
    par = []
    for i in range (len(lista)) :
        if lista [i] % 2 == 0 :
            par.append (lista[i])
    return par

def negativoNumeros (lista) :
    total = 0
    for i in range (len(lista)) :
        if lista [i] < 0 :
            total = total + 1
    return total

def sumaNumeros (lista):
    suma = 0
    for i in range (len(lista)) :
        suma = suma + lista [i]
    return suma

#menu (lista)