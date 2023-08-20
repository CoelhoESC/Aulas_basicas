'''
Em python tudo é um objeto, e objeto geralmente tem metodos atrelados
'''
nome = 'Everton'
print(len(nome))
print(nome.__getitem__(2))  # usando o ponto após a variavel, existirá muitos metodos

complexo = complex('1+2j')
print(complexo)
