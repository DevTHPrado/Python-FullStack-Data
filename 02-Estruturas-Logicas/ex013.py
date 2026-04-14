#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite seu sálario: R$'))

aumento = salario + (salario * 0.15)

print('Seu salário teve um aumento de 15%! Com isso, seu novo salário é de R${:.2f}'.format(aumento))

#OUUUUUUU

salário = float(input('Digite o salário do funcionário: R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))