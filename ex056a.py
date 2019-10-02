tidade = 0
x = 0
y = 0
n = ''
for i in range(5):
    nome = str(input('Digite seu primeiro nome: ')).strip().lower()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite "M" para masculino e "F" para feminino: ')).strip().upper()
    tidade += idade
    if idade > x and sexo == 'M':
        x = idade
        n = nome.title()
    elif idade < 20 and sexo == 'F':
        y += 1
midade = tidade // 3
print('O homem mais velhor tem {} anos e chama-se {}.'.format(x, n))
print('A média de idade é {} anos'.format(midade))
print('{} mulheres tem menos de 20 anos.'.format(y))

