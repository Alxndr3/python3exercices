preco = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Quantos porcento de desconto: '))
novpre = preco - (preco * desconto / 100)
print('O produto que custava R${:.2f}, na promoção com {:.2f}% de desconto vai custar R${:.2f}'.format(preco, desconto, novpre))
