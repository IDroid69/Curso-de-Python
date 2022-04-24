valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
if valor1 < valor2:
    print('{} é menor que {}!' .format(valor1, valor2))
elif valor1 == valor2:
    print('Os valores são iguais!')
else:
    print('{} é maior que {}!' .format(valor1, valor2))