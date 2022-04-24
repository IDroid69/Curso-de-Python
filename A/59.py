r = ''
while r != 'F' and r != 'M':
    r = str(input('Digite o sexo [F/M]: ')).upper()
    if r != 'F' and r != 'M':
        print('[error] Tente novamente.')
print('fim')
