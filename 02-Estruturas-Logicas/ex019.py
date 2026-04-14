# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
x = random.choice(lista)
print('O aluno escolhido foi {}'.format(x))

# o random.choice ele vai sortear um valor dentro de uma lista

#OUUUUUUUU

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input("Terceiro aluno: "))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
x = choice(lista)
print('O aluno escolhido foi {}'.format(x))
