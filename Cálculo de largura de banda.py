### Programa para cálculo de tempo de download em relação a velocidade

tamanho=float(input('Tamanho do arquivo (em MB): '))
velocidade= float(input('Velocidade do link (em Mbps): '))

#### Cálculo
tamanho_mbps=tamanho*8

tempo=tamanho_mbps/velocidade



segundos=tempo%60
minutos=tempo//60

print('Tempo total de download: %.0f minutos e %.0f segundos.' % (minutos,segundos))

