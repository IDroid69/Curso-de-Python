salario = float(input('Digite o salario: '))
if salario >= 1250:
    n1 = salario * 0.1
if salario <= 1250:
    n1 = salario * 0.15
print(('Voçê recebeu um aumento de {}R${:.2f}' .format('\033[0;32m',n1)))
n2 = (n1+salario)
print('{}Agora voçê vai ganhar {}R${:.2f}' .format('\033[0m', '\033[0;32m', n2))