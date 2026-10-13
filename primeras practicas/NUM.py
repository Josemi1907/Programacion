resultado=3
num=int(input("dame un num "))
if num%2 == 0:
    print("par")
    resultado=resultado*num
num=num+1
resultado=resultado+num
print(resultado)