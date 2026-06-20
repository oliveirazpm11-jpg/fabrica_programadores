#|---AUTOR:PIETRO OLIVEIRA---|
#PROJETO:LOOP WHILE
numero=int(input("digite a tabuada que queira saber: "))
inicio= int(input("digite o valor de inicio: "))
fim=int(input("digite o limite para o programa "))
#contagem e "enquanto"
#ENQUANTO inicio FOR MENOR OU IGUAL A fim você continua 
def loop_while(inicio,fim):
    while inicio <= fim:
        print(f"{numero} x {inicio}= {numero*inicio}")
        inicio=inicio+1
loop_while(inicio,fim)