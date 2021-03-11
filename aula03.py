'''a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite outro valor: '))

if a > b and a > c:
    print('{} é o maior número'.format(a))
elif b > a and b > c:
    print('{} é o maior número'.format(b))
elif a == b == c:
    print('Números iguais')
elif c > a and c > b:
    print('{} é o maior valor'.format(c))
'''
n = int(input('Digite um número: '))

res = n % 2
if res == 0:
    print('{} é par.'.format(n))
else:
    print('{} é ímpar.'.format(n))