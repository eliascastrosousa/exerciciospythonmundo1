#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Qual o seu salario? '))
sal_10 = ((salario/100)*10)
sal_15 = ((salario/100)*15)
if salario <=1250:
	print('O seu salario de {:.2f} com aumento, ficou {:.2f}'.format(salario,salario+sal_15))
else:
	print('O seu salario de {:.2f} com aumento, ficou {:.2f}'.format(salario,salario+(salario/100)*10))