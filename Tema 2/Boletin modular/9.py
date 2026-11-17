def Login(usuario, contrasena):
    if usuario == "usuario1" and contrasena == "asdasd":
        logeado = True
    
    else:
        logeado = False

    return logeado

def programaPrincipal():
    intentos = 0
    correcto = False
    while intentos < 3 and correcto == False:
        usuario = input("Introduce el usuario: ")
        contrasena = input("Introduce la contraseña: ")
        correcto = Login(usuario, contrasena)
        if correcto == True:
            print("Has iniciado sesión correctamente")

        else:
            intentos = intentos + 1
            print("Usuario o contraseña incorrectos")
            print("Intentos restantes:", 3 - intentos)

    if correcto == False:
        print("Has agotado los tres intentos")


programaPrincipal()