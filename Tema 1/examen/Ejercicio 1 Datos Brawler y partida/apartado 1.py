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
        print ("Guardando los datos del brawler")

    if numero == 2 :
        print ("Registrando")

    if numero == 3 :
        print ("Resumiendo")

    if numero == 4 :
        fin = True
        print ("Fin del programa")