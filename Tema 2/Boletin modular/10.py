def calculoTiempo (segundosIni) :
    horas = calculaHoras(segundosIni)
    minutos = calculaMinutos(segundosIni, horas)
    segundosFinales = calculaSegundos(segundosIni, minutos, horas)
    return [segundosFinales, minutos, horas]

def calculaHoras (segundosIni): 
    horas = segundosIni // 3600
    return horas

def calculaMinutos (segundosIni, horas):
    minutos = segundosIni // 60
    if horas >= 1:
        minutos = minutos - (60 * horas)
        if minutos < 0 or minutos >= 60:
            minutos = 0

    return minutos

def calculaSegundos (segundosIni, minutos, horas):
    if segundosIni >= 60:
        segundosIni = segundosIni - (minutos * 60) - (horas * 3600)
        if segundosIni < 0 or segundosIni >= 60:
            segundosIni = 0

    return segundosIni

completo = calculoTiempo(4000)
print (completo [2], "horas", completo [1], "minutos", completo [0],  "segundos")