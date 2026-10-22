numero = 0
x = 20
total = 0
pasos = 0

while x > 2 :
    if x % 2 == 0 :
        x = x -5
    else:
        x=x-1
    total = total + x
    pasos = pasos + 1

print (pasos, total)