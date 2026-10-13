print ("Introduce el numero del mes")
mes = int(input())
print ("Introduce el dia")
dia = int(input())

match mes :
    case 1 | 2 | 3 :
        estacion = "Invierno" 
        if mes == 3 and dia > 20 :
            estacion = "Primavera"

    case 4 | 5 | 6 :
        estacion = "Primavera"
        if mes == 6 and dia > 20 :
            estacion = "Verano"

    case 7 | 8 | 9 : 
        estacion = "Verano" 
        if mes == 9 and dia > 20 :
            estacion = "Otoño"

    case 10 | 11 | 12 :
        estacion = "Otoño"
        if mes == 12 and dia > 20 :
            estacion = "Invierno"
print (estacion)