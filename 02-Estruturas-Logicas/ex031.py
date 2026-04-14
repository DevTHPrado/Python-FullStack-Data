#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
#Km para viagens de até 200Km e R$0,45 para viagens mais longas

print('Preço da passagem para viagens de até 200Km: R$0,50 por Km')
print('Preço da passagem para viagens de mais de 200Km: R$0,45 por Km')
print('-=-' * 23)

d = float(input('Digite a distância da sua viagem em Km: '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))
if d <= 200 :
    v = float(d * 0.50)
    print('O valor da sua passagem é R${:.2f}'.format(v))
else:
    v = float(d * 0.45)
    print('O valor da sua passagem é R${:.2f}'.format(v))

#OUUUUUUUUUUUUUU
print('-=-' * 23)
distância = float(input('Qual é a distância da sua viagem?: '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância<= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))