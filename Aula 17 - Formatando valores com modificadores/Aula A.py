"""
Formando valores com modificadores

:s - texto
:d - inteiro
:f - N° de ponto flutuante
:.(n°)f - Quantidade de casas decimais
:(caractere)(> ou < ou ^)(quantidade)(tipo- s, d, e f)
"""
num_1 = 10
num_2 = 3

# :.2f
divisao = num_1 / num_2
print(f'{divisao:.2f}')
print(f'{1154:.4f}')

# :s
nome = 'Everton Coelho'
print(f'{nome:.5s}')

# :d
Soma = num_1 + num_2
print(f'{Soma:^10d}')

# (caracteres)
print(f'{num_2:0>10}')
print(f'{num_2:0<10}')
print(f'{1157:0^10}')

# Pode combinas :.2f com :(caracteres)
print(f'{num_2:0>10.2f}')

# Pode usar com str, usando len para saber quantidade de carecteres
print(len(nome) - 20)
print(f'{nome:=^20}')

# Posso guarda a formatação dentro de uma variavel!
Nome_Formatado = f'{nome:$<20}'
print(Nome_Formatado)
