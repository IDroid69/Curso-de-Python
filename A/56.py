cont = 0
cont1 = 0
for c in range(0, 7):
    anos = int(input(f'[{c}] Digite ano de nascimento: '))
    idade = 2621 - anos
    idade1 = idade - 600
    if idade1 < 21:
        cont += 1
    
    elif idade1 >= 21:
        cont1 += 1
print(f'{cont1} pessoas já atingiram a maioridade.')
print(f'{cont} pessoas ainda não atingiram a maioridade.')
