#Arquivo para aprendizado da parte intermediária de python


#funções 
# def saudacao(nome):
#     print(f'oi {nome}')
# saudacao('felipe')

# def soma(a, b, c):
#     print(f'{a=} + {b=} + {c=} | a + b + c = ', a + b + c)
# soma(1, 2, 3)
# soma(c=1, a=2, b=3)

# def soma(a, b, c = None):
#     if c is not None:
#         print(f'{a=} + {b=} + {c=} | a + b + c = ', a + b + c)
#     else:
#         print(f'{a=} + {b=} | a + b = ', a + b)
# soma(1, 2, 3)
# soma(a=2, b=3)

#escopo
# x = 1
# def escopo():
#     global x
#     x = 10
#     def outra_funcao():
#         global x
#         x = 11
#         y = 2
#         print(x, y)
#     outra_funcao()
#     print(x)
# print(x)
# escopo()
# print(x)

#retorno funções
# def soma(x, y):
#     if x > 10:
#         return x
#     return x + y
# soma1 = soma(1, 2)
# soma2 = soma(3, 4)
# print(soma1 + soma2)
# print(soma(11, 4))

#*args
# def soma(*args):
#     total = 0
#     for numero in args:
#         total += numero
#     return total

# soma1 = soma(1,2,3,4,5,6)
# print(soma1)
# print(sum((1,2,3,4,5,6)))
# numeros = 1,2,3,4,5,6
# print(*numeros)
# print(sum(numeros))

# Exercícios com funções
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
# def multiplica(*args):
#     total = 1
#     for numero in args:
#         total = total *  numero
#     return total
# multiplicacao = multiplica(1, 2, 3, 2)
# print(multiplicacao)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
# def par (x):
#     if x % 2 == 0:
#         return 'par'
#     else:
#         return 'ímpar'
# numero = par(1)
# print(numero)

#higher order function
def saudacao(msg, nome):
    return f'{msg}, {nome}!'
def executa(funcao, *args):
    return funcao(*args)
print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)