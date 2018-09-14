def contar(x):
	if type(x) == int or type (x) == str:
		c=[]
		c.append(x)
		print (len(c))
	elif type(x) == tuple or type(x) == list or type(x) == dict:
		print (len(x))
	else:
		print ('É outra coisa')

p={1}
contar(p)
