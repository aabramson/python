a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 4, 5, 6, 5555, 4324, 1]
n = 0

if len(a) > 3:
    while n < len(a)-3:
        print(a[n], end=', ')
        n += 1
    print('%.i e %.i' % (a[len(a)-2], a[len(a)-1]))
elif len(a) == 2:
    print(a[0], 'e', a[1])
elif len(a) == 1:
    print(a[0])
