#Números primos.
n = int(input('Digite um número: '))
cont = 0

for x in range(1, n+1):
    r = n % x
    if r == 0:
        cont = cont + 1

if cont == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))