dia = int(input("Dime un dia: "))
mes = int(input("Dime un mes: "))
año = int(input("Dime un año: "))
meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
bisiesto = False
total = 0

for i in range (mes -1) :
    total = total + meses [i]
total = total + dia


if año % 4 == 0 :
        bisiesto = True
else :
        bisiesto = False

if año % 100 == 0 :
        bisiesto = False

if año % 400 == 0 :
        bisiesto = True


if bisiesto == True :
    print ("El año es bisiesto")

else:
    print("El año no es bisiesto")

print ("Han transcurrido", total, "dias")