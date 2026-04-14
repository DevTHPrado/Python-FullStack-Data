# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um rograma
# que leia o nome dos quatro alunos e mostre e ordem sorteada

import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será:\n{}'.format(lista))

# o random.shuffle serve para gerar uma ordem aleatória para os valores colocados em uma lista

#OUUUUUUUU

from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
l = [n1, n2, n3, n4]
shuffle(l)
print('A ordem de apresentação será:\n{}'.format(l))