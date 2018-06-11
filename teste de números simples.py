#teste de números pares e divisíveis por 5
try:
 numero = float (input ('Digite um número: '))

 if numero % 2 == 0:
  print ('O número %i é par' % numero)
  if numero % 5 == 0:
   print ('O número %i é também divisíel por cinco' % numero)
 if numero % 2 != 0:
  print ('O número %i é ímpar' % numero)
  if numero % 5 == 0:
   print ('O número %i é também divisíel por cinco' % numero)
 print ('-'*9)
 print ('Obrigado!')
 print ('-'*9)

except:
    print ('Por favor, digite um número válido!')