### Programa para cálculo teórico de tempo de download em relação a velocidade do link ###

while True:
    tamanho_opcao = str(input('Cálculo do arquivo em (M)Bytes ou (m)bits?: '))
    if 'M' not in tamanho_opcao and 'm' not in tamanho_opcao:
        print('Por favor, escolher entre Megabytes (M) ou megabits (m)')
    else: break

tamanho = float(input('Tamanho do arquivo: '))
velocidade = float(input('Velocidade do link (em Mbps): '))
tamanho_real = 0

if tamanho_opcao == 'M':
    tamanho_real = tamanho*8
else:
    tamanho_real = tamanho

tempo = tamanho_real/velocidade

segundos = tempo%60
minutos = tempo//60
minutos_corrigidos = minutos%60
horas = minutos//60
horas_corrigidas = horas%24
dias = horas//24
dias_corrigidos = dias%30
meses = dias//30
meses_corrigidos = meses%12
anos = meses//12

p_ano = None
p_mes = None
p_dia = None
p_hora = None
p_minuto = None
p_segundo = None

if anos == 1:
    p_ano = str('ano')
else:
    p_ano = str('anos')

if meses_corrigidos == 1:
    p_mes = str('mês')
else:
    p_mes = str('meses')

if dias_corrigidos == 1:
    p_dia = str('dia')
else:
    p_dia = str('dias')

if horas_corrigidas == 1:
    p_hora = str('hora')
else:
    p_hora = str('horas')

if minutos_corrigidos == 1:
    p_minuto = str('minuto')
else:
    p_minuto = str('minutos')

if segundos == 1:
    p_segundo = str('segundo')
else:
    p_segundo = str('segundos')

if anos > 0:
    print('Tempo total de download: %.0f %s, %0.f %s, %.0f %s, %.0f %s, %0.f %s e %0.f %s.' % (anos, p_ano, meses_corrigidos, p_mes, dias_corrigidos, p_dia, horas_corrigidas, p_hora, minutos_corrigidos, p_minuto, segundos, p_segundo))
elif meses > 0:
    print('Tempo total de download: %.0f %s, %.0f %s, %.0f %s, %0.f %s e %0.f %s.' % (meses_corrigidos, p_mes, dias_corrigidos, p_dia, horas_corrigidas, p_hora, minutos_corrigidos, p_minuto, segundos, p_segundo))
elif dias > 0:
    print('Tempo total de download: %.0f %s, %.0f %s, %0.f %s e %0.f %s.' % (dias, p_dia, horas_corrigidas,p_hora, minutos_corrigidos,p_minuto, segundos, p_segundo))
elif horas > 0 and dias == 0:
    print('Tempo total de download: %.0f %s, %0.f %s e %0.f %s.' % (horas_corrigidas,p_hora, minutos_corrigidos,p_minuto, segundos, p_segundo))
elif minutos > 0 and horas == 0:
    print('Tempo total de download: %0.f %s e %0.f %s.' % (minutos_corrigidos, p_minuto, segundos, p_segundo))
elif (segundos > 0) and (segundos < 60) and minutos == 0 and horas == 0 and dias == 0:
    print('Tempo total de download: %.0f %s.' % (segundos, p_segundo))
