from time import sleep
num = int(input('Digite um número para saber sua tabuada: '))
de = int(input('Do número: '))
ao = int(input('Ao número: '))
print(' ', '=-' * 9)
for x in range(de, ao + 1):
    igu = num * x
    print('|| ', '{:2} x {:2} = {:2} '.format(num, x, igu),  '  ||')
    sleep(0.5)
print(' ', '=-' * 9)


