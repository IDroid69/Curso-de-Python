frase = str(input('Digite uma frase: '))
quant = (len(frase))
frase1 = ' '.join(frase[::-1])
fraseR = frase.replace(' ', '')
frase1R = frase1.replace(' ', '')

if fraseR == frase1R:
    print('Essa frase é palíndromo!')
else:
    print('Essa frase não é palíndromo.')