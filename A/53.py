print('=-'*20)
print('10 TERMOS DE UMA PA')
print('=-'*20)
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = pt + (10 - 1) * r
for a in range(pt, d + r, r):
    print('{} ' .format(a), end='→ ')
print('ACABOU')
