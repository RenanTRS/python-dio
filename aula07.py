#Metodos e funções

#Funções
'''
def soma(a, b): #soma() receberá dois valores
    return a + b #Quando possui retorno é uma função

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
    return a / b

print(soma(2, 5))
print(sub(2, 5))
print(mult(2, 5))
print(divi(2, 5))
'''

#Class
class Televisao: #Criando uma classe com o nome televisão
    def __init__(self): #metodo de início
        self.ligada = False #padrão
        self.canal = 5 #padrão

    def power(self): #Método para Ligar e desligar TV
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self): #método para aumentar canal
        if self.ligada == True:
            self.canal += 1

    def diminui_canal(self): #Método para diminuir canal
        if self.ligada == True:
            self.canal -= 1

tv = Televisao() #instanciando classe

print('Televisão está ligada: {}'.format(tv.ligada)) #chamando método ligada
tv.power() #chamando método power
print('Televisão está ligada: {}'.format(tv.ligada))
tv.power()
print('Televisão está ligada: {}'.format(tv.ligada))
tv.power()
print('Televisão está ligada: {}'.format(tv.ligada))
print('Canal: {}'.format(tv.canal))
tv.aumenta_canal() #chamando método aumenta_canal
tv.aumenta_canal()
print('Canal: {}'.format(tv.canal))
tv.diminui_canal() #chamando método diminui_canal
print('Canal: {}'.format(tv.canal))
