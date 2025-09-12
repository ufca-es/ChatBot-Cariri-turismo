import json
import os

path_JSON = "src/data/perguntas_frequentes.json"

# Carrega ou cria o arquivo
def carregar_perguntas():
    if os.path.exists(path_JSON):
        with open(path_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

# Salva o dicionário no arquivo
def salvar_perguntas(perguntas):
    with open(path_JSON, "w", encoding="utf-8") as f:
        json.dump(perguntas, f, indent=4, ensure_ascii=False)

# Incrementa ou adiciona a pergunta
def registrar_pergunta(pergunta_usuario):
    perguntas = carregar_perguntas()
    if pergunta_usuario in perguntas:
        perguntas[pergunta_usuario] += 1
    else:
        perguntas[pergunta_usuario] = 1
    salvar_perguntas(perguntas)

# Retorna as n perguntas mais frequentes
def top_perguntas(n=5):
    perguntas = carregar_perguntas()
    # Ordena pelo contador decrescente
    top = sorted(perguntas.items(), key=lambda item: item[1], reverse=True)[:n]
    return [p for p, _ in top]
