factorial = int(input("Ingrese un número : "))
resultado = 1
texto = ""
numGuardado = []
print ("======================")
for i in range(1, factorial + 1):
    resultado = resultado * i
    x = "x"
    numGuardado.append (i)

for i in range (1, factorial + 1) :
    texto = texto + str (i)
    if i < factorial :
        texto = texto + "" + x + ""
    

print (factorial, "!=", texto , "=", resultado)
