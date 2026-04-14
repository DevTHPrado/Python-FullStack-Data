#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada Km acima do limite

v = float(input('Digite a velocidade que o carro passou no radar: '))
print('O limite de velocidade nesta via é de 80Km/h')
multa = float(7.00 * (v - 80))
if v > 80 :
    print('Você foi multado! A velocidade do seu carro estava a {}Km/h, com isso, o valor da multa é de R${:.2f}'.format(v,multa))
else:
    print('Você estava dentro do limite de velocidade, seu carro estava a {}Km/h'.format(v))

    # Não é necessário utilizar o else nesse caso, da para resolver com a estrutura simplicada

velocidade = float(input('Digite a velocidade do carro: '))
m = float (velocidade - 80) * 7

if velocidade > 80 :
    print('VOCÊ FOI MULTADO! O limite de velocidade é de 80Km/h, você deverá pagar R${:.2f}!'.format(m))
print('Tenha um bom dia e dirija com segurança!')