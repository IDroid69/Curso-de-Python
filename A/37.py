casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos voçê pretende pagar? '))
prestação = casa / (anos*12)
minimo = salario * 0.3
print('{}Para pagar uma casa de {}R${:.2f} {}em {} anos' .format('\033[0m', '\033[0;32m' ,casa, '\033[0m' ,anos,))
print('{}A prestação será de {}R${:.2f}' .format('\033[0m', '\033[0;32m' ,prestação))
if prestação <= minimo:
    print('{}Financiamento {}CONCEDIDO!' .format('\033[0m', '\033[0;32m'))
else:
    print('{}Financiamento {}NEGADO!' .format('\033[0m', '\033[0;31m'))
