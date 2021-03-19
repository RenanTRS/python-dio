#módulos, importações de classe, métodos e construções anônimas
'''
from aula07 import Televisao #importando a classe televisão

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
'''

def contador_de_letras(lista_palavras):
    contador = []
    for x in lista_palavras: #contar os itens da lista
        qtd = len(x) #contar a quantidade de caracteres do item da lista
        contador.append(qtd) #incluir a variável à lista
    return contador #retornar a variável contador

def teste():
    return 'teste'


if __name__ == '__main__': #proteger contra outros arquivos
    lista = ['cachorro', 'gato']
    print(contador_de_letras(lista)) #print chamando função
