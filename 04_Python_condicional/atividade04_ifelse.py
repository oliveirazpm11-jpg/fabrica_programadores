#Autor: Pietro
#desvio condicionais

 #variáveis
nome=input('Olá,me diga seu nome? ')
idade=int(input(f"Agora me diga {nome},quantos anos você tem? "))
print(f'{nome} você possui carteira de motorista? ')
#Print pode ou não dirigir
carteira=input(" possui carteira de motorista ? sim ou não? ")
if carteira == "sim":
   print(f"O usuário {nome} tem permissão para dirigir um veiculo ")
else:
    print(f" O usuário {nome} NÃO tem permissão para dirigir")