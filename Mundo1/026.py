# desafio 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.

autor = input('Digite o seu autor preferido: ').strip()
autor_lower = (autor.lower())
quantidade = (autor_lower.count('a'))
primeiroa = (autor_lower.find('a'))
ultimoa = (autor_lower.rfind('a'))
print('o nome do autor {}'.format(autor))
print ('a letra a, aparece {} vezes.' .format(quantidade))
print ('Aparece pela primeira vez em {}.' .format(primeiroa+1))
print('aparece pela ultima vez em {}.' .format(ultimoa+1))
