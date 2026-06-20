#Autor:Pietro Oliveira 
#Projeto: Funções calculadora
#Autor:Pietro Oliveira 
# Projeto: Entradas pelo usuário  
valor1 =float(input('digite o primeiro valor:'))
valor2 = float(input('digite o segundo valor:'))
#função calcular
def calcular (valor1,valor2):
    somar =valor1 +valor2
    subtrair = valor1 - valor2 
    multiplicar = valor1 * valor2  
    dividir = valor1/valor2

    #imprimindo os resultados 
    print(f"O resultado da soma é: {somar}")
    print(f"O resultado da subtração é: {subtrair}")
    print(f"O resultado da multiplicação é: {multiplicar}")
    print(f"O resultado da divisão é: {dividir}")
#Chamda da função
calcular (valor1,valor2)