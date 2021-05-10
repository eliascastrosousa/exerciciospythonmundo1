# desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos
# dígitos separados.

numero = input('Digite um numero entre 0 e 9999: ')
uni = numero[3]
dez = numero[2]
cen = numero[1]
mil = numero[0]
print('Está é a \n unidade: {}\n dezena: {}\n centena: {}\n milhar: {}'.format(uni,dez,cen,mil))