#Conjunto
'''
conjunto = {1, 3, 10, 4, 2, 2} #Coloca em ordem crescente e não duplica valor
print(conjunto)
conjunto.add(5) #Acrescenta item a um conjunto
print(conjunto)
conjunto.discard(2) #Remove item de um conjunto
print(conjunto)
'''

conjunto = {1, 2, 3, 4}
conjunto2 = {4, 5, 6, 7, 8, 9}
#conjuntos = conjunto.union(conjunto2) #Uni dois conjuntos
#print(conjuntos)
#conjunto_interceccao = conjunto.intersection(conjunto2) #Mosta os valores iguais que os conjuntos possuem
#print(conjunto_interceccao)
#conjunto_diferenca = conjunto.difference(conjunto2) #mostra o que tem neste conjunto e não no outro
#print(conjunto_diferenca)
#conjunto_diferenca_simetrica = conjunto.symmetric_difference(conjunto2) #Mostra os conjuntos tirando o que eles tem em comum
#print(conjunto_diferenca_simetrica)

conj_a = {1, 2, 3}
conj_b = {1, 2, 3, 4, 5}
#conj = conj_a.issubset(conj_b) #Serve para mostrar se um conjunto está em outro conjunto
#print(conj)
#conjsup = conj_b.issuperset(conj_a)#Serve para mostar se é um super conjunto
#print(conjsup)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conj_ani = set(lista) #Transforma lista em conjunto
print(conj_ani)
lista = list(conj_ani) #Transforma conjunto em lista
print(lista)