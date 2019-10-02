a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando qual é o menor número
menor = a
if b < a and b < c:
    menor = b
if c < a and c < a:
    menor = c
# Verificando qual é o mairo número
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
