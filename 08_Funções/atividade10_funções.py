#Autor:Pietro Oliveira 
#projeto:introduzindo funções a loop for
#TABUADA
numero =int(input("digite o numero que deseja multiplicar "))
n2=int(input('até qual numero deseja multiplicar?:' ))
#função do loop for 
def loop_for (numero,n2):
    for i in range (1,n2+1):
        print(f"{numero} x {i} = {i * numero}")
loop_for(numero,n2)