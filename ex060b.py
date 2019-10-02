n = int(input('Digite um número para saber seu fatorial: '))
p = n
s = 0
for x in range(n - 1, 0, -1):
    s = n * x
    n = s
print(f'O fatorial de {p} é {n}')

