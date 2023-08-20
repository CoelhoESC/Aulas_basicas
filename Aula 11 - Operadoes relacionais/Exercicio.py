nome = input('Qual é o seu nome? ')
idade = int(input('Qual é sua idade? '))
print()
# Limite para pegar emprestimo
idade_menor = 20  # Jovem
idade_maior = 30  # Passou da idade

if idade < idade_menor:  # ou if idade >= idade_menor and idade <= idade_maior
    print(f'{nome} não é maior de idade! ')
    print('Não poderá pegar emprestimo')
if idade > idade_maior:
    print(f'{nome} já passou dos 30 anos!')
else:
    print(f'{nome} é maior de idade! ')
    print('Poderá pegar emprestimo')
