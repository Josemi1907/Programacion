print("¿Cuanta bateria tienes en el movil?")
porcentajeBateria = int(input())
print ("¿Esta recargando?: s/n")
recargando = input()

if porcentajeBateria < 20 and recargando == "s" :
    print ("Se activa el modo ahorro")