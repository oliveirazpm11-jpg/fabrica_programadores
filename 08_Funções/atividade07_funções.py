#Autor:Pietro Oliveira 
#Projeto: Função IMC com input e f´string

#variaveis apresentadas
peso= float(input("digite seu peso em KG:  "))
altura = float(input("Digite sua altura em metros (use ponto ao invés de virgula): "))
def calcular_imc(peso,altura):
    imc = peso/(altura * altura  )
    print(f"Seu IMC é: {imc:.2f}")

calcular_imc (peso,altura)