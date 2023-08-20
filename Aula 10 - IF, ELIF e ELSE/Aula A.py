"""
Condições IF, ELIF e ELSE
"""
if False:  # Se for falso, executa o else
    print('Verdadeiro')
elif True:
    print('Agora é verdadeiro')
    nome = input('Qual é o seu nome ').strip()  # Posso adicionar varios codigoes, respeitando o bloco verdadeiro
    print(f'Seu nome é {nome}')
elif False:
    print('Mais uma verdadeira')
else:
    print('A minha expressão não é verdadeira')
# Irá me retorna um valor booleando True ou False
