print('=-'*20)
print('POSTO DO OSVALDIN')
print('=-'*20)
print('''TABELA DE PREÇOS:
ALCOOL: 1,90 4% DE DESCONTO!
ACIMA DE 20 LITROS VOÇÊ GANHA 5% DE DESCONTO!
GASOLINA: 2,50 4% DE DESCONTO!
ACIMA DE 20 LITROS VOÇÊ GANHA 6% DE DESCONTO!''')
print('-='*20)
print('''OPÇÕES: 
[1]ALCOOL
[2]GASOLINA''')
a = int(input('Escolha uma opção: '))
litros = int(input('Digite quantos litros voçê deseja coloca: '))
if a == 1:
    preço = 1.90
    if litros <= 20:
        print('Voçê tem 3% de desconto!')
        a1 = preço * litros
        a2 = a1 - (a1*0.03)
        print('O preço ficou R${:.2f}' .format(a2))
    if litros > 20:
        print('Voçê 5% de desconto!')
        b1 = preço * litros
        b2 = b1 - (b1*0.05)
        print('O preço ficou R${:.2f}' .format(b2))
if a == 2:
    preço = 2.50
    if litros <= 20:
         print('Voçê tem 4% de desconto!')
         c1 = preço * litros
         c2 = c1 - (c1*0.04)
         print('O preço ficou R${:.2f}' .format(c2))
    if litros > 20:
        print('Voçê tem 6% de desconto!')
        d1 = preço * litros
        d2 = d1 - (d1*0.06)
        print('O preço ficou R${:.2f}' .format(d2))