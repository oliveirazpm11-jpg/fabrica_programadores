#Autor:Pietro Oliveira 
#desvio condicionais 

#variáveis
nome=input("digite seu nome ")
peso=float(input(f"{nome},agora me diga seu peso em kgs "))
altura=float(input("nos diga sua altura em metros "))
imc=peso/(altura**2)
if imc <18.5:
    print("MAGRO/ABAIXO DO PESO")
else:
    print("PESO NORMAL")