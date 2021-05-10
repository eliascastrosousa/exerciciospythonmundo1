# desafio 018 - faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse angulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo que vc deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print ('Este é o seno {:.2f}, cosseno {:.2f} e sua tangente {:.2f} do angulo {}.'.format(seno,cosseno,tangente,angulo))