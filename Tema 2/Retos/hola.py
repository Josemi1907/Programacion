titulos = ["Amanecer", "Lluvia", "Kilómetro 0", "Faro"]
duraciones = [210, 185, 240, 200]

cancion = False
titulo = []
segundos = []
añadir = input ("Dime una cancion: ").lower()
añadir2 = int(input("Dime los segundos que dura: "))
if añadir.lower() in titulos.lower() :
    cancion = True
    titulo.append (añadir)
    titulos.append (añadir)
    duraciones.append (añadir2)
    segundos.append (añadir2)
    print ("Cancion añadida")

else:
    print ("Ya existe una cancion con ese titulo")