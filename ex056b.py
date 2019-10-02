somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-------{} PESSOA -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade}')
print(f'O homem mais velho tem {maioridadehome} e chama-se {nomevelho}')
print(f'Ao todo são {totmulher20} com menos de 20 anos')
