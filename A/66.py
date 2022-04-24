parar = ''
soma = media = cont = maior = menor = 0

while parar != 'N':
    
    valor = int(input('Digite um valor: '))
    cont += 1
    soma += valor
    media = soma / cont
    if cont == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    parar = str(input('Quer continuar? [S/N] ')).upper()

print('Voçê digitou {} valores e a média entre os valores é {:.2f} ' .format(cont, media))
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
