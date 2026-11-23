def nombreCompleto (lista):
    numerosA = 0
    for i in range (len(lista)+1):
        if lista [0][i] == "a":
            numerosA = numerosA + 1

        elif lista [1][i] == "a":
            numerosA = numerosA + 1

        elif lista [2][i] == "a":
            numerosA = numerosA + 1
    return numerosA

nombre = input("Dime tu nombre: ").lower()
apellido1 = input ("Dime tu primer apellido: ").lower()
apellido2 = input ("Dime tu segundo apellido: ").lower()
lista = nombre, apellido1, apellido2

total = nombreCompleto(lista)

print (total)
