 # Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
 # uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade em que o carro passou? '))
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Tudo bem pode seguir.')
else:
    print('Você foi multado, o valor para pagar é de R${:.2f}'.format(multa))

velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade-80)*7
if velocidade <= 80:
	print('Tenha um bom dia! Dirija com segurança!')
else:
	print('MULTADO! Você excedeu o limite permitido qu eé de 80km/h.\nVocê deve pagar uma multa de R${}!'.format(multa))
	print('Tenha um bom dia! Dirija com segurança!')
