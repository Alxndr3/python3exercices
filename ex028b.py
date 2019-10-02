from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = input('') # Jogadro tenta adivinhar o número
if jogador == computador:
    print('PROCESSANDO...')
    sleep(2)
    print('PARABÉNS!!! Você conseguiu me vencer!')
else:
    print('PROCESSANDO...')
    sleep(2)
    print('Ganhei! Eu pensei no número {} e não no número {}'.format(computador, jogador))
