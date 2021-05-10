# desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo sem considerar os espaços.
#  Quantas letras tem o primeiro nome.


nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {},'.format(nome.upper()))
print('Seu nome em minusculas é {},'.format(nome.lower()))
espaços = nome.count(' ')
tamanho = len(nome)
divisão = nome.split()
print('seu nome tem ao todo {},'.format(tamanho-espaços))
print('e seu primeiro nome tem {}.'.format(len(divisão[0])))