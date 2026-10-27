print ("=====================")
print ("", "", "", "", "CALCULADORA")
print ("=====================")
print ("Introduzca + si desea sumar")
print ("Introduzca - si desea restar")
print ("Introduzca * si desea multiplicar")
print ("Introduzca / si desea dividir")
cifra = input ()
print ("Introduzca 2 numeros para calcular")
primerNumero = float(input())
segundoNumero = float(input())

match cifra:
    case "+" :
        total = primerNumero + segundoNumero
    case "-" :
        total = primerNumero - segundoNumero
    case "*" :
        total = primerNumero * segundoNumero
    case "/" :
        total = primerNumero / segundoNumero

print ("El resultado es", total)