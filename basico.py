#Arquivo para aprendizado da parte básica de python


#comentários e print
"""docstrings não são comentários"""
## print('oi')
'''docstrings não são comentários'''
# print(12, 34, sep="-", end="\n\n")
# print(15, 27, sep='_')

#tipos de dados
# str int float
# print("felipe")
# print(123)
# print(123.55)
# print(123=="felipe")
# print(type(123=="felipe")) #type mostra o tipo do dado
# print(int('1') + 1, type('1'), type(int('1')))

#variáveis
# numero1 = 1
# print(numero1 + 1, (numero1 + 2) > 2)

#exercicio 
# nome = 'Felipe'
# sobrenome = 'Corrêa'
# idade = 22
# anoNascimento = 2002
# altura = 1.821

# print('Nome:', nome)
# print('Sobrenome:', sobrenome)
# print('Idade:', idade)
# print('Ano de nascimento:', anoNascimento)
# print('É maior de idedade?', idade > 18)
# print('Altura em metros:', altura)

#operadores aritméticos
# + adição, - subtração, * multiplicação, / divisão, // divisão inteira, ** exponenciação, % resto de divisão

# repetição print('felipe ' * 3)

#f-string
# linha1 = f'{nome} tem {altura:.2f} de altura'
# print(linha1)

#método format
# a, b, c = 'A', 'BB', 1.2
# formato = 'a = {1} b = {0} c = {nome3:.3f}'.format(a, b, nome3=c)
# print(formato)

#função input
# nome = input('qual seu nome? ')
# print(f'seu nome é {nome}')
# numero1 = input('digite um número: ')
# numero2 = input('digite outro número: ')
# intnumero1 = int(numero1)
# intnumero2 = int(numero2)
# print(intnumero1 + intnumero2)

#int elif else
# entrada = input('vc quer "entrar" ou "sair"? ')
# if entrada == 'entrar':
#     print('vc entrou')
# elif entrada == "sair":
#     print('vc saiu')
# else:
#     print('vc não digitou entrar nem sair')

# condicao = False
# if condicao:
#     print('true')
# elif condicao:
#     pass
# else:
#     print('false')

#operadores de comparação
#>, >=, <, <=, ==, !=

#exercício
# primeirovalor = input('digite o primeiro valor: ')
# segundovalor = input('digite o segundo valor: ')
# if primeirovalor > segundovalor:
#     print(f'{primeirovalor = } é maior que {segundovalor = }')
# else:
#     print(f'{segundovalor = } é maior que {primeirovalor = }')

#operadores lógicos
#and 
# entrada = input('[E]ntrar [S]air ')
# senhadigitada = input('digite a senha:')
# senhapermiida = 'felipe'
# if entrada == 'E' and senhadigitada == senhapermiida:
#     print('vc entrou')
# else:
#     print('vc saiu')
# print(True and True and False and True)
#or
# entrada = input('[E]ntrar [S]air ')
# senhadigitada = input('digite a senha:')
# senhapermiida = 'felipe'
# if (entrada == 'E' or entrada == 'e') and senhadigitada == senhapermiida:
#     print('vc entrou')
# else:
#     print('vc saiu')
# print(True and True and False and True)
# senha = input('senha: ') or 'sem senha'
# print(senha)
#not
# print(not True)
#in e not in
# nome = "felipe"
# print(nome[0])
# print('o' not in nome)

#interpolação
# s str, d i int, f float, x X hexadecimal
# nome = 'felipe'
# preco = 100.567890
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)
# print('o hexadecimal de  %d é %04x' % (1500, 1500))

#formatação str, < direita, > esquerda, ^ centro
# variavel ='felipe'
# print(f'{variavel: ^100}')
# print(f'{1000.87654567890987654:,.3f}')

#fatiamento de str e função len
# variavel = 'felipe'
# print(variavel[0:6:4])
# print(variavel[0:2:4])
# print(variavel[0:10:2])
# print(variavel[::-1]) #inverte
# print(variavel[4:])
# print(variavel[2:])
# print(len(variavel))

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
# nome = input('digite seu nome: ')
# idade = input('digite sua idade: ')

# if nome and idade:
#     print(f'seu nome é {nome}')
#     print(f'seu nome invertido é {nome[::-1]}')
#     if ' ' in nome:
#         print('seu nome contém espaços')
#     else:
#         print('seu nome não contém espaços')
#     print(f'seu nome tem {len(nome)} letras')
#     print(f'primerira letra do seu nome é {nome[0]}')
#     print(f'última letra do seu nome é {nome[-1]}')
# else:
#     print('vc deixou campos vazios')

