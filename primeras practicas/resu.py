resultado=3
print ("dame un numero")
num=int(input())
if num %2 == 0 :
    print("par")
    resultado=resultado*num
num=num+1
resultado=resultado+num
print(resultado)