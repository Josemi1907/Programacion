Brawler1= []
Brawler2 = []
turno_personaje1 = 0
turno_personaje2 = 0

for i in range (1, 3):
    if i == 1 :
        nombre = input("Dime el nombre del brawler: ")
        tipo = input("Dime si es tanque o normal (T o N): ")
        vida = int(input("Dime la vida del brawler"))
        daño = int(input("Dime el daño de ataque del brawler"))
        if tipo == "t" or tipo == "T":
            Brawler1.append(nombre)
            Brawler1.append("Tanque")
            Brawler1.append(vida)
            Brawler1.append(daño)

        elif tipo == "n" or tipo == "N" :
            Brawler1.append(nombre)
            Brawler1.append("Normal")
            Brawler1.append(vida)
            Brawler1.append(daño)

    if i == 2 :
            nombre = input("Dime el nombre del brawler: ")
            tipo = input("Dime si es tanque o normal (T o N): ")
            vida = int(input("Dime la vida del brawler"))
            daño = int(input("Dime el daño de ataque del brawler"))
            if tipo == "t" or tipo == "T":
                Brawler2.append(nombre)
                Brawler2.append("Tanque")
                Brawler2.append(vida)
                Brawler2.append(daño)
    
            elif tipo == "n" or tipo == "N" :
                Brawler2.append(nombre)
                Brawler2.append("Normal")
                Brawler2.append(vida)
                Brawler2.append(daño)

print ("Brawler 1:", Brawler1[0], "(", Brawler1[1], ")", "- Vida:", Brawler1[2], "- Daño:", Brawler1[3])
print ("Brawler 2:", Brawler2[0], "(", Brawler2[1], ")", "- Vida:", Brawler2[2], "- Daño:", Brawler2[3])

while Brawler1[2] >= 0 and Brawler2[2] >= 0 :
    if Brawler1[1] == "Tanque" and Brawler1[2] >= 0:
        daño = Brawler2[3] * 80 / 100
        Brawler1[2] = Brawler1[2] - daño
        turno_personaje1 = turno_personaje1 + 1

    elif Brawler1[1] == "Normal" and Brawler1[2] >= 0 :
        daño = Brawler2[3]
        Brawler1[2] = Brawler1[2] - daño
        turno_personaje1 = turno_personaje1 + 1

    if Brawler2[1] == "Tanque" and Brawler2[2] >= 0:
        daño = Brawler1[3] * 80 / 100
        Brawler2[2] = Brawler1[2] - daño
        turno_personaje2 = turno_personaje2 + 1
    
    elif  Brawler2[1] == "Normal" and Brawler2[2] >= 0:
        daño = Brawler1[3]
        Brawler2[2] = Brawler2[2] - daño
        turno_personaje2 = turno_personaje2 + 1

print (Brawler1[0], "necesita", turno_personaje1, "ataques para derrotar a", Brawler2[0])
print (Brawler2[0], "necesita", turno_personaje2, "ataques para derrotar a", Brawler1[0])
if turno_personaje1 > turno_personaje2 :
    print ("Favorito:", Brawler1[0])

if turno_personaje1 < turno_personaje2 :
    print ("Favorito:", Brawler2[0])

if turno_personaje1 == turno_personaje2 :
    print ("Duelo igualado")