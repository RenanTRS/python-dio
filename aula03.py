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

n = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))

resn = n % 2
resn2 = n2 % 2

if resn == 0 or resn2 == 0:
    print('Um número par foi digitado.')
else:
    print('Nenhum número par foi digitado.')
'''
a = float(input('Nota do primeiro bimestre: '))
b = float(input('Nota do segundo bimestre: '))
c = float(input('Nota do terceiro bimestre: '))
d = float(input('Nota do quarto bimestre: '))

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    media = (a + b + c + d)/4
    if media <= 6:
        print('Média: {} Reprovado!'.format(media))
    else:
        print('Média: {} Aprovado!'.format(media))
else:
    print('Alguma nota foi digitada incorretamente.')

#END