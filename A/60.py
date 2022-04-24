import random
print('Olá! tente adivinhar o número de 0 a 5 que eu vou pensar.')
n1 = (random.randrange(0,5))
acertou = False
tentativas = 0
while not acertou:
    n0 = int(input('Digite um número de 0 a 5: '))
    tentativas += 1
    if n0 == n1:
        acertou = True
    else:
        if n0 > n1:
            print('Menos... tente novamente.')
        elif n0 < n1:
            print('Mais... tente novamente.')
print('Parabéns voçê acertou com {} tentativas' .format(tentativas))
