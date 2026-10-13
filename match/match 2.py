print ("¿Que dia es?")
dia = str (input ())
dia = dia.upper()

match dia :
    case "LUNES" | "MARTES" | "MIERCOLES" | "JUEVES" | "VIERNES":
        print ("===================")
        print ("","" ,"","","" ,"", dia       )
        print ("===================")
        print ("8 - 9 FOL")
        print ("9 - 10 EDE")
        print ("10 - 11 PROG")
        print ("11:30 - 12 Recreo")
        print ("11:30 - 12 Progamación")
        print ("12 - 14 BBDD")
        print ("===================")

    case "SABADO" | "DOMINGO" :
        print ("Dia de estudio y reflexión")

    case _:
        print ("false")