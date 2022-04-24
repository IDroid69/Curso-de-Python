from time import sleep
while True:
    try:
        valor = int(input('Quer ver a tabuada de qual valor? '))
    except ValueError as error:
        print('Error... Voçê só pode digitar um número inteiro.')
        valor = int(input('Quer ver a tabuada de qual valor? '))
            
    if valor < 0:
        break
    print('-='*30)
    for c in range(1, 11):
        print(f'{c} x {valor} = {c*valor}')
    print('-='*30)
    
print('Saindo...')
sleep(3)
print('Até mais!')