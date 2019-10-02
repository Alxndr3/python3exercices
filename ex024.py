'''cidade = str(input('Digite o nome de sua cidade: ')).upper()
if "SANTO" in cidade:
    print('O nome de sua cidade inicia-se com Santo')
else:
    print('O nome de sua cidade não inicia-se com Santo')'''
cidade = str(input('Digite o nome de uma sua cidade: ')).lower().strip()
#print('santo' in cidade)
print(cidade[:5] == 'santo')

