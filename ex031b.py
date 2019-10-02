dis = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a iniciar um viagem de {}km'.format(dis))
preco = dis * 0.50 if dis <= 200 else dis * 0.45
print('E o preço de sua passagém será de R${:.2f}'.format(preco))

