numero = input('digite um número inteiro: ')
try:
    intnumero = int(numero)
    if ((intnumero % 2) == 0):
        print(f'{intnumero} é par')
    else: 
        print(f'{intnumero} é ímpar')
except:
    print(f'{numero} não é inteiro')