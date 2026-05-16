#Autor:Pietro Oliveira 
#desvio condicionais 

#variáveis
nome=input("digite seu nome ")
salario= float(input("informe seu salário "))
caulculo= salario * 0.10
if caulculo > 100:
    print(f"O usuário {nome} tem dinheiro")
else:
    print(f"O usuário {nome} não tem dinheiro")