### Programa de caixa eletrônico - módulo saque ###

### Teste de input de valores ###
while 1:
    try:
        valor = int(input('Digite o valor do saque:R$ '))
        if valor >=10 and valor <=600:
            break
        else:
            print ('Por favor, escolher valor a sacar entre R$10,00 até R$600,00')
    except:
        print ('Por favor, entrar somente com valores numéricos inteiros')
        print ()

notas={}


### Contagem de notas por valor ###

notas['cem']=valor // 100
troco= valor % 100

notas['cinquenta']= troco // 50
troco= troco % 50

notas['vinte']= troco // 20
troco = troco % 20

notas['dez']= troco // 10
troco= troco % 10

notas['cinco']= troco // 5
troco= troco % 5

notas['um'] = troco

### Dicionário com valores 'limpos' sem zeros ###
notas_contadas={}

print()
print ('-'*50)
print()

### Condição para impressão dos valores válidos ###
for i in notas.keys():
    if notas[i]!=0:
        notas_contadas[i]=notas[i]
        if i == 'um':
            print('Notas de %s Real: %i notas' % (i, notas_contadas[i]))
        elif notas_contadas[i] == 1:
            print('Notas de %s Reais: %i nota' % (i, notas_contadas[i]))
        elif notas_contadas[i] != 0:
            print ('Notas de %s Reais: %i notas' % (i,notas_contadas[i]))
print ()
print ('VALOR TOTAL SACADO: R$ %i,00 Reais' % valor)
print()
print ('-'*50)
print()