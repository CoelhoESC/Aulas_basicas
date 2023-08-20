"""
Usando F strings, para formatar uma str
"""
nome = 'Everton'
Idade = 22
Altura = 1.80
Peso = 93
Imc = Peso / (Altura * 2)
print(f'{nome} tem {22} anos e seu imc é {Imc:.2f}')

print('{} tem {} anos e seu imc é {:.2f}'.format(nome, Idade, Imc))
print('{i} tem {n} anos e seu imc é {im}'.format(n=nome, i=Idade, im=Imc))  # Pode usar paramentros e modificar a ordem
