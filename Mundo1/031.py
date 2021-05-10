#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print('~~BEM VINDO A AGENCIA DE VIAGENS DOIS IRMÃOS ~~')
print('-=-'*20)
km = float(input('Qual a distancia em quilometros (km): '))
preço = (km*0.50)
preço2 = (km*0.45)
if km <=200:
	print('O valor da passagem é de R${}' .format(preço))
else:
	print('O valor da passagem é de R${}' .format(preço2))

print('~~BEM VINDO A AGENCIA DE VIAGENS DOIS IRMÃOS ~~')
print('=-=-=' * 15)
km = float(input('Qual a distancia em quilometros (km): '))
if km <= 200:
    print('O valor da passagem é de R${}'.format(km*0.50))
else:
    print('O valor da passagem é de R${}'.format(km*0.45))