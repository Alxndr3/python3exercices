from random import choice
from time import sleep
jog = int(input('0 = PEDRA,   2 = TESOURA,   5 = PAPEL: '))
comp = choice([0, 2, 5])
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
if comp == jog:
    if comp == 0:
        comp = 'PEDRA'
    elif comp == 2:
        comp = 'TESOURA'
    else:
        comp = 'PAPEL'
    print('Computador {}. Empate!'.format(comp))
elif comp == 0 and jog == 2 or comp == 2 and jog == 5 or comp == 5 and jog == 0:
    if comp == 0:
        comp = 'PEDRA'
    elif comp == 2:
        comp = 'TESOURA'
    else:
        comp = 'PAPEL'
    print('Computador {}. Computador ganhou!'.format(comp))
elif jog == 0 and comp == 2 or jog == 2 and comp == 5 or jog == 5 and comp == 0:
    if comp == 0:
        comp = 'PEDRA'
    elif comp == 2:
        comp = 'TESOURA'
    else:
        comp = 'PAPEL'
    print('Computador {}. Você ganhou!'.format(comp))
else:
    jog != 0 or jog != 2 or jog != 5
    print('Opção inválida!')
