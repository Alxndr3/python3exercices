n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
med = (n1 + n2) / 2
if med < 5.0:
    print('Sua média foi {}. Eu lamento, você está REPROVADO.'.format(med))
elif med >= 5.0 and med <= 6.9:
    print('Sua média foi {}. Você esta de RECUPERAÇÃO.'.format(med))
else:
    print('Sua média foi {:.2f}. Parabéns você está APROVADO!'.format(med))
