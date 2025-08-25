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
# duplicados()

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

#dictionay e set comprehension
# produto = {
#     'nome': 'Caneta Azul',
#     'preco': 2.5,
#     'categoria': 'Escritório',
# }
# dc = {
#     chave: valor.upper()
#     if isinstance(valor, str) else valor
#     for chave, valor
#     in produto.items()
#     if chave != 'categoria'
# }
# lista = [
#     ('a', 'valor a'),
#     ('b', 'valor a'),
#     ('b', 'valor a'),
# ]
# dc = {
#     chave: valor
#     for chave, valor in lista
# }
# s1 = {2 ** i for i in range(10)}
# print(s1)

#isintance, verificar tipo
# lista = [
#     'a', 1, 1.1, True, [0, 1, 2], (1, 2),
#     {0, 1}, {'nome': 'Luiz'},
# ]
# for item in lista:
#     if isinstance(item, set):
#         print('SET')
#         item.add(5)
#         print(item, isinstance(item, set))
#     elif isinstance(item, str):
#         print('STR')
#         print(item.upper())
#     elif isinstance(item, (int, float)):
#         print('NUM')
#         print(item, item * 2)
#     else:
#         print('OUTRO')
#         print(item)

#truthy falsy
# lista = []
# dicionario = {}
# conjunto = set()
# tupla = ()
# string = ''
# inteito = 0
# flutuante = 0.0
# nada = None
# falso = False
# intervalo = range(0)
# def falsy(valor):
#     return 'falsy'if not valor else 'truthy'
# print(f'TESTE', falsy('TESTE'))
# print(f'{lista=}', falsy(lista))
# print(f'{dicionario=}', falsy(dicionario))
# print(f'{conjunto=}', falsy(conjunto))
# print(f'{tupla=}', falsy(tupla))
# print(f'{string=}', falsy(string))
# print(f'{inteito=}', falsy(inteito))
# print(f'{flutuante=}', falsy(flutuante))
# print(f'{nada=}', falsy(nada))
# print(f'{falso=}', falsy(falso))
# print(f'{intervalo=}', falsy(intervalo))

# dir, hasattr e getattr
# string = 'Luiz'
# metodo = 'strip'
# if hasattr(string, metodo):
#     print('Existe upper')
#     print(getattr(string, metodo)())
# else:
#     print('Não existe o método', metodo)

# Generator expression, Iterables e Iterators
# import sys
# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iter(iterable)  # tem __iter__ e __next__
# lista = [n for n in range(1000000)]
# generator = (n for n in range(1000000))
# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))
# print(generator)
# for n in generator:
#     print(n)

#Generator functions
# generator = (n for n in range(1000000))
# def generator(n=0, maximum=10):
#     while True:
#         yield n
#         n += 1
#         if n >= maximum:
#             return
# gen = generator(maximum=1000000)
# for n in gen:
#     print(n)
# def gen1():
#     print('COMECOU GEN1')
#     yield 1
#     yield 2
#     yield 3
#     print('ACABOU GEN1')
# def gen3():
#     print('COMECOU GEN3')
#     yield 10
#     yield 20
#     yield 30
#     print('ACABOU GEN3')
# def gen2(gen=None):
#     print('COMECOU GEN2')
#     if gen is not None:
#         yield from gen
#     yield 4
#     yield 5
#     yield 6
#     print('ACABOU GEN2')
# g1 = gen2(gen1())
# g2 = gen2(gen3())
# g3 = gen2()
# for numero in g1:
#     print(numero)
# print()
# for numero in g2:
#     print(numero)
# print()
# for numero in g3:
#     print(numero)
# print()

#try exception 
# a = 18
# b = 0
# c = a / b
# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError:
#     print('Dividiu por zero.')
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError):
#     print('TypeError + IndexError')
# except Exception:
#     print('ERRO DESCONHECIDO.')
# print('CONTINUAR')
# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     # print('Linha 1'[1000])
#     c = a / b
#     print('Linha 2')
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Nome b não está definido')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO.')
# print('CONTINUAR')

# try, except, else e finally
# try:
#     print('ABRIR ARQUIVO')
#     8/0
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
#     print('DIVIDIU ZERO')
# except IndexError as error:
#     print('IndexError')
# except (NameError, ImportError):
#     print('NameError, ImportError')
# else:
#     print('Não deu erro')
# finally:
#     print('FECHAR ARQUIVO')

