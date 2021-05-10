import pygame
import random
from time import sleep


print('Seja bem vindo ao famoso pedra, papel e tesoura!')
print('***'*10)
sleep(1)
print('Vamos jogar!')
sleep(1)
print('Digite: ')
sleep(1)
print ('1 para PEDRA! 2 para PAPEL! 3 para TESOURA!')

sleep(2)
print('Vamos Lá!!!')
sleep(0.5)
print('3!')
sleep(1)
print('2!')
sleep(1)
print('1!')
sleep(1)
usu = int(input('VALENDO! Pode Digitar:  '))

pygame.init()
pygame.mixer.music.load('miau.mp3') #tema de abertura
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()): pass
sleep(1.5)

computador = random.randint(1,3)
if computador == 1 and usu == 1:
    print('EMPATE!!')
    print('Computador jogou Pedra e você Pedra tambem!')

elif computador == 2 and usu == 2:
    print('EMPATE!!')
    print('Computador jogou Papel e você Papel também!')

elif computador == 3 and usu == 3:
    print('EMPATE!!')
    print('Computador jogou Tesoura e você Tesoura tambem!')

elif computador == 1 and usu == 2:
    print('VOCÊ VENCEU! ')
    print('Computador jogou Pedra e você Papel !')


elif computador == 1 and usu == 3:
    print('Computador venceu!')
    print('Computador jogou Pedra e você Tesoura !')


elif computador == 2 and usu == 1:
    print('Computador venceu!')
    print('Computador jogou Papel e você Pedra !')

elif computador == 2 and usu == 3:
    print('Você venceu!')
    print('Computador jogou Papel e você Tesoura !')

elif computador == 3 and usu == 1:
    print('Você venceu!')
    print('Computador jogou Tesoura e você Pedra !')

elif computador == 3 and usu == 2:
    print('Computador venceu!')
    print('Computador jogou Tesoura e você Papel !')





