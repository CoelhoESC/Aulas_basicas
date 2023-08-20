"""
Operadores relacionais
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""

print(2 == 2)  # retornar valor boolean, Retorna TRUE
print(2 == '2')  # Valor int e str não são iguais, retorna FALSE

# Funciona com str também
num_1 = 2
num_2 = 2
expressao_1 = (num_1 > num_2)
expressao_2 = (num_1 >= num_2)
expressao_3 = (num_1 < num_2)
expressao_4 = (num_1 <= num_2)
expressao_5 = (num_1 != num_2)