# raise - lançando exceções (erros)
# def nao_aceito_zero(d):
#     if d == 0:
#         raise ZeroDivisionError('Você está tentando dividir por zero')
#     return True
# def deve_ser_int_ou_float(n):
#     tipo_n = type(n)
#     if not isinstance(n, (float, int)):
#         raise TypeError(
#             f'"{n}" deve ser int ou float. '
#             f'"{tipo_n.__name__}" enviado.'
#         )
#     return True
# def divide(n, d):
#     deve_ser_int_ou_float(n)
#     deve_ser_int_ou_float(d)
#     nao_aceito_zero(d)
#     return n / d
# print(divide(8, '0'))

# import, from, as e *
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys
# platform = 'A MINHA'
# print(sys.platform)
# print(platform)
# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform
# print(platform)
# alias 1 - import nome_modulo as apelido
# import sys as s
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)
# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf
# print(pf)
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem
# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform
# print(platform)
# exit()

# #módulos
# import testemodulo
# print('Este módulo se chama', __name__)
# import testemodulo
# from testemodulo import soma, variavel_modulo
# print('Este módulo se chama', __name__)
# # print('Este módulo se chama', __name__)
# print(testemodulo.variavel_modulo)
# print(variavel_modulo)
# print(soma(2, 3))
# print(testemodulo.soma(2, 3))

# import importlib
# import testemodulo
# print(testemodulo.variavel)
# for i in range(10):
#     importlib.reload(testemodulo)
#     print(i)
# print('Fim')

# from sys import path
# # from sys import path
# import testepackages.modulo
# from testepackages import modulo
# from testepackages.modulo import *
# # import testepackages.modulo
# # from testepackages import modulo
# # from testepackages.modulo import *
# # from testepackages.modulo import soma_do_modulo
# # # from testepackages.modulo import soma_do_modulo
# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(testepackages.modulo.soma_do_modulo(1, 2))
# print(modulo.soma_do_modulo(1, 2))
# print(variavel)
# print(nova_variavel)
# # # print(*path, sep='\n')
# # print(soma_do_modulo(1, 2))
# # print(testepackages.modulo.soma_do_modulo(1, 2))
# # print(modulo.soma_do_modulo(1, 2))
# # print(variavel)
# # print(nova_variavel)
# from testepackages.modulo import fala_oi, soma_do_modulo
# print(__name__)
# fala_oi()

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

# #como eu fiz:
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.10}
#     for produto in produtos
# ]
# print(*novos_produtos, sep='\n')
# produtos_ordenados_por_nome = sorted(produtos, key=lambda item: item['nome'], reverse=True)
# print(produtos_ordenados_por_nome)
# produtos_ordenados_por_preco = sorted(produtos, key=lambda item: item['preco'])
# print(produtos_ordenados_por_preco)

#como era:
# import copy
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]
# novos_produtos = [
#     {**p, 'preco': round(p['preco'] * 1.1, 2)}
#     for p in copy.deepcopy(produtos)
# ]
# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['nome'],
#     reverse=True
# )
# produtos_ordenados_por_preco = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['preco']
# )
# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')
# print()
# print(*produtos_ordenados_por_preco, sep='\n')

# Exercício - Adiando execução de funções
# def soma(x, y):
#     return x + y
# def multiplica(x, y):
#     return x * y
# def criar_funcao(funcao, x):
#     def interna(y):
#         return funcao(x, y)
#     return interna
# soma_com_cinco = criar_funcao(soma, 5)
# multiplica_por_dez = criar_funcao(multiplica, 10)
# print(soma_com_cinco(10))
# print(multiplica_por_dez(10))

#variaveis livre e nonlocal
# def concatenar(string_inicial):
#     valor_final = string_inicial

#     def interna(valor_a_concatenar=''):
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final
#     return interna
# c = concatenar('a')
# print(c('b'))
# print(c('c'))
# print(c('d'))
# final = c()
# print(final)

# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)
# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Vou te decorar')
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         print(f'O seu resultado foi {resultado}.')
#         print('Ok, agora você foi decorada')
#         return resultado
#     return interna
# @criar_funcao #açucar sintatico, chama função para outra função
# def inverte_string(string):
#     print(f'{inverte_string.__name__}')
#     return string[::-1]
# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string')
# invertida = inverte_string('123')
# print(invertida)

#sem decorador seria:
# def inverte_string(string):
#     return string[::-1]
# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string')
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')
# print(invertida)

#decoradores com parâmetros
# def fabrica_de_decoradores(a=None, b=None, c=None):
#     def fabrica_de_funcoes(func):
#         print('Decoradora 1')
#         def aninhada(*args, **kwargs):
#             print('Parâmetros do decorador, ', a, b, c)
#             print('Aninhada')
#             res = func(*args, **kwargs)
#             return res
#         return aninhada
#     return fabrica_de_funcoes
# @fabrica_de_decoradores(1, 2, 3)
# def soma(x, y):
#     return x + y
# decoradora = fabrica_de_decoradores()
# multiplica = decoradora(lambda x, y: x * y)
# dez_mais_cinco = soma(10, 5)
# dez_vezes_cinco = multiplica(10, 5)
# print(dez_mais_cinco)
# print(dez_vezes_cinco)

# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#o que eu consegui fazer:
# lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lista2 = ['BA', 'SP', 'MG', 'RJ']
# def zipper(x, y):
#     contador1 = 0
#     contador2 = 0
#     for item1 in x:
#         for item2 in y:
#             if contador1 == contador2:
#                 print(lista1[contador1], lista2[contador2])
#             else:
#                 print('diferente')
#             contador2 =+ 1
#         contador1 += 1
#         print(contador1, contador2)
# zipper(lista1, lista2)

# o que era:
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
# from itertools import zip_longest
# l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# l2 = ['BA', 'SP', 'MG', 'RJ']
# print(list(zip(l1, l2)))
# print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))

"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

#como eu fiz:
# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = [1, 2, 3, 4, 10]
# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i] + l2[i]) for i in range(intervalo)]
# print(zipper(l1, l2))

#como podia ser:
# lista_a = [10, 2, 3, 40, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(lista_soma)
# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)
# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# count é um iterador sem fim (itertools)
# from itertools import count
# c1 = count(step=8, start=8)
# r1 = range(8, 100, 8)
# print('c1', hasattr(c1, '__iter__'))
# print('c1', hasattr(c1, '__next__'))
# print('r1', hasattr(r1, '__iter__'))
# print('r1', hasattr(r1, '__next__'))
# print('count')
# for i in c1:
#     if i >= 100:
#         break

#     print(i)
# print()
# print('range')
# for i in r1:
#     print(i)

# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
# from itertools import combinations, permutations, product
# def print_iter(iterator):
#     print(*list(iterator), sep='\n')
#     print()
# pessoas = [
#     'João', 'Joana', 'Luiz', 'Letícia',
# ]
# camisetas = [
#     ['preta', 'branca'],
#     ['p', 'm', 'g'],
#     ['masculino', 'feminino', 'unisex'],
#     ['algodão', 'poliéster']
# ]
# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
# print_iter(product(*camisetas))

# groupby - agrupando valores (itertools)
# from itertools import groupby
# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'A'},
#     {'nome': 'Anderson', 'nota': 'C'},
# ]
# def ordena(aluno):
#     return aluno['nota']
# alunos_agrupados = sorted(alunos, key=ordena)
# grupos = groupby(alunos_agrupados, key=ordena)
# for chave, grupo in grupos:
#     print(chave)
#     for aluno in grupo:
#         print(aluno)

# map, partial, GeneratorType e esgotamento de Iterators
# from functools import partial
# from types import GeneratorType
# # map - para mapear dados
# def print_iter(iterator):
#     print(*list(iterator), sep='\n')
#     print()
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]
# def aumentar_porcentagem(valor, porcentagem):
#     return round(valor * porcentagem, 2)
# aumentar_dez_porcento = partial(
#     aumentar_porcentagem,
#     porcentagem=1.1
# )
# # novos_produtos = [
# #     {**p,
# #         'preco': aumentar_dez_porcento(p['preco'])}
# #     for p in produtos
# # ]
# def muda_preco_de_produtos(produto):
#     return {
#         **produto,
#         'preco': aumentar_dez_porcento(
#             produto['preco']
#         )
#     }
# novos_produtos = list(map(
#     muda_preco_de_produtos,
#     produtos
# ))
# print_iter(produtos)
# print_iter(novos_produtos)
# print(
#     list(map(
#         lambda x: x * 3,
#         [1, 2, 3, 4]
#     ))
# )

# filter é um filtro funcional
# def print_iter(iterator):
#     print(*list(iterator), sep='\n')
#     print()
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]
# def filtrar_preco(produto):
#     return produto['preco'] > 100
# # novos_produtos = [
# #     p for p in produtos
# #     if p['preco'] > 100
# # ]
# novos_produtos = filter(
#     # lambda produto: produto['preco'] > 100,
#     filtrar_preco,
#     produtos
# )
# print_iter(produtos)
# print_iter(novos_produtos)

# reduce - faz a redução de um iterável em um valor
# from functools import reduce
# produtos = [
#     {'nome': 'Produto 5', 'preco': 10},
#     {'nome': 'Produto 1', 'preco': 22},
#     {'nome': 'Produto 3', 'preco': 2},
#     {'nome': 'Produto 2', 'preco': 6},
#     {'nome': 'Produto 4', 'preco': 4},
# ]
# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']
# total = reduce(
#     lambda ac, p: ac + p['preco'],
#     produtos,
#     0
# )
# print('Total é', total)
# total = 0
# for p in produtos:
#     total += p['preco']
# print(total)
# print(sum([p['preco'] for p in produtos]))

