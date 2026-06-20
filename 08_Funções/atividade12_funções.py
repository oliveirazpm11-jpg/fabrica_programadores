#AUTOR:PIETRO OLIVEIRA
#PROJETO:LISTAS EM PYTHON
#variaveis:
#            0       1          2         3          4        
contatos=['José\n','Maria\n','Paulo\n','Pedro\n','Julia\n']
print(*contatos)
def adicionar (contatos):
    contatos.append(input("Digite o nome do contato que sera adicionado: ")) #append você adicionou o nome ao ultimo lugar da lista
    print(*contatos)
    adicionar(contatos)
permissao= (input("Deseja remover algum contato (sim-1/n-2)?= "))
        if permissao == 1:
            print("selecionar o contato que deseja remover ")
            def remover (contatos):
                contatos.remove(input("Agora digite o conato que sera removido: "))
                remover(contatos)
                print (*contatos)
        else:
            print("certo,otido dia")
            print(contatos)

