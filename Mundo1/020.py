# desafio 020 - o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random as r
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1,n2,n3,n4]
r.shuffle(lista)
print('a ordem de apresentação será: {}'.format(lista))