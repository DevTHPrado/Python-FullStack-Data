#Crie um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR

n = int(input('Digite um número: '))

if  n % 2 == 0 :
    print('O número que você digitou é PAR')
else:
    print('O número que você digitou é ÍMPAR')

#OUUUUUUUUUUUUU
numero = int(input('Digite um número qualquer: '))
resultado = numero % 2

if resultado == 0 :
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))