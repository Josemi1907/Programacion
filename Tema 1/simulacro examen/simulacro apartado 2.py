alumno = input ("¿Cual es el nombre del alumno?: ")
nota = int(input("¿Cual es su nota?(0 al 100): "))

while nota < 0 or nota > 100 :
    nota = int(input("Nota incorrecta, Vuelva a repetir su nota: "))

while alumno != "exit" :
    if nota >= 90 and nota <= 100 :
        print ("Sobresaliente")

    elif nota >= 70 and nota <= 89 :
            print ("Notable")

    elif nota >= 60 and nota <= 69 :
            print ("Bien")

    elif nota >= 50 and nota <= 59 :
            print ("Suficiente")

    elif nota >= 0 and nota <= 49 :
            print ("Suspenso")

    alumno = input ("¿Cual es el nombre del alumno?: ")
    nota = int(input("¿Cual es su nota?(0 al 100): "))

