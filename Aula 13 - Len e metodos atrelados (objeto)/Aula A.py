'''
Len - Quantidade de caracteres
'''
usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)
print(usuario, qtd_caracteres, type(qtd_caracteres))
print()
if qtd_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres.')
else:
    print('Voce foi cadastrado no sistema.')