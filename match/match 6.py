print ("Pulsa 1 para mostrar el listado de habitaciones")
print ("Pulsa 2 para consultar el detalle de habitación")
numero = int (input())

if numero == 1 :
    print ("habitacion")
    print ("1. Azul")
    print ("2. Roja")
    print ("3. Verde")
    print ("4. Rosa")
    print ("5. Gris")

elif numero == 2 :
    print ("Numero de habitación")
    habitacion = int (input())
    match habitacion :
        case 1 :
            nHabitacion = "1"
            planta = "Primera"
            camas = "2"
        case 2 :
            nHabitacion = "2"
            planta = "Primera"
            camas = "1"
        case 3 :
            nHabitacion = "3"
            planta = "Segunda"
            camas = "3"            
        case 4 :
            nHabitacion = "4"
            planta = "Segunda"
            camas = "2"            
        case 5 :
            nHabitacion = "5"
            planta = "Tercera"
            camas = "1"           

print ("habitacion", nHabitacion)
print (planta, "planta")
print (camas, "Camas")