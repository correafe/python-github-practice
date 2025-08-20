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
# def saudacao(msg, nome):
#     return f'{msg}, {nome}!'
# def executa(funcao, *args):
#     return funcao(*args)
# print(
#     executa(saudacao, 'Bom dia', 'Luiz')
# )
# print(
#     executa(saudacao, 'Boa noite', 'Maria')
# )

#closure
# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar
# falar_bom_dia = criar_saudacao('Bom dia')
# falar_boa_noite = criar_saudacao('Boa noite')
# for nome in ['Maria', 'Joana', 'Luiz']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
#como eu fiz:
# def duplicar(x):
#     def triplicar(x):
#         def quadruplicar(x):
#             return f'{x}, {x*4}!'
#         return f'{x}, {x*3}!', quadruplicar(x)
#     return f'{x}, {x*2}!', triplicar(x)

# numero = (duplicar(2))
# print(numero)

#como era:
# def criar_multiplicador(multiplicador):
#     def multiplicar(numero):
#         return numero * multiplicador
#     return multiplicar
# duplicar = criar_multiplicador(2)
# triplicar = criar_multiplicador(3)
# quadruplicar = criar_multiplicador(4)
# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

#dict
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ],
# }
# # print(pessoa, type(pessoa))
# print(pessoa['nome'])
# print(pessoa['sobrenome'])
# print()
# for chave in pessoa:
#     print(chave, pessoa[chave])

#chave
# pessoa = {}
# chave = 'nome'
# pessoa[chave] = 'Luiz Otávio'
# pessoa['sobrenome'] = 'Miranda'
# print(pessoa[chave])
# pessoa[chave] = 'Maria'
# del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])
# # print(pessoa.get('sobrenome'))
# if pessoa.get('sobrenome') is None:
#     print('NÃO EXISTE')
# else:
#     print(pessoa['sobrenome'])

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 900,
# }
# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# for valor in pessoa.values():
#     print(valor)
# for chave, valor in pessoa.items():
#     print(chave, valor)

# import copy
# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }
# d2 = d1.copy()
# d2['c1'] = 1000
# d2['l1'][1] = 999999
# print(d1)
# print(d2)

# p1 = {
#     'nome': 'Luiz',
#     'sobrenome': 'Miranda',
# }
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))
# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]
# p1.update(lista)
# print(p1)

# Exercício - sistema de perguntas e respostas
# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# #como eu fiz
# contador = 0
# n = 0

# for pergunta in perguntas:
#     print('')
#     print(pergunta['Pergunta'])
#     print('Opções: ')

#     for opcoes in pergunta['Opções']:
#         print(f'{n})', opcoes)
#         n += 1

#     n = 0

#     resposta = input('qual é a resposta? ')
#     if resposta == pergunta['Resposta']:
#         contador += 1
#         print('acertou')
#     else:
#         print('errou')

# print('')
# print(f'vc acertou {contador} respostas')

# #como era:
# qtd_acertos = 0
# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')

#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True

#     print()
#     if acertou:
#         qtd_acertos += 1
#         print('Acertou 👍')
#     else:
#         print('Errou ❌')

#     print()


# print('Você acertou', qtd_acertos)
# print('de', len(perguntas), 'perguntas.')