#recursividade 
# def recursiva(inicio=0, fim=4):
#     print(inicio, fim)
#     # Caso base
#     if inicio >= fim:
#         return fim
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)
# print(recursiva())

# def fatorial(n):
#     if n <= 1:
#         return 1
#     return n * fatorial(n - 1)
# print(fatorial(3))

# ambientes virtuais
# python -m venv venv
# .\venv\bin\Activate.ps1
# deactivate
# git add .
# git commit -m "testando pelo notebook"
# git push
# pip - instalando pacotes e bibliotecas
# Instalar última versão:
# pip install nome_pacote
# Instalar versão precisa
# (tem outras formas também não mencionadas)
# pip install nome_pacote==0.0.0
# Desinstalar pacote
# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze

# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt

# Criando arquivos com Python + Context Manager with
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# caminho_arquivo = 'teste.txt'
# # arquivo = open(caminho_arquivo, 'w')
# # #
# # arquivo.close()
# with open(caminho_arquivo, 'w') as arquivo:
#     print('Olá mundo')
#     print('Arquivo vai ser fechado')
# import os
# caminho_arquivo = 'teste.txt'
# with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
#     arquivo.write('Atenção\n')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
# print('#' * 10)
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())
# os.remove(caminho_arquivo) # ou unlink
# os.rename(caminho_arquivo, 'aula116-2.txt')

#json
# import json
# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }
# with open('testejson.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#     )
# with open('testejson.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     # print(pessoa)
#     # print(type(pessoa))
#     print(pessoa['nome'])

# Problema dos parâmetros mutáveis em funções Python
# def adiciona_clientes(nome, lista=None):
#     if lista is None:
#         lista = []
#     lista.append(nome)
#     return lista
# cliente1 = adiciona_clientes('luiz')
# adiciona_clientes('Joana', cliente1)
# adiciona_clientes('Fernando', cliente1)
# cliente1.append('Edu')
# cliente2 = adiciona_clientes('Helena')
# adiciona_clientes('Maria', cliente2)
# cliente3 = adiciona_clientes('Moreira')
# adiciona_clientes('Vivi', cliente3)
# print(cliente1)
# print(cliente2)
# print(cliente3)

# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


# while True:
#     print('comandos: listar, refazer, desfazer')
#     resposta = input('digite uma tarefa ou um comando: ')
#     resposta1 = adicionaitens(resposta)
#     adicionaitens(resposta, resposta1)
#     print(resposta1)
#     # cliente1 = adiciona_clientes('luiz')
#     # adiciona_clientes('Joana', cliente1)

#o que eu fiz:
# def adicionaitens(item, lista = []):
#     if lista is None:
#         lista = []
#     lista.append(item)
#     return lista
# while True:
#     print('comandos: listar, refazer, desfazer')
#     item = input('digite uma tarefa ou um comando: ')

#     if item == 'listar':
#         if item1 == []:
#             print('não há itens')
#         print(item1)
#     elif item == 'refazer':
#         print(item)
#     elif item == 'desfazer':
#         print(item1)
#     elif item1 == []:
#         print('não há itens')
#     else:
#         item1 = adicionaitens(item)
#         print(item1)

#o que era:
# import os
# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()

# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'clear':
#         os.system('clear')
#         continue
#     else:
#         adicionar(tarefa, tarefas)
#         listar(tarefas)
#         continue

#outra forma:
# import os

# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()

# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()
#     listar(tarefas)

# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)

# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)

# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()

#outra forma:
# import json
# import os

# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()

# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()
#     listar(tarefas)

# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)

# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)

# def ler(tarefas, caminho_arquivo):
#     dados = []
#     try:
#         with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
#             dados = json.load(arquivo)
#     except FileNotFoundError:
#         print('Arquivo não existe')
#         salvar(tarefas, caminho_arquivo)
#     return dados

# def salvar(tarefas, caminho_arquivo):
#     dados = tarefas
#     with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#         dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
#     return dados

# CAMINHO_ARQUIVO = 'aula119.json'
# tarefas = ler([], CAMINHO_ARQUIVO)
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()
#     salvar(tarefas, CAMINHO_ARQUIVO)

# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/
# def soma(a, b, /, *, c, **kwargs):
#     print(kwargs)
#     print(a + b + c)
# soma(1, 2, c=3, nome='teste')