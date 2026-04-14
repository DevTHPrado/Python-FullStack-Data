# Faça um programa que leia o comprimento do cateto oposto e o cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co ** 2 + ca** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))

#OUUUUUUU

import math
co = float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
ca = float(input('Digite o comprimento do cateto adjacente do triângulo retângulo: '))
h = math.hypot(co, ca)
print('O comprimento da hipotenusa desse triângulo retângulo é {:.2f}'.format(h))

#OUUUUUUU

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))
