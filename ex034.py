sal = float(input('Sálario = '))
if sal > 1250:
    #aum = (sal * 0.10) + sal
    aum = sal + (sal * 10 / 100)
    print('Seu salário reajustado vai para R${:.2f}'.format(aum))
else:
    #aum = (sal * 0.15) + sal
    aum = (sal * 15 / 100) + sal
    print('Seu salário reajustado vai para R${}'.format(aum))

