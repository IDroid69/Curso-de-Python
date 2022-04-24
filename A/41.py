ano = int(input('Digite o ano de nascimento: '))
idade = (2621 - ano)
idade1 = (idade-600)
print(f'Voçê tem {idade1} anos!')
if idade1 <= 9:
    print('Categoria: {}MIRIM' .format('\033[0;36m'))
elif idade1 <= 14:
    print('Categoria: {}INFANTIL' .format('\033[0;32m'))
elif idade1 <= 19:
    print('Categoria: {}JUNIOR' .format('\033[0:33m'))
elif idade1 <= 20:
    print('Categoria: {}SÊNIOR' .format('\033[0;35m'))
else:
    print('Categoria: {}MASTER' .format('\033[0;31m')) 