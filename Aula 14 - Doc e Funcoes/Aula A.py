"""
Documentação e funções
"""
# isnumeric, isdigit, isdecimal
num1 = input('Digite um n°: ')
num2 = input('Digite outro n°: ')
Nome = input("Digite seu nome: ")

# Números e positivos (123456...)
print(num1.isnumeric())  # Retorna um valor Boolean
print(num2.isnumeric())
print(num1.isdigit())
print(num2.isdigit())
print(num1.isdecimal())
print(num2.isdecimal())
print(Nome.ljust(20, "*"))

if num1.isdigit() and num2.isdigit():
    num1 = int(float(num1))
    num2 = int(float(num2))
    print(num1 + num2)
else:
    print('Não pode converter os n° para somar!')
