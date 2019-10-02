dis = float(input('Qual e a distancia da viagem? '))
if dis > 200:
    preco = dis * 0.45
    print('O preço da passagem sera: {}R${:.2f}{}'.format('\033[1;33m', preco, '\033[m'))
else:
    preco = dis * 0.50
    print("O preço da viagem será {}R${:.2f}{}".format('\033[1;33m', preco, '\033[m'))
