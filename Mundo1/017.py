#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
x= float(input('E qual o comprimento do cateto adjacente (lado menor)? '))
y= float(input('Qual o comprimento do cateto oposto (lado maior)? '))
hipotenusa = math.sqrt(y*y + x*x)
print('A sua hipotenusa é {:.2f}'.format(hipotenusa))

