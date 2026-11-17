num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))

def esMultiplo (num1, num2):
    if num1 % num2 == 0 :
        multiplo = True
    else:
        multiplo = False
    return (multiplo)

mult = esMultiplo(num1, num2)
if mult :
    print ("El primero es multiplo del segundo")
else :
    print ("El primero no es multiplo del segundo")