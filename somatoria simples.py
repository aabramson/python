# soma de valores - v1 - Alexandre Abramson
print ("Calculadora de Soma de Valores")
n = float (input ("Insira um número diferente de zero, sendo este o finalizador desta função: "))
total = n
while n:
	n = float (input ("Insira o próxmo valor:"))
	total = total + n
print ("Total: %.2f" % total)  