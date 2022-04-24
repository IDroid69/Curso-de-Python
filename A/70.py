
from os import error

cont = cont2 = cont3 = 0
while True:
    print('-='*30)
    print('CADASTRE UMA PESSOA')
    print('-='*30)
    
    try:
        idade = int(input('Idade: '))
    except ValueError as error:
        print('Error... Voçê tem que digita um número...')
        idade = int(input('Idade: '))
            
    sexo = str(input('Sexo: [M/F] ')).upper()
    
    while True:
        if sexo != 'M' and sexo != 'F':
            print('Error... Tente novamente...')
            sexo = str(input('Sexo: [M/F] ')).upper()
        else:
            break
        
    c = str(input('Quer continuar? [S/N]')).upper()
    
    while True:
        if c != 'S' and c != 'N':
            print('Error... Tente novamente...')
            c = str(input('Quer continuar? [S/N]')).upper()
        else:
            break
        
    if idade > 18:
        cont += 1
    
    if sexo == 'M':
        cont2 += 1
    
    if sexo == 'F' and idade < 20:
        cont3 += 1
    
    if c == 'S':
        True
    else:
        print(f'Total de pessoas com mais de 18 anos: {cont}')
        print(f'Ao todo temos {cont2} homens cadastrados.')
        print(f'É temos {cont3} mulheres com menos de 20 anos.')
        break