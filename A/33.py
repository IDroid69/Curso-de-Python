import datetime
ano = int(input('Que ano quer analisar? (coloque 0 para analisar o ano atual: '))
n1 = datetime.datetime.now()
date = n1.date()
if ano == 0:
    ano = date.year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!' .format(ano))
else:
    print('O ano {} não é bissexto!' .format(ano))