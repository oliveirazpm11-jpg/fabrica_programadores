#Autor: Pietro Oliveira
#Projeto: Desvio Condicional 

#Criação das variáveis
nome=input('Me diga seu nome: ')
nota=float(input('digite a nota final: '))
if nota>=6:
    print(f'Aluno {nome} esta: APROVADO')
else:
    print(f'Aluno {nome} esta: REPROVADO')