# desafio 021 - faça um programa em python que abra e reproduza o audio de um arquivo em MP3.

import pygame
pygame.init()
pygame.mixer.music.load('pedrapapel.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass