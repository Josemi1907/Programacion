import random
innombrable = "Voldemort"
alumno = ""
numero = 0
casa = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw" ]
salida = False
total_alumnos = 0
Gryffindor = 0
Slytherin = 0
Hufflepuff = 0
Ravenclaw = 0

while salida == False :
    print ("===========================================")
    print("SOMBRERO SELECCIONADOR")
    print ("===========================================")
    print("1. Seleccionar casa para un alumno")
    print("2. Mostrar estadisticas")
    numero = int(input ("Elige una opcion. Si quieres salir del programa, escribe la opcion 1 y el nombre del personaje innobrable: "))

    if numero == 1 :
        alumno = input("Nombre del alumno: ")
        total_alumnos = total_alumnos + 1
        aleatorio = random.randint (1, 4)
        if alumno == innombrable :
            salida = True
        else:
            print ("Ejecutando y seleccionando casa")
            print("El sombreo dice que", alumno, "pertenece a", casa[aleatorio -1])

            if casa[aleatorio -1] == "Gryffindor" :
                Gryffindor = Gryffindor + 1

            elif casa[aleatorio -1] == "Slytherin" :
                Slytherin = Slytherin + 1

            elif casa[aleatorio -1] == "Hufflepuff" :
                Hufflepuff = Hufflepuff + 1

            elif casa[aleatorio -1] == "Ravenclaw" :
                Ravenclaw = Ravenclaw + 1

    if numero == 2 :
        if total_alumnos > 0 :
            print ("Ejecutando y mostrando estadisticas")
            print ("Total de alumnos:", total_alumnos)
            print ("Gryffindor:", Gryffindor)
            print ("Slytherin", Slytherin)
            print ("Hufflepuff", Hufflepuff)
            print ("Ravenclaw", Ravenclaw)
        else:
            print("Todavia no hay estadisticas")

    while numero != 1 and numero != 2:
        numero = int(input ("Opcion incorrecta. Elige una opcion. Si quieres salir del programa, escribe la opcion 1 y el nombre del personaje innobrable: "))

print("Apparition, transportame a otro sitio")