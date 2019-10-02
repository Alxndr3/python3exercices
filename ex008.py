med = float(input('Digite a medida em metros: '))
cm = med * 100
mm = med * 1000
km = med * 0.001
hm = med * 0.01
print('{}m = {}cm e {}mm'.format(med, cm, mm))
print('{}m = {}km e {}hm'.format(med, km, hm))