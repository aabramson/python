a = []
n = 0
while 1:
    try:
        insert = float(input('Digite um número para colocar na pilha: '))
        a.append(insert)
    except:
        break
if len(a) >= 3:
    while n <= len(a) - 3:
        print(int(a[n]), end=', ')
        n += 1
    print('%i e %i' % (int(a[len(a)-2]), int(a[len(a)-1])))
elif len(a) == 2:
    print(int(a[0]), 'e', int(a[1]))
elif len(a) == 1:
    print(int(a[0]))
