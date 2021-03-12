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

#Entrada de dados
a = float(input('Nota do Primeiro bimestre: '))
while a > 10:
    a = float(input('Nota inválida, digite novamente: '))

b = float(input('Nota do Segundo bimestre: '))
while b > 10:
    b = float(input('Nota inválida, digite novamente: '))

c = float(input('Nota do Terceiro bimestre: '))
while c > 10:
    c = float(input('Nota inválida, digite novamente: '))

d = float(input('Nota do Quarto bimestre: '))
while d > 10:
    d = float(input('Nota inválida, digite novamente: '))

#Manipulação de dados
media = (a + b + c + d)/4

#Saída de dados
print('='*20)
if media <= 6:
    print('Média: {:.1f} Reprovado!'.format(media))
else:
    print('Média: {:.1f} Aprovado!'.format(media))


#END