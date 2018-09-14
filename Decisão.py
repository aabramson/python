### Programa tem pão no céu

preco=float(input('Preço unitário do pão: R$ '))
print()
print('Panificadora Tem Pão no Céu - Tabela de Preços')
print('-'*46)
print()
valor=[]
for i in range(1,51):
    valor.append(preco*i)
    print ('%2i - R$ %.2f ' % (len(valor),valor[len(valor)-1]))
