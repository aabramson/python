#Sortear nomes aleatóriamente através de input do usuário - Alexandre Abramson

import random

lista = []

print ('Digite 1 para inserir um nome')
print ('Digite 2 para listagem de nomes')
print ('Digite 3 para apagar um nome')
print ('Digite 4 para sortear um nome e retirá-lo da lista')

try:
    opcao = int (input ('Por favor, insira sua opção agora: '))
except:
    print ('Insira uma opção válida!')

if opcao == 1:
    try:
        while 1:
            novo_nome = input ("Por favor, insira um nome para adicionar na lista, aperte ENTER para terminar: ")
            lista.append(novo_nome)
            if not novo_nome:
                break
            print ('Nome inserido com sucesso!')
    except:
        print ('Por favor, insira um valor válido!')

elif opcao == 2:
    print (lista)
elif opcao == 3:
    remove_nome = input ('Digite o nome a ser removido da lista: ')
    try:
        lista.remove(remove_nome)
        print ('O nome %s foi removido com sucesso da lista!' % remove_nome)
    except:
        print ('Este nome não consta na listagem, por favor tente novamente')

elif opcao == 4:
    print ('Sorteando nomes, por favor aguarde...')
    lista = lista.sort()
    resultado = random.choice (lista)
    print ('resultado')



