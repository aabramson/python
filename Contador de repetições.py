# Contador de repetições de caracteres em uma lista

print()

while 1:
    try:
        char_inicial = int(input ('Digite o primeiro caractere numérico da lista: '))
        char_final = int(input ('Digite o último caractere numérico da lista: '))
        razao = int(input ('Digite a razão de repetição desta lista: '))
        lista = []
        choice = 0
        for i in range (char_inicial,char_final+1,razao):
            lista.append(i)
        print ('A Lista está desta maneira: ',lista)
        break
    except:
        print('Burrão!!!')
choice = 0
while 1:
        try:
            choice = int(input('Deseja inserir mais caracteres? Digite 1 para Sim e 2 para Não:'))
            if choice == 2:break
            elif choice != (1 or 2):
                print ('Digite 1 ou 2!!!')
                continue
            char_inicial = int(input('Digite o primeiro caractere numérico da lista: '))
            char_final = int(input('Digite o último caractere numérico da lista: '))
            razao = int(input('Digite a razão de repetição desta lista: '))
            for i in range(char_inicial, char_final+1, razao):
                lista.append(i)
            print('A Lista está desta maneira: ', lista)
            choice = int(input('Deseja inserir mais caracteres? Digite 1 para Sim e 2 para Não: '))
            if choice == 1:continue
            if choice == 2:break
            elif choice != 1 or 2:
                print('Digite 1 ou 2!!!')
                continue

        except:
            print ('Burrão!!!')


lista_str=', '.join(map(str,lista))
print()
print('-'*(len(lista_str)+38))
print ('Lista final: %s, contendo %i elementos' % (lista,len(lista)))
print('-'*(len(lista_str)+38))
print()
print('Obrigado!')