import time
num = int(input('Digite um número para ver sua tabuada: '))
con = 1
print(' ', '=' * 16)
while con <= 10:
    res = num * con
    print('|| ', num, ' x {:2} = {:2}'.format(con, res), ' ||')
    con += 1
    time.sleep(1.5)
print(' ', '=' * 16)

