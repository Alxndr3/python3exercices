from time import sleep
s = 0
c = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        sleep(0.02)
        print(x)
        s += x
        c += 1
print(f'A soma dos {c} valores solicitados é {s}.')




