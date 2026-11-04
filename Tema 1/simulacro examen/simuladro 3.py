dia = int(input("Dime un dia: "))
mes = int(input("Dime un mes: "))
año = int(input("Dime un año: "))
meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0

for i in range (mes -1) :
    total = total + meses [i]
total = total + dia

print ("Han transcurrido", total, "dias")