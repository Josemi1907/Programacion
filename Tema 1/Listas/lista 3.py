import random
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print (semana [6])

numero = []

for x in range (0, 5) :
    aleatorio = random.randint (0,8)
    numero.append (aleatorio)
print (numero)

multiplos = []
x = 0
while len(multiplos) <20:
    if x % 3 == 0 :
        multiplos.append(x)
    x = x + 1
print (multiplos)

multiplos7 = []
while len(multiplos7) <10:
    aleatorio7 = random.randint (0,100)
    if aleatorio7 % 7 == 0 :
        multiplos7.append(aleatorio7)
print (multiplos7)

multiplos7.insert (8, "programo")
print (multiplos7)