# soma de valores - v2 - Alexandre Abramson
print ("Calculadora de Soma de Valores")
total = 0
while 1:
	try:
		linha = input ("Insira um número para soma e tecle ENTER para finalizar: ")
		n = float (linha)
		total = total + n
	except:
		if len (linha) == 0:
			break
		elif "," in linha:
			print ('Use a tecla ponto (.) para separação decimal')
		else:
			print ("Isso não parece ser um número. Por favor, corrija")
print ("Total: %.2f" % total)  


