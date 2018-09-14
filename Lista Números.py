n=[]
q=-1
while 1:
    try:
        i = input('Insira Número, ENTER para parar: ')
        if not i:break
        i=float(i)
        n.append(i)
        q+=1
    except:
        print ('Só números...')


n_sorted = sorted(n)
print()
print ('Maior número:',n_sorted[q])
print ('Menor número:',n_sorted[0])
print ('Total de números:',len(n))
