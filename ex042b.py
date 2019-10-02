l1 = float(input('Digite a primeira medida para formar um triângulo: '))
l2 = float(input('Digite a segunda medida para formar um triângulo: '))
l3 = float(input('Digite a terceira medida para formar um triângulo: '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Não é possível formar um triângulo.')
