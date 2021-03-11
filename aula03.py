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
n2 = int(input('Digite um segundo número: '))

resn = n % 2
resn2 = n2 % 2

if resn == 0 or resn2 == 0:
    print('Um número par foi digitado.')
else:
    print('Nenhum número par foi digitado.')