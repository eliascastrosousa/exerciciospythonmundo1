# Exercício Python 015: Escreva um programa que pergunte a quantidade
# de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Digite quantos dias o carro ficou alugado: '))
km= float(input('Digite km o carro percorreu: '))
dp = d*60
kmp = km*0.15
pagar = dp+kmp
print('''O Carro ficou {} dia(s) alugado e percorreu {} Km.
O total a pagar é de {:.2f} 
'''.format(d,km,pagar))