"""
Tipos de dados
Str - string - Textos 'aspa simples' ou "aspa duplas"
Int - inteiro - 12345, 0, -10, -20, -1000...
Float - real/ponto flutuante - N° com ponto 10.50, -8.5, 0.0...
Bool - booleano/logico - True/False - Irá ver valores bool, quando está comparando algo ex: 10 == 10
"""
print('Algo', type('Algo'))  # Retorna qual tipo desse valor
print('123', type(123))
print('25.23', type(25.23))
print('10 == 10', type(10 == 10))
print('10 == 20', type(10 == 20))
print("'l' == 'l'", type('l' == 'l'))
print(bool(''), bool(0), bool([]))  # Me retorna tudo em False
print('-' * 30)
# Pode converte um tipo em outro tipo
print('Luiz', type('Luiz'), bool('Luiz'))
print('10', type('10'), type(int('10')))
