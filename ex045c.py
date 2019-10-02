from random import choice
from time import sleep
jog = int(input('0 = PEDRA,   1 = TESOURA,   2 = PAPEL: '))
comp = choice([0, 1, 2])
itens = ('PEDRA', 'TESOURA', 'PAPEL')
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
if comp == jog:
    print('Computador {}. Empate!'.format(itens[comp]))
elif comp == 0 and jog == 1 or comp == 1 and jog == 2 or comp == 2 and jog == 0:
    print('Computador {}. Computador ganhou!'.format(itens[comp]))
elif jog == 0 and com == 1 or jog == 1 and comp == 2 or jog == 2 and comp == 0:
    print('Computador {}. Você ganhou!'.format(itens[comp]))
elif jog != 0 or jog != 2 or jog != 5:
    print('Opção inválida!')