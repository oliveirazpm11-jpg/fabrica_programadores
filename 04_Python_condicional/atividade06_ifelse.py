#Autor:Pietro Oliveira 
#desvio condicionais 

#variáveis
nome=input("Me diga seu nome ")
idade=int(input(f"{nome} quantos anos você possui? "))
cidade=str(input("em que cidade você reside? "))
if idade > 12:
    print(f" usuário {nome},residente da cidade:{cidade} você é ADOLESCENTE")
else:
    print(f"{nome}, residente da cidade:{cidade} você é uma CRIANÇA ainda")
