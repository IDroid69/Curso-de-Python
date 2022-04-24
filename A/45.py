import random
from time import sleep
print('=-'*20)
print('Bem vindo jogador(a)!')
print('=-'*20)
pedra = ('0')
papel = ('1')
tesoura = ('2')
cartas = (pedra, papel, tesoura)
print('SUAS OPÇÕES:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA ')
j1 = input('DIGITE SUA JOGADA: ')
pc = random.choice(cartas)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if j1 == pedra and pc == tesoura:
    print('Voçê jogou Pedra')
    print('O computador jogou Papel')
    print('O computador venceu!')
elif j1 == papel and pc == tesoura:
    print('Voçê jogou Papel')
    print('O computador jogou Tesoura')
    print('O computador venceu!')
elif j1 == tesoura and pc == pedra:
    print('Voçê jogou Tesoura')
    print('O computador jogou Pedra')
    print('O computador venceu!')
elif pc == pedra and j1 == papel:
    print('O computador jogou Pedra')
    print('Voçê jogou Papel')
    print('Voçê venceu!')
elif pc == papel and j1 == tesoura:
    print('O computador jogou Papel')
    print('Voçê jogou Tesoura')
    print('Voçê venceu!')
elif pc == tesoura and j1 == pedra:
    print('O computador jogou Tesoura')
    print('Voçê jogou Pedra')
    print('Voçê venceu!')
else:
    print('Os dois jogou a mesma carta.')
    print('Deu empate!')
