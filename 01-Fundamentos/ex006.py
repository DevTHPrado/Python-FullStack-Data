#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = float(input('Digite um número:'))
x2 = n * 2
x3 = n * 3
raizq = n ** (1/2)
print('O dobro de {} é: {}'.format(n, x2))
print('O triplo de {} é: {}'.format(n, x3))
print('A raiz quadrada de {} é: {:.2f}'.format(n, raizq))

#Ou, utilizando \n para pular as linhas do print

n = float(input('Digite um número:'))
x2 = n * 2
x3 = n * 3
raizq = n ** (1/2)
print('O dobro de {} é: {}. \nO triplo de {} é: {}. \nA raiz quadrada de {} é: {:.2f}'.format(n, x2, n, x3, n, raizq))

#Ou, fazendo a conta no proprio format
n = float(input('Digite um número:'))
print('O dobro de {} é: {}. \nO triplo de {} é: {}. \nA raiz quadrada de {} é: {:.2f}'.format(n, (n*2), n, (n*3), n, (n**(1/2))))

#Ou, utilizando o metodo pow() para fzr a raiz quadrada

n = float(input('Digite um número:'))
print('O dobro de {} é: {}. \nO triplo de {} é: {}. \nA raiz quadrada de {} é: {:.2f}'.format(n, (n*2), n, (n*3), n, pow(n, (1/2))))