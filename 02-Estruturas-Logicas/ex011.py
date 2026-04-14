#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Quantos metros de largura tem sua parede?:'))
altura = float(input('E quantos metros de altura?:'))

area = largura * altura

print('A área da sua parede é de {}m²'.format(area))

tinta = area / 2

print('Para pintar toda a sua parede irá precisar de {}l de tinta'.format(tinta))
