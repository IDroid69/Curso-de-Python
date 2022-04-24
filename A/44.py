valor = float(input('Digite o preço do produto: '))
print('=-'*20)
print('Forma de pagamento...')
print('=-'*20)
print('Digite 1 para pagamento a vista')
print('Digite 2 para pagamento a vista no cartão.')
print('Digite 3 para pagamento em até 2x no cartão.')
print('Digite 4 para pagamento em até 3x no cartão.')
pagamento = str(input('Forma de pagamento: '))
vista = valor - (valor*0.1)
vcartao = valor - (valor*0.05)
dcartao = (valor)
dcartao1 = valor / 2
tcartao = valor + (valor*0.2)
tcartao1 = tcartao / 3
print('O preço é R${:.2f}' .format(valor))
if pagamento == '1':
    print('Com 10% de desconto o valor fica R${:.2f}' .format(vista))
if pagamento == '2':
    print('Com 5% de desconto o valor fica R${:.2f}' .format(vcartao))
if pagamento == '3':
    print('Sem desconto')
    print('Voçê vai pagar 2x de {:.2f}' .format(dcartao1))
if pagamento == '4':
    print('Com 20% de juros o valor fica R${:.2f}' .format(tcartao1))
