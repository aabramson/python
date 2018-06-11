# soma de boteco - v1 - Alexandre Abramson
# Exercício de inclusão de nomes em um dicionário

print("Calculadora de Soma de Cerveja")
contas = {}
total = 0
while 1:
    pessoa = input("Digite o nome do cabrunco: ")
    if not pessoa: break
    while 1:
        grana = input("Quanto o %s gastou? " % pessoa)
        try:
            gasto = float(grana)
            break

        except:
            print("Número inválido ou caratere não permitido")
    contas[pessoa] = gasto
    total = total + gasto
num_pessoas = len(contas)
print()
print("Número de bêbados: %d" % num_pessoas)
print("Total do tiro: %.2f" % total)
media = total / num_pessoas
print("Gasto médio por bebum: %.2f" % media)
print()
for nome in contas.keys():
    saldo = contas[nome] - media
    print("Saldo do desinfeliz %s é de: R$ %.2f" % (nome, saldo))
