from math import pi

def calculaArea(radio):
    area = pi * radio ** 2
    return area


def calculaPerimetro(radio):
    perimetro = 2 * pi * radio
    return perimetro


def calculaAreaYPerimetro(radio):
    area = calculaArea(radio)
    perimetro = calculaPerimetro(radio)
    return [perimetro, area]


radio = float(input("Dame el radio de la circunferencia: "))

resultado = calculaAreaYPerimetro(radio)

print("El perímetro es:", resultado[0])
print("El área es:", resultado[1])