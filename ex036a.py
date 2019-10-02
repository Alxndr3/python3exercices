valor = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = float(input('Em quantos anos você deseja pagar? '))
prestação = valor / (anos * 12)
consumo = (salario * 30) / 100
print('O valor da prestação será de R${:.2f}'.format(prestação))
if prestação > consumo:
    print('Seu empréstimo não pode ser concedido.', end=' ')
    print('A prestação não pode exceder R${:.2f}'.format(consumo))
else:
    print('Empréstimo concedido.')


