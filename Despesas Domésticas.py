# Programa teste de balanço de números fictício - Alexandre Abramson
print ("Programa de Balanço Doméstico")
ana = float (input ("Quanto gastou Ana?"))
bete = float (input ("Quanto gastou Bete?"))
print ()

total = float (ana) + float (bete)
print ("Total de gastos: R$ %.2f" % total)
media = total / 2
print ("Média de gastos: R$ %.2f" % media)
print ("-"*40)
if ana < media:
	diferenca = media - ana
	print ("Ana deverá ressarcir Bete com R$ %.2f" % diferenca)
	print ()
	print ("Se fode ae Ana...")
	print ()
elif ana == media:
	print ()
	print ("Tá tudo certo, irmão...")
	print ()
else:
	diferenca = media - bete
	print ("Bete deverá ressarcir Ana com R$ %.2f" % diferenca)
	print ()
	print ("Se fode ae Bete...")
	print ()