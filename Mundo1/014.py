#Exercício Python 014: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em C°: '))
f = ((c*1.8)+32)
print('{} C° convertido para Fahrenheit fica em {}°F.'.format(c,f))
