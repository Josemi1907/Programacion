import random
numero = random.randint(0,10)
numero2 = random.randint(0,10)
print ("Introduce el total de la suma de", numero, "y", numero2)
valor = int(input())
suma = numero + numero2

while valor != suma :
    print ("Incorrecto, introduce el total de la suma de", numero, "y", numero2)
    valor = int(input())

print("Fin")