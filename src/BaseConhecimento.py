import json
import random

"""Módulo que gerencia a base de conhecimento do chatbot a partir de um JSON."""

class BaseConhecimento():
    def __init__(self,caminho_arquivo):
        """Inicializa a classe, carregando os dados do arquivo JSON."""
        try:
               with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                self.dados = json.load(arquivo)
        except FileNotFoundError:
            print(f"ERRO: Arquivo de conhecimento '{caminho_arquivo}' não foi encontrado.")
            self.dados = []
    def buscar_palavras_e_blocos(self, pergunta_usuario, personalidade):
        """Busca uma resposta no JSON com base em palavras chaves na pergunta do usuário e na personalidade ativa."""
        pergunta_usuario = pergunta_usuario.lower()

        # Percorre todos os items do array ate encontrar uma pergunta semelhante 
        for bloco in self.dados:

            # pegar palavras-chave de cada item do array 
            chaves = next((v for k, v in bloco.items() if k.startswith("palavras_chaves")), [])  

            # Comparar as palavras da pergunta com as palavras-chave
            if any(chave.strip() in pergunta_usuario for chave in chaves):
                lista_respostas = bloco["respostas"][personalidade]
                return chaves, random.choice(lista_respostas)
        
        return None, None