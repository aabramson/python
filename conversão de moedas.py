# Programa de cotação de moedas estrangeiras - Alexandre Abramson
print ("Programa de Cotação de Moedas Estrangeiras")
nome = input ("Por favor, insira seu nome: ")
dolar = float (input ("Cotação do Dólar atual: "))
euro = float (input ("Cotação do Euro atual: "))
reais = float (input ("Quantidade de Reais para conversão: "))
print ("Seguem conversões pedidas: %5.2f Dólares e %5.2f Euros" % (reais/dolar,reais/euro))
print ("Obrigado pela consulta, %s." % nome)
