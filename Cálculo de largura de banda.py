### Programa para cálculo de tempo de download em relação a velocidade

while True:
    tamanho_opcao = str(input('Cálculo do arquivo em MB ou mb (selecione M ou m)?: '))
    if 'M' not in tamanho_opcao and 'm' not in tamanho_opcao:
        print('Por favor, escolher entre Megabytes (M) ou megabits (m)')
    else:
        break

tamanho = float(input('Tamanho do arquivo: '))
velocidade = float(input('Velocidade do link (em Mbps): '))
tamanho_real = 0

### Cálculo

if tamanho_opcao == 'M':
    tamanho_real = tamanho*8
else:
    tamanho_real = tamanho

tempo = tamanho_real/velocidade

segundos = tempo%60
minutos = tempo//60
minutos_corrigidos = minutos%60
horas = minutos//60
horas_corrigidas = horas%60
dias = horas//24
dias_corrigidos = dias%365
anos = dias//365

if anos >= 1:
    print('Tempo total de download: %.0f anos, %.0f dias, %.0f horas, %0.f minutos e %0.f segundos' % (anos, dias_corrigidos, horas_corrigidas, minutos_corrigidos, segundos))
elif dias > 0:
    print('Tempo total de download: %.0f dias, %.0f horas, %0.f minutos e %0.f segundos' % (dias, horas_corrigidas, minutos_corrigidos, segundos))
elif horas > 0 and dias ==0:
    print('Tempo total de download: %.0f horas, %0.f minutos e %0.f segundos' % (horas_corrigidas, minutos_corrigidos, segundos))
elif minutos > 0 and horas == 0:
    print('Tempo total de download: %.0f minutos e %.0f segundos.' % (minutos, segundos))
elif (segundos > 0) and (segundos < 60) and minutos == 0 and horas == 0 and dias == 0:
    print('Tempo total de download: %.0f segundos.' % (segundos))