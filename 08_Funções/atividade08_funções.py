#Autor:Pietro Oliveira 
#projeto: função com if else
#Criação das variáveis
nome=input('Me diga seu nome: ')
nota=float(input('digite a nota final: '))
def status(nota):
    if nota >= 6:
        print(f" O usuario {nome} esta APROVADO!!! ")
    else:
        print(f" O usuario {nome} esta REPROVADO!!! ")
status(nota)