#Autor: Pietro Oliveira
#Projeto: Desvio Condicional 

#CRIAÇÃO DAS VARIÁVEIS
nome=input("informe seu nome: ")
telefone=int(input("TELEFONE: "))
cidade=input("Em qual cidade você reside: ")
salario=float(input(" De quanto é o seu salário: "))

#CONDIÇÕES
if salario >1000:
    print(f"{nome},você possui uma renda mensal BOA")
elif salario >700:
    print(f"{nome},você possui uma renda RAZOÁVEL")
elif salario >500:
    print(f"{nome} você possui uma renda mensal BAIXA")
else:
    print(f"{nome} você possui uma renda mensal MUITO BAIXA")
