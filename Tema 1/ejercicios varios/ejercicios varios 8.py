producto = 0
total = 0

while producto >= 0 :
    producto = float(input("Precio del producto: "))
    if producto >= 0 :
        total = total + producto

iva = total * 7 / 100

print ("Total de la compra:", total, "lo cual el iva es:", iva)