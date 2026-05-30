#|---AUTOR:PIETRO OLIVEIRA---|
#PROJETO:LOOP WHILE
numero=int(input("digite a tabuada que queira saber: "))
inicio= int(input("digite o valor de inicio: "))
fim=int(input("digite o limite para o programa"))
#contagem e "enquanto"
while inicio <= fim:
    print(f"{numero} x {inicio}= {numero*inicio}")
    inicio=inicio+1
