#autor:Pietro Oliveira 
#desvio condicional

nome=input('Qual seu nome? ')
idade=int(input('Quantos anos você tem? '))
if idade>=18:
    print(f'{nome} é: MAIOR DE IDADE')
else:
    print(f'{nome} ainda é: MENOR DE IDADE')