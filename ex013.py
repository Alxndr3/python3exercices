salario = float(input('Digite seu salário: R$'))
aumeto = float(input('Digite a porcentagem de aumento: '))
novosal = salario + (salario * aumeto / 100)
print('Seu salário reajustado foi para R${:.2f}'.format(novosal))
