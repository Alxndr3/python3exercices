velo = float(input('Qual a velociade do carro: '))
exed = velo - 80
multa = exed * 7
if velo > 80:
    exced = (80 - velo)
    print('Voce ultrapassou a velocidade em: {}km e foi multado em: R${:.2f} '.format(exed, multa))
else:
    print("OK! You're good to go.")
