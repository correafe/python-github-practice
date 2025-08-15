#Arquivo para aprendizado da parte intermediária de python


#funções 
# def saudacao(nome):
#     print(f'oi {nome}')
# saudacao('felipe')

# def soma(a, b, c):
#     print(f'{a=} + {b=} + {c=} | a + b + c = ', a + b + c)
# soma(1, 2, 3)
# soma(c=1, a=2, b=3)

def soma(a, b, c = None):
    if c is not None:
        print(f'{a=} + {b=} + {c=} | a + b + c = ', a + b + c)
    else:
        print(f'{a=} + {b=} | a + b = ', a + b)
soma(1, 2, 3)
soma(a=2, b=3)