#Autor:Pietro Oliveira
#introdução ao try except
numero1= input("Digite o primeiro número ")
operacao=input( "digite a operação ")
numero2= input("Digite o segundo número ")

try:
    numero1 =int(numero1)
    numero2=int(numero2)
    if operacao == "+":
        print(numero1+numero2)
    elif operacao == "-":
        print(numero1+numero2)
    elif operacao == "x":
        print(numero1*numero2)
    elif operacao == "/":
        print(numero1/numero2)
except:
    print("É permitido apenas a digitação de números")
    print("verifique a digitação da operação")
