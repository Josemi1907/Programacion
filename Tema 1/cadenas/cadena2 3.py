frase = "Hola mundo"
print (frase)
print("Seleccionada opción de menú 1")
print("Seleccionadas opción de menú 2")
numero = input()
cantidad = 0

while numero != "exit" :
    if numero == "1" :
        frase = input ("Dime una frase: ")
        for i in range (len(frase)) :
            x = frase [i]
            print (x)

    if numero == "2" :
        letra = input ("Dime la letra que desea buscar: ")
        for i in frase :
            if i == letra :
                cantidad = cantidad + 1
        porcentaje = cantidad / len(frase) * 100
        print ("El numero de veces que esta la letra", letra, "es de:", cantidad, "su porcentaje es:", porcentaje, "%")

    if numero == "3" :
        cadena = input("Dime una cadena: ")
        subcadena = input ("Dime una subcadena: ")
        coincide = True
        if len(subcadena) > len(cadena):
                coincide = False

        else:
            for i in range (len(subcadena)) :
                if  cadena[i] != subcadena[i] :
                    coincide = False

        if coincide:
            print("empieza con subcadena")

        else:
            print("No empieza por subcadena")

    else :
        print ("Opcion incorrecta")

    print ("=============================================")
    print("Selecciona opción de menú 1")
    print("Selecciona opción de menú 2")
    print("Selecciona opción de menú 3")
    numero = input()

print ("FIN")
