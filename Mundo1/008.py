#Exercício Python 008: Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

a = float(input('Digite sua altura: '))
print('Você tem  {:.0f} centimetros de altura e {:.0f} milímetros'.format(a*100,a*1000))

