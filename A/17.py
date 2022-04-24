import math
n1 = int(input('Digite o cateto oposto: '))
n2 = int(input('Agora digite o cateto adjacente: '))
n3 = (n1**2)
n4 = (n2**2)
n5 = (n3+n4)
n6 = math.sqrt(n5)
print('O comprimento da hipotenusa é {:.3f}' .format(n6))
