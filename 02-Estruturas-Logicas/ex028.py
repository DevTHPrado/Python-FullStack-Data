#Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o úsuario tentar descobrir
#qual foi no número escolhido pelo computador. O computador deverá escrever na tela se o úsuario venceu ou perdeu

import random
from time import sleep # faz o computador demorar um pouco para responder
n = random.randint(0, 5)
print('-=-' * 20) # enfeite
print('Olá, tente adivinhar o número que eu vou escolher de 0 á 5!') # Faz o computador "PENSAR"
print('-=-' * 20) # enfeite

n2 = int(input('Digite um número de 0 á 5: ')) # Jogador tenta adivinhar
print('-=-' * 20)
print('PROCESSANDO...')
sleep(2) # faz o computador demorar 2 segundos para responder

if n2 == n :
    print('Você acertou, eu pensei no {} também!'.format(n))
else:
    print('Você errou, eu pensei no número {}'.format(n))
