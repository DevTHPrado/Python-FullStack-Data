#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$1,00 = R$3,27

real = float(input('Quantos reais você tem na carteira?: R$'))

dolar = 3.27

comprar = real / dolar

print('Você pode comprar U${:.2f}!'.format(comprar))

#OUUUU
#OBS: irei colocar a cotação atual do dia 13/03/2025

real = float(input('Quanto dinheiro você tem na carteira?: R$'))
dolar = real / 5.81
euro = real / 6.31
print('Com R${:.2f} você pode comprar U${:.2f} e €{:.2f}!'.format(real, dolar, euro))
