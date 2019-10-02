frase = str(input('Digite uma frase para saber se é um palíndromo: ')).lower().strip().replace(' ', '')
string = frase[::-1]
if frase == string:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')


'''def reverse(x):
    str = ''
    for i in frase:
        str = i + str
    return str
frase = str(input('Digite uma frase para saber se é um palíndromo: ')).lower().strip().replace(' ', '')
string = reverse(frase)
print(string)
if frase == string:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')'''


