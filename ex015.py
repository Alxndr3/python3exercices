kmr = float(input('Quantos Km foram rodados? '))
dia = int(input('Por quantos dias o carro foi utilizado? '))
totpag = (kmr * 0.15) + (dia * 60)
print('O total a pagar é: R${:.2f}'.format(totpag))