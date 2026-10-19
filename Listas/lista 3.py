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

