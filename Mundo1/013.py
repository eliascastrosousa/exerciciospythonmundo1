#Exercício Python 013: Faça um algoritmo que leia o salário de
# um funcionário e mostre seu novo salário, com 15% de aumento.

v = float(input('Digite o antigo salario: '))
n = ((15*v)/100)
print('Seu antigo salario de R${:.2f} com o aumento de 15% fica R${:.2f}'.format(v,v+n))