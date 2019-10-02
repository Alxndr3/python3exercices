r = float(input('Quanto dinheiro você tem na carteira? R$'))
d = float(input('Qual é a cotação do dolar hoje: '))
c = r / d
print('Com R${:.2f} Você pode comprar US${:.2f} dolares. '.format(r, c))