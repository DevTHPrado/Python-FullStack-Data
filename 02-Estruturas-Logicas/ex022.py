#Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

"""Pedindo a str pro usuario"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))

print('Seu nome em minúsculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

pn = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(pn[0])))

#OUUUUUU
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))