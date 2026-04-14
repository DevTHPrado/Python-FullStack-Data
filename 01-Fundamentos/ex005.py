#Faça um programa um leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número inteiro:'))
ant =  n - 1
sus = n + 1
print('Esse é o antecessor do seu número: {}'.format(ant))
print('E esse é o sucessor do seu número: {}'.format(sus))

#Ou
#ocupa menos memória
n2 = int(input('Digite um número inteiro:'))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n2, (n2-1), (n2+1)))