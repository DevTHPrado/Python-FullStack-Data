#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira
#ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6


n = float(input('Digite um número real: '))
from math import trunc
print('O número Real digitado foi {} e sua porção inteira é {}'.format(n, trunc(n)))

#OUUUUUUU

import math
n = float(input('Digite um número Real: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(n, math.trunc(n)))

#OUUUUUUU sem usar o import

n = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(n, int(n)))
