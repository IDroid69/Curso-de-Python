somaidade = 0
mediaidade = 0
maioridadeh = 0
nomev = ''
mulher20 = 0
for c in range(0, 4):
    nome = str(input(f'[{c}] Nome: ')).strip()
    idade = int(input(f'[{c}] Idade: '))
    sexo = str(input(f'[{c}] Sexo: [M/F]')).strip()
    print('=-'*20)
    somaidade += idade
    if c == 0 and sexo in 'Mm':
        maioridadeh = idade
        nomev = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

mediaidade = somaidade / 4
print('A media das idades do grupo é {}' .format(mediaidade))
print('O homem mais velho tem {} anos e o nome dele é {}.' .format(maioridadeh, nomev))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(mulher20))
