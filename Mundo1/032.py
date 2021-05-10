#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
ano = int(input('Digite um ano para eu dizer se é bissexto: '))
print(calendar.isleap(ano))

ano = int(input('Digite um ano para eu dizer se é bissexto: '))
bissexto = ano %4
if bissexto == 0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')

from datetime import date
ano = int(input('Digite um ano para eu dizer se é bissexto, ou digite 0 para saber sobre o ano atual: '))
if ano == 0:
	ano = date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
