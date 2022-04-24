import random
print('Olá! tente adivinhar o número de 0 a 5 que eu vou pensar.')
n0 = int(input('Digite um número de 0 a 5: '))
n1 = (random.randrange(0,5))
if n0 == n1:
    print('Parabéns! voçê acertou!')
else:
    print('Voçê errou.')
print('A resposta era {}' .format(n1))
