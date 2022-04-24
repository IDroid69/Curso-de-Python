num = int(input('Digite um número: '))
print('''Escolha uma das bases de conversão:
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Sua escolha: '))
if opcao == 1:
    print('{} Convertido para Binario é igual a {}' .format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é igual a {}' .format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a {}' .format(num, hex(num)[2:]))
