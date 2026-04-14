#Escreva um programa que leia um valor em metros e exiba convertido em centimentos e milimentros

m = float(input('Digite uma quantidade em metros:'))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} metros equivale a {} quilometros'.format(m, km))
print('{} metros equivale a {} hectômetros'.format(m, hm))
print('{} metros equivale a {} decâmetros'.format(m, dam))
print('{} metros equivale a {:.0f} decimetros'.format(m, dm))
print('{} metros equivale a {:.0f} centímetros'.format(m, cm))
print('{} metros equivale a {:.0f} milímetros'.format(m, mm))