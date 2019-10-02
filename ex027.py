nome = str(input('Digite seu nome completo: ')).title().strip()
nome = nome.split()
print('Prazer em te conhecer')
print('Seu primeiro nome e {}: '.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[-1]))


