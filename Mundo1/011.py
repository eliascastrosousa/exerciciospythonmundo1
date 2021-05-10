#Exercício Python 011: Faça um programa que leia a largura e a altura
# de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma
# área de 2 metros quadrados.

l = float(input('largura da sua parede em metros: '))
a = float(input('Altura da sua parede em metros: '))
m2 = (l*a)
print('Com {:.2f}m² você irá gastar {:.2f}L de tinta'.format(m2,m2/2))
