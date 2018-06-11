#Mostrar todos os pares ou ímpares de 1 a maximo que são divisíveis por divisor - Alexandre Abramson

while 1:
        try:
           divisor = int (input ('Digite um número divisor: '))
           break
        except:
            print ('Por favor, insira um número inteiro válido')

while 1:
        try:
            maximo = int (input ('Digite o número máximo para o contador: '))
            break
        except:
            print ('Por favor, insira um número inteiro válido')


while 1:
        try:
            razao = int (input ('Digite 1 para números ímpares ou 2 para pares: '))
            if razao == 1:
                break
            elif razao == 2:
                break
            else:
                print ('Escolha entre os números 1 ou 2')
        except:
            print ('Por favor, insira um número inteiro válido')

n = divisor

if razao == 2:
     while n <= maximo:
        if n % 2 == 0:
            if n % divisor == 0:
                print ('O número %i é par e é divisível por %i' % (n,divisor))
            elif n % divisor != 0:
                print ('O número %i é par, mas não é divisível por %i' % (n,divisor))
        n = n+1

if razao == 1:
     while n <= maximo:
        if n % 2 != 0:
            if n % divisor == 0:
                print('O número %i é ímpar e é divisível por %i' % (n, divisor))
            elif n % divisor != 0:
                print('O número %i é ímpar, mas não é divisível por %i' % (n, divisor))
        n = n+1

print ('-'*9)
print ('Obrigado!')
print ('-'*9)

