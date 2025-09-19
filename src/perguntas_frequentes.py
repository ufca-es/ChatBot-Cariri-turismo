import json
import os

"""Módulo para gerenciar o registro e a contagem de perguntas frequentes."""

path_JSON = "src/data/perguntas_frequentes.json"

# Carrega ou cria o arquivo
def carregar_perguntas():
    """Carrega o dicionário de perguntas frequentes do arquivo JSON."""
    if os.path.exists(path_JSON):
        with open(path_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

# Salva o dicionário no arquivo
def salvar_perguntas(perguntas):
    """Salva o dicionário de perguntas frequentes no arquivo JSON."""
    with open(path_JSON, "w", encoding="utf-8") as f:
        json.dump(perguntas, f, indent=4, ensure_ascii=False)

# Incrementa ou adiciona a pergunta
def registrar_pergunta(pergunta_usuario):
    """Registra e incrementa a contagem de uma pergunta feita pelo usuário."""
    perguntas = carregar_perguntas()
    if pergunta_usuario in perguntas:
        perguntas[pergunta_usuario] += 1
    else:
        perguntas[pergunta_usuario] = 1
    salvar_perguntas(perguntas)

# Retorna as n perguntas mais frequentes
def top_perguntas(n=5):
    """Retorna uma string formatada com as 'n' perguntas mais frequentes."""
    perguntas = carregar_perguntas()
    # Ordena pelo contador decrescente
    total = sorted(perguntas.items(), key=lambda item: item[1], reverse=True)[:n]
    top = [p for p, _ in total]
    if top:
        mensagem = "\n📊 Perguntas mais frequentes:\n" + "\n".join(f"• {p}" for p in top)
    else:
        mensagem = "\n📊 Nenhuma pergunta registrada ainda."
    return f"{mensagem} \n"
