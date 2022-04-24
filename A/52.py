soma = 0
cont = 0
for n1 in range(1,7):
    num = int(input(f'Primeiro {n1}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voçê informou {} números pares é a soma foi {}' .format(cont, soma))
