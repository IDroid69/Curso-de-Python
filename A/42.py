print('=-'*20)
print('Analisador de triangulos!')
print('=-'*20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima podem formar um {}triangulo!' .format('\033[0;34m'))
    if n1 == n2 == n3:
        print('{}Esse triângulo é equilátero.' .format('\033[0m'))
    if n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('{}Esse triângulo é isósceles.' .format('\033[0m'))
    if n1 != n2 != n3 != n1:
        print('{}Esse triângulo é escaleno.' .format('\033[0m'))
else:
    print('Os segmentos acima não podem formar um {}triangulo.' .format('\033[0;34m'))
