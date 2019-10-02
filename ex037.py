num = int(input('Digite um número: '))
conv = int(input('Digite 1 para converte-lo para binário 2 para octal e 3 para exadecimal: '))

if conv == 1:
    print('O número {} convertido para binário será "{}"'.format(num, bin(num)[2:]))

elif conv == 2:
    print('O número {} convertido para octal será "{}"'.format(num, oct(num)[2:]))

elif conv == 3:
    print('O número {} convertido para hexadecimal será "{}"'.format(num, hex(num)[2:]))

else:
    print('Opção invalida')
