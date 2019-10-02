ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {}{}{} é bissexto'.format('\033[4;34m', ano, '\033[m'))
elif ano % 400 == 0:
    print("O ano {}{}{} é bissexto".format('\033[4;36m', ano, '\033[m'))
else:
    print('O ano {}{}{} não é bissexto'.format('\033[7;32m', ano, '\033[m'))





