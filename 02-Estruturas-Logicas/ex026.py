#Faça um programa que leia uma frase pelo teclado e mostre:

#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece pela última vez

frase = str(input('Digite uma frase: ')).strip()

#OUUUUUUUUUUUUUUUUU
# frase = str(input('Digite uma frase: ')).strip().lower()


frase = frase.lower()
print('Sua frase possui {} letras A'.format(frase.count('a')))

print('A posição em que ela aparece a primeira vez é {}'.format(frase.find('a')+1))

print('A posicão que ela se encontra pela última vez é {}'.format(frase.rfind('a')+1))