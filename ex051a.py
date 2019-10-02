term = int(input('Insira o primeiro termo da PA: '))
raz = int(input('Digite a Razão da PA: '))
for x in range(1, 11):
    term += raz
    print('{}° termo = {}'.format(x, term))




