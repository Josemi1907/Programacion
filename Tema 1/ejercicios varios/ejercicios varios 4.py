edad = []
altura = []
mayorEdad = 0
media = 0

while len(edad) < 4 and len(altura) < 4 :
    N_edad = int(input("¿Edad?: "))
    N_altura = int(input("¿Altura?(cm): "))
    edad.append (N_edad)
    altura.append (N_altura)
    media = media + N_altura

media = media / 4

for i in range(len(edad)) :
    if edad[i] >= 18:
        print (altura [i])
        mayorEdad = mayorEdad + 1

print (mayorEdad, "mayores de edad")

for i in range(len(altura)) :
    if altura[i] < media :
        print ("El alumno", i , "mide menos de la media")