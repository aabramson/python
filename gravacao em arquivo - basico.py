### teste de gravação básica

arq = open ('c:/temp/carros.txt','r')
lista2=[]
lista=arq.readlines()
for i in lista:
    lista2.append(i)

print (lista2[::-1])

arq.close()
