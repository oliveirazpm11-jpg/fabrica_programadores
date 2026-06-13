#AUTOR:PIETRO OLIVEIRA
#PROJETO:LISTAS EM PYTHON

#          0        1        2        3        4
nomes =["Pelé","Maradona",'Messi','Ronaldo',"Neymar"] # didico 4   neymar (passou para 5),  ZICO
#EXIBIÇÃO LISTAS
print(*nomes)

#ADICIONANDO UM NOME A LISTA
#PARA RETIRAR AS ASPAS E OS COLCHETES,USE *"ASTERISCOS"
nomes.append ("zico") #append adiciona no final da listas 
print (*nomes)

#ADICIONANDO UM NOME EM UMA POSIÇÃO ESPECIFICA 
nomes.insert(4,"Didico") #"4 representa o local especifico do nome na listas"
print(*nomes)

#modificar uma pessoa da lista
nomes [2]="MBAPPE"
print (*nomes)

#deletar uma pessoa dessa lista por numero
del nomes[2]
print(*nomes)
#removendo o nome por texto
#vai buscar o nome e apagar o primeiro que aparecer 
nomes.remove ("Maradona")
print (*nomes)
#usando o "pop" para mostrar o nome removido
# 0       1      2     3      4
#pelé ronaldo  didico neymar zico
removido = nomes.pop (1)
print (f"após o pop foi removido o nome :{removido}",nomes)
#limpar a listas
nomes.clear()
print(f"após o comando 'clear' a lista é {nomes}")