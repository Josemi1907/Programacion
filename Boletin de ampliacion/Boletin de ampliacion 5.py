print("¿Tiene suscripción plus? S/N")
plus = input()
print ("¿Cuanto ha gastado en el pedido?")
Gastado = float(input())

if plus == "S" or Gastado >= 35 :
    print ("Sin gastos de envios")