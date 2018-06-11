# Gerador de números de alunos
print ()
print ('Gerador de números de classe para alunos')
print ()
lista_alunos = []
lista_numeros = []

# Início do loop lógico
while 1:
    aluno = input ('Insira o nome do aluno: ')
    if not aluno:break
    lista_alunos.append(aluno)

# Contagem de alunos
quant_alunos = len (lista_alunos)

# Gerador de números na lista de números de classe
for n in range (1,quant_alunos+1):
    lista_numeros.append (n)

i = 0
alunos_ordenados = sorted (lista_alunos)

# Impressão dos alunos com seus respectivos números
while i < quant_alunos:
    print ('Aluno %8s é o número %2i da sala' % (alunos_ordenados[i],lista_numeros[i]))
    i+=1




