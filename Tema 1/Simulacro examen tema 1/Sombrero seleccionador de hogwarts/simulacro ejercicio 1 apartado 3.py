import random
innombrable = "Voldemort"
alumno = ""
numero = 0
casa = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw" ]
salida = False

while salida == False :
    print ("===========================================")
    print("SOMBRERO SELECCIONADOR")
    print ("===========================================")
    print("1. Seleccionar casa para un alumno")
    print("2. Mostrar estadisticas")
    numero = int(input ("Elige una opcion. Si quieres salir del programa, escribe la opcion 1 y el nombre del personaje innobrable: "))

    if numero == 1 :
        alumno = input("Nombre del alumno: ")
        aleatorio = random.randint (1, 4)
        if alumno == innombrable :
            salida = True
        else:
            print ("Ejecutando y seleccionando casa")
            print("El sombreo dice que", alumno, "pertenece a", casa[aleatorio -1])

    if numero == 2 :
        alumno = input("Nombre del alumno: ")
        print ("Ejecutando y mostrando estadisticas")

    while numero != 1 and numero != 2:
        numero = int(input ("Opcion incorrecta. Elige una opcion. Si quieres salir del programa, escribe la opcion 1 y el nombre del personaje innobrable: "))

print("Apparition, transportame a otro sitio")