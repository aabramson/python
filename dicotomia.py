### Paradoxo da Dicotomia ###




from decimal import *
with localcontext() as context:
    context.prec = 1

a = 0.5
n = 2
i = 1
while a < 1:
    a = a + (1 / (n * 2))
    n = n * 2
    print(Decimal(a))
    i = i+1
print('Chegamos a 1, com', i, 'iterações.')
