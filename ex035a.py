ra = int(input('Digite a medida da primeira reta: '))
rb = int(input('Digite a medida da segunda reta: '))
rc = int(input('Digite a medida da terceira reta: '))
if ra >= rb >= rc:
    gra = ra
    med = rb
    peq = rc
    print('{}, {}, {}'.format(gra, med, peq))
    if (peq + med) > gra:
        print('Triângulo possível')
    else:
        print('Triângulo não possível')
elif rb >= rc >= ra:
    gra = rb
    med = rc
    peq = ra
    print('{}, {}, {}'.format(gra, med, peq))
    if (peq + med) > gra:
        print('Triângulo possível')
    else:
        print('Triângulo não possível')
elif rc >= ra >= rb:
    gra = rc
    med = ra
    peq = rb
    print('{}, {}, {}'.format(gra, med, peq))
    if (peq + med) > gra:
        print('Triângulo possível')
    else:
        print('Triângulo não possível')
elif rc >= rb >= ra:
    gra = rc
    med = rb
    peq = ra
    print('{}, {}, {}'.format(gra, med, peq))
    if (peq + med) > gra:
        print('Triângulo possível')
    else:
        print('Triângulo não possível')
