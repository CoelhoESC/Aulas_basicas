'''
Operadores logicos
and, or, not, in e not in
'''
comp1 = comp2 = 0

# Verdadeiro E Verdadeiro = True
var = comp1 and comp2

# Verdadeiro Ou verdadeiro = True
var_2 = comp1 or comp2

# not é um inversor, se utiliza bastante com variaveis vazias ou 0
a = ''
b = 0
if not a:  # Sem o not iria retorna FALSE
    print('Preencha o valor de A', type(a), bool(a), bool(not a))

# in, faz comparações de letrar e número, para ver se existe, em determinada variavel!
nome = 'Everton Coelho'
if 'v' in nome:
    print('Existe!')
else:
    print('Não existe!')

# not in, inverti a expressão!
if 'n' not in nome:
    print('Não existe o texto!')
else:
    print('Executa!')
