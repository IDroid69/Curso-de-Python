vcarro = float(input('Qual a velocidade atual do carro: '))
if vcarro >80:
    print('MULTADO! Voçê excedeu o limite maximo permitido de 80km/h')
    multa = (vcarro - 80) * 7
    print('Voçê recebeu uma multa de {:.2f}' .format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
