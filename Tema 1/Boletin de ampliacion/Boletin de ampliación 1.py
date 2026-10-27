print("¿Cuanto ha gastado?")
Gastado = float(input())
print("¿Tiene cupon: S o N?")
Cupon = (input())
if Gastado >= 20 and Cupon == S :
    Descuento = Gastado * 0.1
    Total = Gastado - Descuento
    print ("Tiene un descuento de", Descuento, "Gastando un total de", Total)

else :
    print ("No tiene descuento")