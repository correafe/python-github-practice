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

#set 
# s1 = set()
# s1 = {'felipe', 1, 2, 3}
# s2 = set('felipe')
# print(s1, s2)
# print(s2)
# print(1 in s1)
# s1.add(7)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()
# s1.discard('Olá mundo')
# s1.discard('Luiz')
# print(s1)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s2 - s1
# s3 = s1 ^ s2
# print(s3)

# Exemplo de uso dos sets
# letras = set()
# while True:
#     letra = input('Digite: ')
#     letras.add(letra.lower())
#     if 'l' in letras:
#         print('PARABÉNS')
#         break
#     print(letras)

"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
# lista_de_listas_de_inteiros = [
#     [1, 1, 3, 4, 5, 6, 7, 8, 9, 10],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]

#o que eu consegui fazer:
# def duplicados ():
#     contadorlista = 0
#     contadoritem = 0
#     for lista in lista_de_listas_de_inteiros:
#         contadorlista += 1

#         for item in lista:
#             print(contadoritem, item)
#             contadoritem += 1
#         contadoritem = 0

#o que era:
# def encontra_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1

#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break

#         numeros_checados.add(numero)

#     return primeiro_duplicado


# for lista in lista_de_listas_de_inteiros:
#     print(
#         lista,
#         encontra_primeiro_duplicado(lista)
#     )

#função lambda
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()
# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])
# exibir(l1)
# exibir(l2)

#lambda complexo
# def executa(funcao, *args):
#     return funcao(*args)
# def soma(x, y):
#     return x + y
# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica
# duplica = cria_multiplicador(2)
# duplica = executa(
#     lambda m: lambda n: n * m,
#     2
# )
# print(duplica(2))
# print(
#     executa(
#         lambda x, y: x + y,
#         2, 3
#     ),
# )
# print(
#     executa(
#         lambda *args: sum(args),
#         1, 2, 3, 4, 5, 6, 7
#     )
# )

#*args e *kwargs
# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
# print(a, b)
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# for chave, valor in pessoa.items():
#     print(chave, valor)
# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }
# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }
# pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)
# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
# def mostro_argumentos_nomeados(*args, **kwargs):
#     print('NÃO NOMEADOS:', args)

#     for chave, valor in kwargs.items():
#         print(chave, valor)
# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)
# configuracoes = {
#     'arg1': 1,
#     'arg2': 2,
#     'arg3': 3,
#     'arg4': 4,
# }
# mostro_argumentos_nomeados(**configuracoes)

#list comprehension
# lista = []
# for numero in range(10):
#     lista.append(numero)
# # print(lista)
# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)

# mapeamento de dados em list comprehension
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]
# # print(novos_produtos)
# print(*novos_produtos, sep='\n')

# import pprint
# def p(v):
#     pprint.pprint(v, sort_dicts=False, width=40)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
# ]
# p(novos_produtos)

# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
# lista = [
#     (x, y)
#     for x in range(3)
#     for y in range(3)
# ]
# lista = [
#     [(x, letra) for letra in 'Luiz']
#     for x in range(3)
# ]
# print(lista)
