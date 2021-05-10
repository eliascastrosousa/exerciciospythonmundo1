#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
#formar um triângulo.
a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))
if a <b+c and b < a+c and c < a+b:
	print('Este conjunto de medidas PODEM FORMAR um triangulo.')
else:
	print('Este conjunto de medidas NÃO PODEM FORMAR um triangulo.')