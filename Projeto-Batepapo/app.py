#Autor:Pietro Oliveira
#Projeto bate papo
import json
from pathlib import Path
from datetime import datetime

import streamlit as st 

ARQUIVO_MENSAGENS = Path("Mensagens.json")

def carregar_mensagens(): #Buscar as mensagens no arquivo
    if not ARQUIVO_MENSAGENS.exists():
        return []
    
    try:
        with open(ARQUIVO_MENSAGENS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        
    except json.JSONDecodeError:
        return []
def salvar_mensagens(mensagens): 
    with open(ARQUIVO_MENSAGENS, "w", encoding="utf-8") as arquivo:
        json.dump(mensagens, arquivo, indent=4, ensure_ascii=False)

def adicionar_mensagem(username, mensagem): #Adicionar mensagem a lista de mensagens
    mensagens = carregar_mensagens()

    horario = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    mensagens.insert(0,{"time": horario,
                         "username": username,
                         "mensagem":mensagem})
    
    salvar_mensagens(mensagens)    print()