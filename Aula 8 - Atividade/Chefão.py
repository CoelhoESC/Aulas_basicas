"""
Criar variaveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
Criar variavel com o ano atual (int)
Obter o ano de nascimento da pessoa pela idade e ano atual
Obter o Imc da pessoa com altura e peso
Exibir o texto com todas as informações usando F-strings
"""
print('Informações de uma pessoa')
Nome = str(input('Nome: '))
Idade = int(input('Idade:'))
Altura = float(input('Altura:'))
Peso = input('Peso kg:').replace(',', '.')
Peso = float(Peso)
Ano = 2021
Data_Nasc = Ano - Idade
Imc = Peso / (Altura ** 2)
print(f'{Nome} tem {Idade} anos e nasceu no ano {Data_Nasc}, sua altura é {Altura} e seu peso {Peso}Kg,'
      f' seu imc {Imc:.2f}')