#try except
# numerostr = input('dobrar o número: ')
# try:
#     numerofloat = float(numerostr)
#     print('float: ', numerofloat)
#     print(f'o dobro de {numerostr} é {numerofloat * 2} ')
# except:
#     print('isso não é um número')

#contantes 
# CONSTANTE1 = 1

#identidade
# v1 = 'a'
# print(id(v1))

#flag, none, is, is not
# condicao = False
# passou_no_if = None
# if condicao:
#     passou_no_if = True
#     print('Faça algo')
# else:
#     print('Não faça algo')

# if passou_no_if is None:
#     print('Não passou no if')
# else:
#     print('Passou no if')

#exercicio
# numero = input('digite um número inteiro: ')
# try:
#     intnumero = int(numero)
#     if ((intnumero % 2) == 0):
#         print(f'{intnumero} é par')
#     else: 
#         print(f'{intnumero} é ímpar')
# except:
#     print(f'{numero} não é inteiro')

#exercicio
# horario = input('que horas são? ')
# inthorario = int(horario)
# if inthorario >= 0 and inthorario <= 11:
#     print('bom dia')
# elif inthorario >= 12 and inthorario <= 17:
#     print('boa tarde')
# elif inthorario >= 18 and inthorario <= 23:
#     print('boa noite')
# else:
#     print('vc não informou um horário válido')

#exercicio
# nome = input('qual seu primeiro nome ')
# if len(nome) <= 4:
#     print('seu nome é pequeno')
# elif len(nome) >= 5 and len(nome) <= 6:
#     print('seu nome é normal')
# elif len(nome) > 6:
#     print('seu nome é muito grande')
# else:
#     print('vc não informou um nome válido')

#repetições
# condicao = True
# while condicao:
#     nome = input('qual é seu nome? ')
#     print(nome)
#     if nome == 'sair':
#         break
# print('saiu do while')

#operadores de atribuição
#=, +=, -=, *=, /=, **=, //=, %=
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador == 6:
#         print('não vou mostrar o 6')
#         continue
#     print(contador)
#     if contador == 8:
#         break

#while em while
# qtd_linhas = 5
# qtd_colunas = 5
# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1
#     linha += 1
# print('Acabou')

#exercicio
#como eu fiz:
# nome = 'felipe'
# letra = 0 
# numeroletras = len(nome)
# while letra < numeroletras:
#     print(f'*{nome[letra]}*')
#     letra += 1
#como era:
# nome = 'felipe' 
# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1
# novo_nome += '*'
# print(novo_nome)

#exercício calculadora
""" Calculadora com while """
# while True:
#     numero_1 = input('Digite um número: ')
#     numero_2 = input('Digite outro número: ')
#     operador = input('Digite o operador (+-/*): ')
#     numeros_validos = None
#     try:
#         num_1_float = float(numero_1)
#         num_2_float = float(numero_2)
#         numeros_validos = True
#     except:
#         numeros_validos = None
#     if numeros_validos is None:
#         print('Um ou ambos os números digitados são inválidos.')
#         continue
#     operadores_permitidos = '+-/*'
#     if operador not in operadores_permitidos:
#         print('Operador inválido.')
#         continue
#     if len(operador) > 1:
#         print('Digite apenas um operador.')
#         continue
#     ###
#     sair = input('Quer sair? [s]im: ').lower().startswith('s')
#     if sair is True:
#         break

#exercício
# frase = 'felipe'
# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''
# while i < len(frase):
#     letra_atual = frase[i]
#     if letra_atual == ' ':
#         i += 1
#         continue
#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_apareceu_mais_vezes = letra_atual
#     i += 1
# print(
#     'A letra que apareceu mais vezes foi '
#     f'"{letra_apareceu_mais_vezes}" que apareceu '
#     f'{qtd_apareceu_mais_vezes}x'
# )

#for
# texto = 'pytohn'
# novotexto = ''
# for letra in texto:
#     novotexto += f'*{letra}' 
#     print(letra)
# print(novotexto)

#range(start, stop, step)
# numeros = range(5, 19, 2)
# for numero in numeros:
#     print(numero)

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# import os
# palavra_secreta = 'perfume'
# letras_acertadas = ''
# numero_tentativas = 0
# while True:
#     letra_digitada = input('Digite uma letra: ')
#     numero_tentativas += 1

#     if len(letra_digitada) > 1:
#         print('Digite apenas uma letra.')
#         continue
#     if letra_digitada in palavra_secreta:
#         letras_acertadas += letra_digitada
#     palavra_formada = ''
#     for letra_secreta in palavra_secreta:
#         if letra_secreta in letras_acertadas:
#             palavra_formada += letra_secreta
#         else:
#             palavra_formada += '*'
#     print('Palavra formada:', palavra_formada)
#     if palavra_formada == palavra_secreta:
#         os.system('clear')
#         print('VOCÊ GANHOU!! PARABÉNS!')
#         print('A palavra era', palavra_secreta)
#         print('Tentativas:', numero_tentativas)
#         letras_acertadas = ''
#         numero_tentativas = 0

