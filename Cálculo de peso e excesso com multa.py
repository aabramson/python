# Cálculo de peso de peixes, excesso e multas --- em construção...
print('Cálculo de peso de peixes, excesso e multas')



peixes={}

quantidade=1



# Inserção de dados
while 1:
    peso= input('Insira o peso do peixe, para terminar digite [S]air ou [ENTER]: ')
    if peso in ('s','S','Sair','SAIR'):
        break
    if not peso:
        break

    while 1:
        try:
            peso= float(peso)
            peixes[quantidade]=peso
            quantidade+=1
            break
        except:
            print ('Insira um número válido!')
            break

# Cálculo de multa e peso
soma=0

for p in peixes.keys():
    soma=peixes[p]+soma

multa=(soma-50)*4

excesso=soma-50

qtde_final= len(peixes)

print()
print()
print ('Quantidade de peixes pescados:',qtde_final)
print()
if excesso > 0:
    print ('Excesso de peso: %.3f KG' % excesso)
    print ()
if soma <= 50:
    print ('O peso total é %.3f KG e você não pagará multas. CABRA SAFADO!!!' % soma)
if soma > 50:
    print ('O peso total é %.3f KG e você pagará uma multa de R$ %.2f. CHUPA!!!' % (soma,multa))



