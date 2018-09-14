### Cálculo de salário completo com impostos inclusos ###


while 1:
    try:
        valor_hora= float(input ('Valor/hora de seu trabalho: '))
        horas_trab= float(input ('Horas trabalhadas no mês: '))
        break
    except:
        print ('Digite somente números.')
        print()

sal_bruto= valor_hora*horas_trab

IR=sal_bruto*0.11
INSS=sal_bruto*0.08
SIND=sal_bruto*0.05

print()
print('+ Salário Bruto: R$ %.2f'% sal_bruto)
print('- IR (11%%): R$ %.2f' % IR)
print('- INSS (8%%): R$ %.2f' % INSS)
print('- Sindicato (5%%): R$ %.2f' % SIND)
print ('Salário Líquido: R$ %.2f' % (sal_bruto-IR-INSS-SIND))
print()
print('Falou!!!')
