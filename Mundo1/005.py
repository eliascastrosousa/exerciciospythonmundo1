# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na
# tela o seu sucessor e seu antecessor.

from time import sleep
n = int(input('Digite um numero: '))
sleep(1)
print('O numero antecessor de {} é {} e o sucessor é {}.'.format(n, n-1, n+1))