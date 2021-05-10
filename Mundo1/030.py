# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
from time import sleep
num = int(input('Digite um numero: '))
sleep(1)
resto = num % 2
if resto == 0:
	print('O numero é par')
else:
	print('o numero é impar')