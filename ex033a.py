n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if (n1 > n2) and (n2 > n3):
    print('O primeiro número é o maior e o terceiro é o menor')
elif (n3 > n1) and (n1 > n2):
    print('O terceiro número é o maior e o segundo é o menor')
elif (n2 > n3) and (n3 > n1):
    print('O segundo número é o maior e o primeiro é o menor')
elif (n3 > n2) and (n2 > n1):
    print('O terceiro número é o maior e o primeiro é o menor')
elif (n2 > n1) and (n1 > n3):
    print('O segundo número é o maior e o terceiro é o menor')
elif (n1 > n2) and (n3 > n2):
    print('O primeiro número é o maior e o segundo é o menor')

