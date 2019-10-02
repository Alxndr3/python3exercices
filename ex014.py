padrao = str.upper(input('Digite (C) para converter para graus Celcius e (F) para converter para Fahrenheint: '))
temp = float(input('Digite a tenperatura: '))
if padrao == 'C':
    fahtocel = ((temp -32) * 5) / 9
    print('Hoje esta em {:.2f}° Celcius'.format(fahtocel))
else:
    celtofah = ((temp * 9) / 5) + 32
    print('Hoje esta em {:.2f}° Fahrenheints'.format(celtofah))
