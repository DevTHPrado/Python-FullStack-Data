#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
#a R$1250,00, calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%

s = float(input('Digite o valor do seu sálario: R$'))
if s <= 1250 :
    novo = s + (s * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, novo))
else :
    novo = s + (s * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(s, novo))