from datetime import date
i = 0
m = 0
for x in range(7):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        i += 1
    else:
        m += 1
print(f'{i} pessoas são maiores de idade.')
print(f'{m} pessoas são menores de idade.')
