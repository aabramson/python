### teste de gravação básica
tamanho=[]
arq=open ('carros.txt','r')
print('********** Dados já imputados **********')
print()
print(arq.read())
with open('carros.txt') as arq:
    for i in arq:
        tamanho.append(i)
    print('Total de linhas: %i' % len(tamanho))
    print()

while True:
    novos=input('Por favor, insira outros carros na lista: ')
    if not novos:break
    with open('carros.txt','a+') as arq:
        arq.writelines(novos)
        arq.writelines('\n')

lista=[]
arq=open('carros.txt')
for i in arq:
    lista.append(i)
print(lista)
arq.close()

#continuarei daqui: quero numerar a lista obtida da variável arq obtida da leitura do arquivo carros.txt e, após isso,
#poderei excluir algum item baseado na numeração desse índice criado por um dicionário.