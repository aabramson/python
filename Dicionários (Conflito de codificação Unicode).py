dicionario = {}

i=1

carro = input ('Insira o nome do carro e, caso queira terminar, digite [S]air: ').title()

while carro not in ('S','Sair'):
    dicionario[i] = carro
    if not carro:
        dicionario.pop(i)
        i-=1
    try:
        while True:
            float (carro)
            print ('-' * 26)
            print ('| Insira somente letras! |')
            print ('-' * 26)
            dicionario.pop (i)
            carro = input ('Insira o nome do carro e, caso queira terminar, digite [S]air: ').title()
            break
    except:
        carro = input ('Insira o nome do carro e, caso queira terminar, digite [S]air: ').title()
        i+=1

else:
    print()
    print()
    print('-' * 31)
    print('|Lista de Carros Cadastrados: |')
    print('-' * 31)
    for chave,valor in dicionario.items():
        str_chave = str (chave)
        str_valor = str (valor)
        print ('|Carro ' + str_chave + ": " + str_valor + ' ' * (21 - len (str_chave) - len (str_valor)) + '|')
        print('-' * 31)
print ()
print ('      .::Obrigado::.')
print ()