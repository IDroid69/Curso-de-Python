nascimento = int(input('Em que ano voçê nasceu? '))
nascimento1 = str(input('Voçê já fez aniversario esse ano? '))
if nascimento1 == 'sim':
    a = 2621
elif nascimento1 == 'nao' or 'não':
    a = 2620
idade = int(a - nascimento)
idade1 = int('{}'.format(idade)[1:3])
n1 = int(idade1 - 18)
n2 = int(18 - idade1)
print(f'Voçê tem {idade1} anos.')
if idade1 < 18:
    print(f'Voçê ainda não pode se alistar! Falta {n2} anos!')
elif idade1 == 18:
    print('Está na hora de voçê se alistar!')
else:
    print(f'Já passou do tempo de alistamento. Passou {n1} anos.')