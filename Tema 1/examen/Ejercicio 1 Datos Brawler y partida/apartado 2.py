fin = False

while fin == False :
    print ("=========== BRAWLS STARTS REGISTRO ===========")
    print ("1. Guarda datos del brawler")
    print ("2. Registra partida")
    print ("3. Mostrar resumen")
    print ("4. Terminar programa")
    print ("Selecciona una opcion")
    numero = int(input("-> "))

    if numero == 1 :
        nombre = input ("Dime el nombre del brawler: ")
        rareza = input ("Dime la rareza del brawler (C (Comun), R (Rara), E (Epico), L(Legendario)): ")
        trofeos = int (input ("Dime el numero de trofeos iniciales: "))
        partidas = 0
        if rareza == "C" or rareza == "c" :
            rareza = "Comun"

        if rareza == "R" or rareza == "r" :
            rareza = "Rara"

        if rareza == "E" or rareza == "r" :
            rareza = "Epico"

        if rareza == "L" or rareza == "l" :
            rareza = "Legendario"

        print ("Registrandos los datos del brawler:", nombre)

    if numero == 2 :
        print ("Registrando")

    if numero == 3 :
        print ("Resumiendo")

    if numero == 4 :
        fin = True
        print ("Fin del programa")