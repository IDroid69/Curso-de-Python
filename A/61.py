from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

somar = valor1 + valor2
multiplicar = valor1 * valor2

r = 0
while r != 5:
    print('=-'*20)
    print('''   OPÇÕES:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS VALORES
    [5] SAIR''')
    print('=-'*20)

    r = int(input('Escolha uma opção: '))
    if r != 1 and r != 2 and r != 3 and r != 4 and r != 5:
        print('[ERROR] Tente novamente.')
    elif r == 1:
        print(f'{valor1} + {valor2} = {somar}')
    elif r == 2:
        print(f'{valor1} x {valor2} = {multiplicar}')
    elif r == 3:
        if valor1 > valor2:
            print(f'O valor {valor1} é maior que o valor {valor2}.')
        elif valor1 < valor2:
            print(f'O valor {valor2} é maior que o valor {valor1}.')
    elif r == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
print('Saindo...')
sleep(5)
