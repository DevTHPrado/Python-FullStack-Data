#Faça um algoritmo que leia o preço e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto que quer comprar: R$'))
desconto = preco - (preco * 0.05)

print('A loja toda está com 5% de desconto! Com isso, o valor do produto fica R${:.2f}!'.format(desconto))

#OUUUUU
preço = float(input('Qual é o preço do produto?: R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% irá custar R${:.2f}'.format(preço, novo))

#irei mostrar um macete para aprender a calcular porcentagem!

vp = float(input('Valor do produto: R$'))
d = float(input('% de desconto:'))
vd = (vp * d) / 100
print('Você terá R${:.2f} de desconto nessa compra'.format(vd))
