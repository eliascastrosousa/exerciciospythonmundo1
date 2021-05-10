#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na
# tela a sua porção Inteira.
import math
n = float(input('Digite quantos reais você tem: '))
print('Você tem {} reais inteiros.'.format(math.trunc(n)))