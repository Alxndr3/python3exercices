'''import math
angulo = float(input('Digite um ângulo: '))
seno  = math.sin(math.radians(angulo))
cosse = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('Seu Seno, cosseno e tangente são: {}, {}, {} respectivamente'.format(seno, cosse, tang))'''

from math import radians, sin, cos, tan

ângulo = float(input('Digite um ângulo: '))
seno = sin(radians(ângulo))
cosse = cos(radians(ângulo))
tang = tan(radians(ângulo))

print('Seu seno, cosseno e tangente são: {:.2f}, {:.2f}, {:.2f} respectivamente'.format(seno, cosse, tang))

