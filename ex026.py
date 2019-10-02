'''frase = str(input('Digite uma frase: ')).lower().strip()
if frase.count('a') < 1:
    print('Na frase nao ha a letra "a"')
elif frase.count('a') is 1:
    print('A frase contem uma letra "a"')
elif frase.count('a') > 1:
    print('A frase contem {} letras "a"'.format(frase.count('a')))
print('A primeira letra "a" esta na posiçao: {}'.format(frase.find('a')))
print('A ultima letra "a" esta na posiçao : {}'.format(frase.rfind('a')))'''

frase = str(input('Digite ua frase: ')).lower().strip()
print('A frase contem {}'.format(frase.count('a')))
print('A primeira letra "a" encontra-se na posiçao {}'.format(frase.find('a') + 1))
print('A ultima letra "a" encontra-se na posiçao {}'.format(frase.rfind('a') + 1))

