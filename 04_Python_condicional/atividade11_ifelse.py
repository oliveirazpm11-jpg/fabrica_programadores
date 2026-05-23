#Autor: Pietro Oliveira
#Projeto: Desvio Condicional 

#CRIAÇÃO DAS VARIÁVEIS
nome=input("DIGA O NOME DO ALUNO: ")
nota1=float(input("DIGITE A PRIMEIRA NOTA DO ALUNO "))
nota2=float(input("DIGITE A SEGUNDA NOTA DO ALUNO  "))
nota3=float(input("DIGITE A TERCEIRA NOTA DO ALUNO "))
#CALCULO DA MÉDIA
media=(nota1+nota2+nota3)/3
resultado=print(f"A média do(a) estudante em questão é: {media}")
#CONDIÇÕES 
if media >= 7:
    print(f"O(a) estudante {nome} está: APROVADO(A)")
elif media > 4:
    print(f"Devido a média o estudante {nome} está em RECUPERAÇÃO")
else:
    print(f"O(a) estudante {nome} será: REPROVADO")
