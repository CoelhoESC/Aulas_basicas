"""
Entrada de dados
"""
nome = input('Qual é o seu nome? ')  # input é entrada de informações ao sistema, pode colocar em uma variavel
idade = input('Qual é sua idade? ')
ano_nasc = 2021 - int(idade)
print()
print(f'O usuário digitou {nome} e o tipo de variavel é {type(nome)}')
print(f'{nome} tem {idade} anos, e nasceu no ano de {ano_nasc}.')
