num = int(input('Digite um número inteiro: '))
for x in range(2, num + 1):
    cos = num // x
    res = num % x
    if x >= cos and res != 0:
        print('{} / {} = {} resta {}, Número Primo'.format(num, x, cos, res))
        break
    elif res == 0:
        print('{} / {} = {} resta {}, Número Composto'.format(num, x, cos, res))
        break

