preco = float(input('Preço do produto: R$'))
desconto = float(input('Quantos porcento de desconto: '))
porc = desconto / 100
precre = porc * preco
precli = preco - precre
print('O preço final do produto é: R${}'.format(precli))