import random

cont = 0

print('-='*30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-='*30)
while True:
    
    try:
        valor = int(input('Diga o valor: ')) 
    except ValueError as error:
        print('Error... Voçê só pode digitar número.')
        valor = int(input('Diga o valor: '))
    
    while True:
        d = (input('Par ou Ímpar? [P/I]')).upper()
        if d != 'P' and d != 'I':
            print('Error... Voçê só pode digitar P ou I.')
        else:
            break
    
    pc = (random.randint(0,10))
    soma = (valor + pc)
    dpc = ''
    if d == 'P':
        dpc = 'I'
    else:
        dpc = 'P'
    #-------------------
    if (soma%2) == 0:
        r = 'Par'
    else:
        r = 'Ímpar'
    
    print('-'*30)
    print(f'Voçê jogou {valor} e o computador {pc}. Total de {soma} DEU {r}')
    print('-'*30)
    
    if (soma%2) == 0:
        r2 = 'P'
    else:
        r2 = 'I'
    #-------------------
    if r2 == d:
        print('-'*30)
        print('Voçê VENCEU!')
        print('-'*30)
        cont += 1
    else:
        print('-='*30)
        print('Voçê PERDEU!')
        print('-='*30)
        if cont == 0:
            print(f'GAME OVER! Voçê não venceu nenhuma vez!🙁')
            break
        elif cont == 1:
            print(f'GAME OVER! Voçê venceu {cont} vez!🙂')
            break
        elif cont > 1:
            print(f'GAME OVER! Voçê venceu {cont} vezes!😀')
            break