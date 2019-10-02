from math import hypot
altu = float(input('Digite o comprimento do cateto oposto: '))
comp = float(input('Digite o comprimento do cateto adjacente: '))
hipo = (hypot(altu, comp))
print('O comprimento da hipotenusa é: {:.2f}'.format(hipo))


