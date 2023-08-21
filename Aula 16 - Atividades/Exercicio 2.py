"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada
Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
print('Comprimentando você pelas horas!')
horas = input('Que horas são agora: ').lower().strip().replace(':', '.').replace('h', '.')
horas = float(horas)
if 0 <= horas <= 11:
    print('Bom dia, agora são', end=' ')
    if horas < 5:
        horas = str(horas).replace('.', ':').ljust(4, '0')
        print(f'{horas} da madrugada!')
    else:
        horas = str(horas).replace('.', ':').ljust(4, '0')
        print(f'{horas:.5s} da manhã!')
elif 12 <= horas <= 17:
    horas = str(horas).replace('.', ':').ljust(5, '0')
    print(f'Boa tarde, agora são {horas} da tarde!')
elif 18 <= horas <= 23:
    horas = str(horas).replace('.', ':').ljust(5, '0')
    print(f'Boa noite, agora são {horas} da noite!')
