x = 9999999
y = 0
for i in range(1, 5):
    peso = float(input('Digite o peso em Kg: '))
    if peso < x:
        x = peso
        print(f'x = {x}')
        if y < peso:
            y = peso
            print(f'y = {y}')
    elif peso > y:
        y = peso
        print(f'y = {y}')
print('O menor peso é: {}Kg'.format(x))
print('O maior peso é {}Kg'.format(y))
