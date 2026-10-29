listaDonaA = ["A", "AB"]
listaRecibeA = ["A", "0"]
listaDonaB = ["B", "AB"]
listaRecibeB = ["B", "0"]
listaDonaAB = ["AB"]
listaRecibeAB = ["A", "B", "AB", "0"]
listaDona0 = ["A", "B", "AB", "0"]
listaRecibe0 = ["0"]
dona = False
recibe = False
grupo1 = input("Dime un grupo sanguineo: ")
grupo2 = input("Dime otro grupo sanguineo: ")

if grupo1 == "A" :
    if grupo2 in listaDonaA :
        dona = True

    if grupo2 in listaRecibeA :
        recibe = True

if grupo1 == "B" :
    if grupo2 in listaDonaB :
        dona = True

    if grupo2 in listaRecibeB :
        recibe = True

if grupo1 == "AB" :
    if grupo2 in listaDonaAB :
        dona = True

    if grupo2 in listaRecibeAB :
        recibe = True

if grupo1 == "0" :
    if grupo2 in listaDona0 :
        dona = True

    if grupo2 in listaRecibe0 :
        recibe = True

if dona :
    print("El grupo sanguineo", grupo1, "dona a", grupo2)

elif recibe :
    print("El grupo sanguineo", grupo1, "recibe del", grupo2)

else:
    print ("El grupo sanguineo", grupo1, "no es compatible con el", grupo2)



