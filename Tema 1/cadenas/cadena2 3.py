frase = "Hola mundo"
print (frase)
print("Seleccionada opción de menú 1")
print("Seleccionadas opción de menú 2")
numero = input()
cantidad = 0

while numero != "exit" :
    if numero == "1" :
        for i in range (len(frase)) :
            x = frase [i]
            print (x)

    if numero == "2" :
        letra = input ("Dime la letra que desea buscar: ")
        for i in range (len(numero)) :
            if letra in frase :
                cantidad = cantidad + 1
        print ("El numero de veces que esta la letra", letra, "es de:", cantidad)

    print ("=============================================")
    print("Seleccionada opción de menú 1")
    print("Seleccionadas opción de menú 2")
    numero = input()

print ("FIN")
