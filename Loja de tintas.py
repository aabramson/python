### Cálculo de quantidade de latas de tinta por metro quadrado ###


while 1:
    try:
        metros_quad= float(input('Metros quadrados a serem pintados: '))
        if metros_quad >0:
            break
        if metros_quad <= 0:
            print()
            print('Digite somente valores positivos e maiores que zero!')
            print()
            continue
    except:
        print ('Digite somente números, no formato inteiro ou fracionado, separados por ponto (.)')
        print()

litros=metros_quad/3

latas=litros/18

print()
if metros_quad <= 54:
    print('O cliente precisará de 1 lata de tinta')
    print()
    print('Preço: R$ 80.00')
if metros_quad > 54 :
    lata_correcao=int('%0.f'%(metros_quad/54))
    if latas % lata_correcao !=0:
        if metros_quad % 54 < 27:
            print('O cliente precisará de %.0f latas de tinta' % (lata_correcao+1))
            print()
            preco=80*(lata_correcao+1)
            print()
            print('Preço: R$ %.2f' % preco)
        elif metros_quad % 54 >= 27:
            print('O cliente precisará de %.0f latas de tinta' % (lata_correcao))
            print()
            preco = 80 * (lata_correcao)
            print()
            print('Preço: R$ %.2f' % preco)
    else:
        print('O cliente precisará de %.0f latas de tinta' % latas)
        print()
        preco = 80 * latas
        print()
        print('Preço: R$ %.2f'%preco)
