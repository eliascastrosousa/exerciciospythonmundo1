#Exercício Python 010: Crie um programa que leia quanto dinheiro
#uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('BEM VINDO AO CONVERSOR DE MOEDAS DO ELIAS 1.0!!!!')
a = float(input('Digite o quanto você tem na carteira: '))
b = (a/5.65)
print('você tem R${}, dá para comprar ${:.2f} Dolar. '.format(a,b))