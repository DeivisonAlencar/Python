primeiro_valor = input('digite o primeiro valor: ')
segundo_valor = input('digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    
    print('o primeiro valor {} é maior que o segundo valor {}'.format(primeiro_valor, segundo_valor))

elif segundo_valor > primeiro_valor:
    
    print('o segundo valor {} é maior que o segundo valor {}'.format(segundo_valor, primeiro_valor))

elif primeiro_valor == segundo_valor:

    print(' o primeiro valor {} é igual ao segundo valor {}'.format(primeiro_valor, segundo_valor))