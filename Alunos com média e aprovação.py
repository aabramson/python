# Cadastro de alunos com notas e médias
print ()
print ('Bem vindo ao sistema de cadastro da escola Raimundão. CHAMA!!!')
print ()
alunos = []
notas_p1 = []
notas_p2 = []
notas_p3 = []
notas_p4 = []

while 1:
    aluno = input ('Por favor, insira o nome do aluno, ou aperte ENTER para terminar a operação: ')
    if not aluno:break
    alunos.append(aluno)

quantidade = len(alunos)
i=0

while i < quantidade:
    try:
        p1 = float(input('Insira a nota P1 do aluno %s: ' % alunos[i]))
        while p1 >= 0 and p1 <= 10:
            notas_p1.append(p1)
            print('Nota do aluno %s inserida com sucesso!' % alunos[i])
            break
        else:
            print('A nota deve ser entre 0 e 10. Por favor, corrija o erro!')
            continue
        p2 = float(input('Insira a nota P2 do aluno %s: ' % alunos[i]))
        while p2 >= 0 and p2 <= 10:
            notas_p2.append(p2)
            print('Nota do aluno %s inserida com sucesso!' % alunos[i])
            break
        else:
            print('A nota deve ser entre 0 e 10. Por favor, corrija o erro!')
            continue
        p3 = float(input('Insira a nota P3 do aluno %s: ' % alunos[i]))
        while p3 >= 0 and p3 <= 10:
            notas_p3.append(p3)
            print('Nota do aluno %s inserida com sucesso!' % alunos[i])
            break
        else:
            print('A nota deve ser entre 0 e 10. Por favor, corrija o erro!')
            continue
        p4 = float(input('Insira a nota P4 do aluno %s: ' % alunos[i]))
        while p4 >= 0 and p4 <= 10:
            notas_p4.append(p4)
            print('Nota do aluno %s inserida com sucesso!' % alunos[i])
            break
        else:
            print('A nota deve ser entre 0 e 10. Por favor, corrija o erro!')
            continue
        i+=1
    except:
        print ('Por favor, digite um valor numérico válido!')


while 1:
    try:
        media = float (input ('Insira a nota média para aprovação: '))
        break
    except:
        print ('Por favor, digite um valor numérico adequado.')

print ()
print ('Calculando médias dos alunos, com resultado de aprovação ou reprovação...')
print ()

i = 0

while i < quantidade:
    final = (notas_p1 [i] + notas_p2 [i] + notas_p3 [i] + notas_p4 [i]) / 4
    if final >= media:
        print ('Aluno %10s APROVADO, com média %.2f' % (alunos [i], final))
    else:
        print ('Aluno %10s REPROVADO, com média %.2f. SE FODEU!!!' % (alunos [i], final))
    i+=1
print ('-'*50)
print ('Tenha um bom dia!')