#Exercício Python 012: Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

v = float(input('Digite o valor: '))
d = ((5*v)/100)

print('R${:.2f} com desconto de 5% fica: RS{:.2f}'.format(v,v-d))