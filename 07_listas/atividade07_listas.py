#AUTOR:PIETRO OLIVEIRA
#PROJETO:LISTAS EM PYTHON
#variaveis:
#        0     1    2     3     4
nome=['José','Maria','Paulo','Pedro','Julia']
print(*nome)
nome.append("Nicolas") #append você adicionou o nome ao ultimo lugar da lista
print(*nome)
#agora vc pode remover alguém especifico da listas basta apenasa indicar o indice(numero em que esta)
del nome [2]
print(*nome)