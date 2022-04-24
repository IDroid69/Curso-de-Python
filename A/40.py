n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = float(n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f} a media do aluno é: {media:.1f}')
if media < 5:
    print('Voçê foi reprovado.')
elif media >= 5 and media <= 6.9:
    print('Voçê está de recuperação.')
elif media >= 7:
    print('Parabens! Voçê foi aprovado!')