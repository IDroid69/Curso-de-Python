print('-='*30)
print('LOJA DO OSVALDIM')
print('-='*30)

totmil = menor = cont = soma = 0
barato = ''

while True:
    nome = str(input('Nome do Produto: '))
    
    try:
        preco = float(input('Preço: '))
    except ValueError as error:
        print('Error... Voçê só pode digitar número.')    
        preco = float(input('Preço: '))
        
    c = str(input('Quer continuar? [S/N] ')).upper()
    soma += preco
    cont += 1
    if preco > 1000:
        totmil += 1
    
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco 
            barato = nome
    
    while True:
        if c != 'S' and c != 'N':
            print('Error... Voçê pode Digitar S ou N')
            c = str(input('Quer continuar? [S/N] ')).upper()
        else:
            break
    
    if c == 'N':
        break

print('-='*30)
print(F'O total da compra foi R${soma:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
print('-='*30)