def calculaTemperaturaMedia (sumados):
    media = (sumados) / 2
    return (media)

def validacion (max, min) :
    max = int(input("Dime la temperatura maxima: "))
    min = int(input("Dime la temperatura minima: "))
    while min > max :
        print("Temperatura incorrecta")
        max = int(input("Dime la temperatura maxima: "))
        min = int(input("Dime la temperatura minima: "))
    suma = max + min
    return (suma)

dias = int(input("Cuantas dias?: "))

while dias != 0 :
    sumados = validacion (max, min)
    mediaTotal = calculaTemperaturaMedia(sumados)
    print("Temperatura media es:", mediaTotal)
    dias = dias - 1
