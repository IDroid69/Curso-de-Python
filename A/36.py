print('=-'*20)
print('Analisador de triangulos!')
print('=-'*20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima podem formar um {}triangulo!' .format('\033[0;34m'))
else:
    print('Os segmentos acima não podem formar um {}triangulo.' .format('\033[0;34m'))