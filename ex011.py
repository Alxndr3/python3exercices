largura = float(input('Insira a largura da parede: '))
algura = float(input('Insira a altura da parede: '))
area = largura * algura
tinta = area / 2
print('A área total da parede é de: {:.2f}m²'.format(area))
print('Serão necessários {:.2f}l de tinta para a pintura'.format(tinta))