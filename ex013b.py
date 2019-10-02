preco = float(input('Insira o preço do produto: R$'))
tipo_pag = str.upper(input('Para pagamento a vista digite (V) e para pagamento a prazo digite (P): '))
if tipo_pag == 'V':
    desc_juro = float(input('Digite a porcentagem do desconto: '))
    pre_fin = preco - (preco * desc_juro / 100)
    print('O preço do produto com desconto é: R${:.2f}'.format(pre_fin))
else:
    tipo_pag == 'F'
    desc_juro = float(input('Digite a porcentagem de juros: '))
    pre_fin = preco + (preco * desc_juro / 100)
    print('O preço do produto com juros é: R${:.2f}'.format(pre_fin))
