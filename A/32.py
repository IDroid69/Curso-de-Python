distancia = float(input('Digite a distancia da viagem: '))
n1 = float(distancia * 0.50)
n2 = float(distancia * 0.45)
if distancia >200:
    print('Sua viajem vai custar R${}' .format(n2))
else:
    print('Sua viajem vai custar R${}' .format(n1))
