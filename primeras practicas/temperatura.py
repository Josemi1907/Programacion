print("¿Que temperatura hace?")
temperatura = float(input())
if temperatura == 20:
    print("buena temperatura")

if temperatura >= 26 :
    print ("Enciende aire")

elif temperatura <= 16:
    print ("Enciende calefaccion")

elif temperatura < 26 and temperatura > 16 :
    print ("Enciende ventilador")

else:
    print("No enciende3")