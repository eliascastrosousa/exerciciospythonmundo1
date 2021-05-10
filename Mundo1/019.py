# desafio 019 - um professor quer sortear um dos alunos para apagar o quadro. faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

import random
n1 = input('Digite o nome 1: ')
n2 = input('Digite o nome 2: ')
n3 = input('Digite o nome 3: ')
n4 = input('Digite o nome 4: ')
num = random.randint(1,4)
print('O sorteado entre \n 1- {}\n 2- {}\n 3- {}\n 4- {}\n para limpar o quadro é:\nN. {}'.format(n1,n2,n3,n4,num ))