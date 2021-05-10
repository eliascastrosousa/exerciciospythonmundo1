import pygame
nome = input('digite seu nome completo: ').strip()
nomedividido = nome.split()
print('o seu primeiro nome é {}'.format(nomedividido[0]))
print('Seu ultimo nome é {}'.format(nomedividido[len(nomedividido)-1]))