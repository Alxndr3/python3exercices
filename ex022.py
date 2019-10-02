nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
rang = len(nome.replace(' ', ''))
prin = len(lista[0])
print('Analizando seu nome...')
print('{}'.format(nome.title()))
print('Seu nome maiusculo: {}'.format(nome.upper()))
print('Seu nome minusculo: {}'.format(nome.lower()))
print('O total de caracteres excetuando espaços é: {}'.format(rang))
print('O total de caracteres excetuando espaços é: {}'.format(len(nome) - (nome.count(' '))))
print('O total de caracteres excetuando espaços é: {}'.format(len(nome.replace(' ', ''))))
print('O primeiro nome tem: {} caracteres'.format(prin))





