"""
Faça um programa que peça ao usuario para digitar um n° inteiro,
informe se este numero é par ou impar.
Caso o usuario não digite um numero inteiro, informe que não é um numero inteiro
"""
print('PAR OU IMPAR')
numero = input('Digite um número inteiro: ')
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é PAR!')
    else:
        print(f'O Número {numero} é IMPAR!')
elif not numero.isdigit():
    if numero.isalpha():
        print('ERRO...Digite um numero inteiro!')
    else:
        numero = int(float(numero))
        print(f'Convertir seu número flutuante para um inteiro ({numero})! ')
        if numero % 2 == 0:
            print(f'O número {numero} é PAR!')
        else:
            print(f'O Número {numero} é IMPAR!')
