nome = 'Everton Coelho'
# nome = nome.removesuffix('Coelho')
# nome = nome.removeprefix('Everton')
nome = nome.ljust(20, '%').rjust(30, '&')
print(nome)
