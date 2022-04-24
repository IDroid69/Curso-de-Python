n = cont = soma = 0
n = int(input('Digite o número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite o número [999 para parar]: '))
print('Voçê digitou {} números e a soma entre eles é {}' .format(cont, soma))
