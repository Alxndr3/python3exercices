a = float(input('Digite sua altura em metros: '))
p = float(input('Digite seu peso: '))
imc = p / (a ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 17:
    print('Muito abaixo do peso')
elif imc < 18.50:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso normal.')
elif imc < 30:
    (print('Acima do peso'))
elif imc < 35:
    print('Obesidade I')
elif imc < 40:
    print('Obesidade II - Severa')
else:
    print('Obesidade III - Mórbida')
