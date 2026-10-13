edadComprador = int(input())
autorizacionParental = bool(input())

if edadComprador >= 16 or autorizacionParental :
    print ("Puede coprar el juego")

else :
    print ("No puede comprar el juego")