# desafio 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome completo: ')
nome_upper = (nome.upper())
print('Seu nome tem SILVA: ')
print('SILVA' in nome_upper )