print('{:=^40}'.format(' CARDOSO ENTERPRISES '))
preco = float(input('Preço do produto: R$'))
forma = int(input('''Digite a forma de pagamento:
1 - À vista.
2 - À vista no cartão.
3 - 2x no cartão.
4 - 3 x ou mais no cartão: '''))
if forma == 1:
    preco = preco - (preco * 10 / 100)
    print('Para pagamento à vista você tem 10% de desconto e pagará R${:.2f}'.format(preco))
elif forma == 2:
    preco = preco - (preco * 5 / 100)
    print('Para pagamento à vista no cartão você terá 5% de desconto e pagará R${:.2f}'.format(preco))
elif forma == 3:
    valor = preco / 2
    print('Para pagamento em até 2x não há juros e você pagará: R${:.2f}'.format(preco))
    print('Valor da parcela: R${:.2f}'.format(valor))
elif forma == 4:
    npar = int(input('Digite o número de parcelas desejadas: '))
    if npar == 1 or npar == 2:
        print('\033[1;31mUtilize a opção 4 para 3 ou mais parcelas, favor tentar novamente.\033[m')
    else:
        preco = preco + (preco * 20 / 100)
        valor = preco / npar
        print('Para pagamento em 3x ou mais há 20% de juros e você pagará R${:.2f}'.format(preco))
        print('O valor da parcela será R${:.2f}'.format(valor))
else:
    print('Opção inválida, favor escolher entre as opções 1, 2, 3 ou 4')

