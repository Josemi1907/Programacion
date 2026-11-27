titulos = ['Amanecer', 'Lluvia', 'Kilómetro 0', 'Faro']
duraciones = [210, 185, 240, 200]
salir = False

def menu (titulos, duraciones, salir) :
    print ("============== MENU ============")
    print ("Titulos iniciales:", titulos)
    print ("Duraciones iniciales:", duraciones)
    print ("Opcion A. Añadir canción")
    print ("Opcion B. Duración total)")
    print ("Opcion C. Canciones que caben en un tiempo ")
    print ("Opcion Z. Salir")
    correcto = eleccionCorrecta ()
    match correcto:
        case "a" :
            añadido = añadirCancion(titulos, duraciones)
        
        #case "b" :
            #duracionT = duracionTotal (duraciones)
        
        #case "c" :
            
    
        case "z" :
                salir = True
    
    return salir    

def eleccionCorrecta () :
    good = False
    while good == False :
        eleccion = input("->").lower()
        match eleccion:
            case "a" | "b" | "c" | "z" :
                good = True
            case _:
                print ("Eleccion incorrecta, vuelva a decir")
        return eleccion

def añadirCancion (titulos, duraciones) :  
    cancion = False
    titulo = []
    segundos = []
    añadir = input ("Dime una cancion: ")
    añadir2 = input("Dime los segundos que dura: ")
    if añadir not in titulos :
        cancion = True
        titulo.append (añadir)
        titulos.append (añadir)
        duraciones.append (añadir2)
        segundos.append (añadir2)
        print ("Cancion añadida")

    else:
        print ("Ya existe una cancion con ese titulo")
        
    return (cancion)

#def duracionTotal (duraciones) :
    for i in range (len(duraciones)):
        minutos = duraciones[i] / 60

salida = menu (titulos, duraciones, salir)
while salida == False :
    salida = menu (titulos, duraciones, salir)