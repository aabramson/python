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

### Litros cobertos por metro quadrado
litros=metros_quad/6


### Quantos metros uma lata grande consegue cobrir
lata_grande=litros/108

### Quantos metros uma lata pequena consegue cobrir
lata_pequena=litros/21.6

### Preços da lata grande (lg) e da lata pequena (lp)
preco_lg=80
preco_lp=25

### Proporção de preço por metro, ou seja, até 56% compensa fazer com latinha
proporcao=(108*preco_lp)/(21.6*preco_lg)

print()
if metros_quad <= 108:
    print ()
    print ('Latas grandes: 1 lata')
    print ('Latas pequenas: %.0f latas' %int(metros_quad/21.6))
    print('Preço com latões: R$ %.2f'%(preco_lg*1))
    print ('Preço com latinhas: R$ %.2f'%int((preco_lp*metros_quad/21.6)))

elif metros_quad > 108 :
    lg_correcao=int('%0.f'%(metros_quad/108))
    lp_correcao=int('%0.f'%(metros_quad/21.6))
    if lata_grande % lg_correcao != 0:
        if metros_quad % 108 < 56:
            print('O cliente precisará de %.0f latas de tinta' % (lg_correcao + 1))
            preco = preco_lg * (lg_correcao + 1)
            print('Preço: R$ %.2f' % preco)
        elif metros_quad % 108 >= 56:
            print('O cliente precisará de %.0f latas de tinta' % (lg_correcao))
            preco = preco_lg * (lg_correcao)
            print('Preço: R$ %.2f' % preco)
    if lata_pequena % lp_correcao != 0:
        if metros_quad % 21.6 < 10.8:
            print('O cliente precisará de %.0f latinhas de tinta' % (lp_correcao + 1))
            preco = preco_lp * (lp_correcao + 1)
            print('Preço: R$ %.2f' % preco)
        elif metros_quad % 21.6 >= 10.8:
            print('O cliente precisará de %.0f latinhas de tinta' % (lp_correcao))
            preco = preco_lp * (lp_correcao)
            print('Preço: R$ %.2f' % preco)
else:
    print('O cliente precisará de %.0f latas de tinta grande' % lata_grande)
    print()
    print('Ou o clietne precisará de %.0f latas pequenas' % lata_pequena)
    preco_tot_lg = preco_lg * lata_grande
    preco_tot_lp = preco_lp * lata_pequena
    print()
    print('Preço lata grande: R$ %.2f' % preco_tot_lg)
    print('Preço lata pequena: R$ %.2f' % preco_tot_lp)