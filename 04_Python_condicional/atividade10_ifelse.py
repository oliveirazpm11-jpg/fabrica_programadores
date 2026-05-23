#Autor:Pietro Oliveira 
#desvio condicionais 

#variáveis
nome=input("Olá tudo bem? digite seu nome ")
peso=float(input(f"{nome},agora me diga seu peso em kgs "))
altura=float(input("nos diga sua altura em metros "))
imc=peso/(altura**2)
#CONDIÇÕES
if imc <= 18.5:
    print(F"{nome} você se encontra em estado de : MAGREZA ")
elif imc<= 24.9:
    print(f"{nome} você se encontra em estado de : NORMALIDADE")
elif imc<=29.9:
    print(f"{nome} você se encontra em estado de :SOBREPESO")
elif imc<=39.9:
    print(f"{nome} você se encontra em estado de: OBESIDADE")
else:
    print(f"{nome} você se encontra em estado de: OBESIDADE GRAVE")