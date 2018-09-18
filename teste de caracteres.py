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
        print(a[n], end=', ')
        n += 1
    print('%f e %f' % (a[len(a)-2], a[len(a)-1]))
elif len(a) == 2:
    print(a[0], 'e', a[1])
elif len(a) == 1:
    print(a[0])