#list
# string = 'dfgbn'
# lista = [112, 'felipe', 1.5, True, 'tadodio', []]
# lista[0] = 'felipe'
# del lista[3]
# print(lista, lista[3])
# lista.append(50)
# print(lista)
# lista.pop()
# print(lista)
# lista1 = [112, 'felipe', 1.5, True, 'tadodio', []]
# print(lista)
# # print(lista.clear())
# lista.insert(0,5)
# print(lista)
# lista2 = [1, 2, 4, 'felipe']
# lista1.extend(lista2)
# lista3 = lista1 + lista2
# print(lista3)
# print(lista1)
# lista2 = lista1.copy()
# print(lista2)

#exercício
# lista = ['Maria', 'Helena', 'Luiz', 123]
# lista.append('João')
# indices = range(len(lista))
# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))

#empacotamento e desempacotamento
# lista = ['Maria', 'Helena', 'Luiz', 123]
# nome1, *_ = ['Maria', 'Helena', 'Luiz', 123]
# nome1, nome2, nome3, nome4= lista
# print(nome2)

#tuplas
# tupla = 'Maria', 'Helena', 'Luiz', 123
# tupla = ('Maria', 'Helena', 'Luiz', 123)
# tupla[2] = 345
# print(tupla)

#enumerate, enumera iteráveis (índices)
# lista = ['Maria', 'Helena', 'Luiz', 123]
# # listaemunerada = enumerate(lista)
# for nome in enumerate(lista):
#     indice, nomes = nome
#     print(indice, nomes)
# for indice, nome in enumerate(lista):
#     print(indice, nome)
# # print(listaemunerada)

#exercicio
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
# import os
# listacompras = []

# while True:
#     print('selecione uma opção:')
#     escolha = input('[i]nserir [a]pagar [l]istar ')

#     if escolha == 'i':
#         os.system('cls')
#         valor = input('valor: ')
#         listacompras.append(valor)

#     elif escolha == 'a':
#         try:
#             indice = input('escolha o indice a apagar: ')
#             indiceint = int(indice)
#             del listacompras[indiceint]
#         except:
#             print('não existe esse índice')

#     elif escolha == 'l':
#         os.system('cls')
#         if listacompras == '':
#             print('não há itens na lista')
#         for indice, nome in enumerate(listacompras):
#             print(indice, nome)

#     else: 
#         print('vc não digitou uma opção válida')

#round e decimal
# import decimal
# numero_1 = decimal.Decimal('0.1')
# numero_2 = decimal.Decimal('0.7')
# numero_3 = numero_1 + numero_2
# print(numero_3)
# print(f'{numero_3:.2f}')
# print(round(numero_3, 2))

#split e join, divide e une string, strip
# frase = 'felipe   felipe  , dois felipes, felipe  '
# print(frase)
# novafrase = frase.split(',')
# print(novafrase)
# lista = []
# # for i, frase in enumerate(frase):
# #     print(novafrase[i].strip())
# for i, frase in enumerate(novafrase):
#     lista.append(novafrase[i].strip())
# print(frase)
# print(lista)
# frasesunidas = '-'.join('lista')
# print(frasesunidas)

#lista de lista
# lista = [['felipe', 'fghjk', 123], ['ghjkl', 67890, 'ghjk', (6, 7, 8)], [345, 'fghk']]
# print(lista[1][3][0])
# for item in lista:
#     print(item)
#     for item2 in item:
#         print(item2)
#         for item3 in item2:
#             print(item3)

#desempacotando em chamada de função
# lista = ['felipe', 'guilherme', 123, 'eu']
# nome = 'felipe'
# print(*nome)
# print(*lista)
# print(*lista, sep='\n')

#operação ternária
# digito = 10
# novodigito = 3 if digito > 7 else digito 
# print(novodigito)

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
# o que eu comecei a fazer:
# cpf = '746824890'
# multiplicador = 11
# indice = -1
# soma = 0
# while indice < 9:
#     while multiplicador > 2:
#         multiplicador -= 1
#         indice += 1
#         numero = cpf[indice]
#         intnumero = int(numero)
#         soma += intnumero * multiplicador
#         soma2 = (soma * 10) % 11
#         soma2 = soma2 if soma2 <= 9 else 0
#         print(soma2)

#o que era
# cpf = '74682489070'
# nove_digitos = cpf[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito_1 in nove_digitos:
#     resultado_digito_1 += int(digito_1) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0
# print(digito_1)

