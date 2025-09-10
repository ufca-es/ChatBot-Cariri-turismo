import json
import random
from GerenciadorPersonalidades import GerenciadorPersonalidades
from historico import addPerguntaList, salvarHistorico, carregarHistorico


def buscar_respostas(pergunta, gerenciador, dados, personalidade_ativa):

    encontrada = False
    e_despedida = False
    resposta_sorteada = ""

    if pergunta.lower() == "mudar":
        gerenciador.trocar_personalidade()
        personalidade_ativa = gerenciador.ativa
        resposta_sorteada = f"Personalidade trocada para {personalidade_ativa.replace('_',' ').title()}"
        return resposta_sorteada

    for item in dados:
        chaves_item = next((v for k, v in item.items() if k.startswith("palavras_chaves")), [])
        if any(chave in pergunta for chave in chaves_item):
            lista_de_respostas = item["respostas"][personalidade_ativa]
            resposta_sorteada = random.choice(lista_de_respostas)
            encontrada = True
            addPerguntaList( pergunta, resposta_sorteada)
            gerenciador.somar_contagem_uso()
            if "tchau" in chaves_item:
                e_despedida = True
            break

    if not encontrada:
        resposta_sorteada = "Desculpe, não consegui compreender sua pergunta."
    
    return resposta_sorteada, e_despedida