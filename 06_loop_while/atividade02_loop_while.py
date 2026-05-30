#|---AUTOR:PIETRO OLIVEIRA---|
#PROJETO:LOOP WHILE

#inserir os dados
numero= int(input("digite o numero que deseja que seja multiplicado: "))
i=1
# ENQUANTO i FOR MENOR OU IGUAL A 10,ELE CONTINUARÁ REALIZANDO A FÓRMULA
while i <= 10:
    #saida de informações
    print(f"{numero} x {i} = {numero*i}")
    i=i+1 #o computador vai ler o código e voltar a fórmula inicial(line 8) e vai adiconar mais +1(iterar)
#ELE VAI IR E VOLTAR NA LEITURA ATÉ O LIMITE ESTABELECIDO 
