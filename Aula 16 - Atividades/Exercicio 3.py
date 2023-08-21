"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tive 4 letras ou
menos escreva 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva 'Seu nome é normal';
maior que 6 escreva 'Seu nome é muito grande'.
"""
print('Lendo o seu nome!')
nome = str(input('Qual é seu primeiro nome? ')).strip().capitalize()
tam_nome = len(nome)
if tam_nome <= 4:
    print(f'Sr(a). {nome} é curto!')
elif 5 == tam_nome or 6 == tam_nome:
    print(f'Sr(a). {nome} é normal')
else:
    print(f'Sr(a). {nome} é muito grande!')
