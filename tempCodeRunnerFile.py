
while True:
    print('selecione uma opção')
    escolha = input('[i]nserir [a]pagar [l]istar ')
    if escolha == 'i':
        valor = input('valor: ')
        listacompras.append(valor)
        print(listacompras)