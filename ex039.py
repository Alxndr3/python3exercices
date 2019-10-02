from datetime import date
ano = int(input('Qual é seu ano de nascimento: '))
idade = date.today().year - ano
falta = 18 - idade
alista = date.today().year + falta
print('Você tem {} anos de idade.'.format(idade))
if idade == 18:
    print('Esta na hora de você se alistar.')
elif idade < 18:
        print('Ainda faltam {} para você se alistar, você de se alistar em {}.'.format(falta, alista))
elif idade > 18:
    passou = idade - 18
    ano = ano + passou
    print('Passaram-se {} do seu alistamento, seu alistamento foi em {}'.format(passou, ano))
