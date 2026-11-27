def menu () :
    print ("============== MENU ============")
    print ("Devuelve la matriz de n x n (a)")
    print ("Devuelve matriz con los numeros alineados (b)")
    correcto = eleccionCorrecta ()
    crearTabla(correcto)
    return correcto      

def eleccionCorrecta () :
    good = False
    eleccion = input("->").lower()
    while good == False :
        if eleccion != "a" and  eleccion != "b":
            eleccion = input("->").lower()
        else:
            good = True

        return eleccion

def crearTabla (correcto) :
    lista = []
    n = int(input("dime un numero: " ))
    match correcto:
        case "a" :
            for i in range (n):
                lista = crearFilaPrimera (n, lista)
                print (lista[i])
    
        case "b" :
            mult = formulaMultiplicar (n)
    
    
def crearFilaPrimera (n, lista):
    mult = []
    for i in range (n):
        lista = []
        for x in range (n):
            lista.append ((i + 1) * (x + 1))
        mult.append(lista)
    return mult

def formulaMultiplicar (n):
    for i in range (10 + 1):
        multiplicado = i * n
        print (i, "x", n, "=", multiplicado)

    return multiplicado

menu ()