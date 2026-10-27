print ("¿Cuanto dinero ha enviado hoy?")
dineroEnviadoHoy = float (input ())
print ("¿Cuanto dinero envia?")
dineroParaEnviar = float (input ())
dineroDiario = float (dineroParaEnviar + dineroEnviadoHoy)

if dineroParaEnviar >= 0.50 and dineroParaEnviar <= 1000 and dineroDiario <= 2000 :
    dineroEnviado = True
    print (dineroEnviado)

else :
    noEnviar = False
    print (noEnviar)
