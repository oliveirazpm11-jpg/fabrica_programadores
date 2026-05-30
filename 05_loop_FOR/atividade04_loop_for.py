#|---AUTOR:PIETRO OLIVEIRA---|
#PROJETO=LOOP FOR- VARIAVEIS DE INICIO E FIM
numero=int(input("digite o número: "))
numero_inicio=int(input("digite o inicio da tabuada: "))
numero_final=int(input("digite o fim da tabuada: "))

for i in range(numero_inicio,numero_final+1):
    print(f"{numero} x {i} = {numero * i}")