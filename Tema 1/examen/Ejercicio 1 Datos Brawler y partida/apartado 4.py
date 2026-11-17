fin = False
brawler = False

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
        brawler = True
        if rareza == "C" or rareza == "c" :
            rareza = "Comun"

        if rareza == "R" or rareza == "r" :
            rareza = "Rara"

        if rareza == "E" or rareza == "e" :
            rareza = "Epico"

        if rareza == "L" or rareza == "l" :
            rareza = "Legendario"
        
        print ("Registrandos los datos del brawler:", nombre)

    if numero == 2 :
        trofeos_ganados = trofeos
        modo_juego = input("Dime el moodo de juego (G (Atrapagemas), B (Balon Brawl), N (Noqueo), S (Supervivencia))")
        if modo_juego == "G" or modo_juego == "B" or modo_juego == "N" or modo_juego == "g" or modo_juego == "b" or modo_juego == "n"  :
            resultado = input ("¿Cual ha sido el resultado? (V (Victoria), D (Derrota), E (Empate)): ")
            if resultado == "V" or resultado == "v":
                trofeos = trofeos + 10

            if resultado == "D" or resultado == "d":
                trofeos = trofeos - 5

        if modo_juego == "S" or modo_juego == "s":
            posicion = int(input ("¿En que posicion has quedado?(del 1 al 10):"))
            match posicion :
                case 1 :
                    trofeos = trofeos + 10
                case 2 :
                    trofeos = trofeos + 8
                case 3 :
                    trofeos = trofeos + 6
                case 4 :
                    trofeos = trofeos + 4
                case 5 :
                    trofeos = trofeos + 2
                case 6 :
                    trofeos = trofeos + 0
                case 7 :
                    trofeos = trofeos - 2
                case 8 :
                    trofeos = trofeos - 4
                case 9 :
                    trofeos = trofeos - 5
                case 10 :
                    trofeos = trofeos - 6

        if trofeos < 0 :
            trofeos = 0
        trofeos_ganados = trofeos - trofeos_ganados
        partidas = partidas + 1
        print ("El Brawler", nombre, "ha conseguido", trofeos_ganados, "en esta partida, quedandose su total de trofeos a:", trofeos)
        print ("Registrando")

    if numero == 3 :
        if brawler == True :
            print ("Resumiendo")
            print ("Brawler:", nombre, "(", rareza, ")")
            print ("Partidas registradad:", partidas)
            print ("Trofeos alcanzados:", trofeos)

        else:
            print("Primero debes guardar los datos del brawler")

    if numero == 4 :
        fin = True
        print ("Fin del programa")