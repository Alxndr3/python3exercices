# encoding: utf-8
import random

lista = [1, 2, 3, 4, 5]
choice = random.choice(lista)
print('Adivinhe o numero escolhido pelo computado')
guess = int(input('Digite um numero de 1 a 5: '))
if choice == guess:
    print('Voce acertou!!!')
else:
    print('Voce errou!!!')
