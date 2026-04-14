#Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF

c = float(input('Informe a tempertura em ºC: '))
f = ((9 * c) / 5) + 32 # é possivel usar sem os parenteses por conta da ordem de precedência 
print('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))
