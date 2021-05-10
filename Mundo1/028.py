# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep  #importação da função randint da biblioteca random
print('Fala seu garoto de programa, vamos jogar...')
sleep(2)
print('Eu vou pensar em numero de 0 a 5 e vc vai tentar advinhar!')
sleep(2)
print('Deixa eu ver...')
sleep(3)
computador = randint(0, 5)
pessoa = int(input('Ok, Pensei.\nagora é com você! em que numero eu pensei? '))
print('ANALISANDO...')
sleep(1.5)
if computador == pessoa:
    print('Parabéns, você ganhou! o numero que eu pensei foi {} mesmo.' .format(computador))
else:
    print('Você errou, otario! eu pensei no {} e nao no {}! Boa sorte na proxima.' .format(computador,pessoa))