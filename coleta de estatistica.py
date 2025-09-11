import json
import random
from collections import Counter

class Estatisticas:
    def __init__(self):
        self.total_interacoes = 0
        self.perguntas = []
        self.uso_personalidades = Counter()

    def registra_interacao(self, pergunta, personalidade):
        self.total_interacoes += 1
        self.perguntas.append(pergunta)
        self.uso_personalidades[personalidade] += 1

    def pergunta_mais_frequente(self):
        if not self.perguntas:
            return None
        return Counter(self.perguntas).most_common(1)[0]

    def gerar_relatorio(self, caminho="relatorio.txt"):
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("==== Relatório do Chat ====\n\n")
            f.write(f"Total de interações: {self.total_interacoes}\n")
            mais_freq = self.pergunta_mais_frequente()
            if mais_freq:
                f.write(f"Pergunta mais feita: '{mais_freq[0]}' ({mais_freq[1]} vezes)\n")
            else:
                f.write("Nenhuma pergunta registrada.\n")
            f.write("\nUso das personalidades:\n")
            for p, qtd in self.uso_personalidades.items():
                f.write(f"- {p}: {qtd} vezes\n")

    def sugestoes_perguntas(self, n=3):
        contador = Counter(self.perguntas)
        return [p for p, _ in contador.most_common(n)]

# Funções auxiliares
def addPerguntaList(lista, pergunta, resposta):
    lista.append(pergunta)
    lista.append(resposta)

def salvarHistorico(lista):
    with open("historico.txt", "a", encoding="utf-8") as f:
        for i in lista:
            f.write(i + "\n")

def carregarHistorico():
    try:
        with open("historico.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        ultimas_10 = linhas[-10:] if len(linhas) >= 10 else linhas
        print("\nÚltimas interações:")
        for i, linha in enumerate(ultimas_10, 1):
            if i % 2 != 0:
                print(f"Pergunta: {linha.strip()}")
            else:
                print(f"Resposta: {linha.strip()}\n")
    except FileNotFoundError:
        print("Nenhum histórico encontrado.")

# =============================
# Chat principal (usando gerenciador existente)
# =============================
def main(gerenciador):
    # Carregar perguntas e respostas do JSON
    with open("./data/perguntas_respostas.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    estatisticas = Estatisticas()
    perguntas_respostas = []

    print("Olá! Sou o ChatBot Cariri, seu guia de turismo!")
    print("(Digite 'mudar' para trocar de personalidade, 'historico' para ver interações ou 'sair' para encerrar.)")

    carregarHistorico()
    pergunta = input("Digite sua pergunta: ")

    while True:
        if pergunta.lower() == "sair":
            break
        if pergunta.lower() == "mudar":
            gerenciador.trocar_personalidade()
        elif pergunta.lower() == "historico":
            carregarHistorico()
        else:
            encontrada = False
            e_despedida = False
            for i in dados:
                chaves = next((v for k, v in i.items() if k.startswith("palavras_chaves")), [])
                if any(chave in pergunta for chave in chaves):
                    lista_respostas = i["respostas"][gerenciador.ativa]
                    resposta_sorteada = random.choice(lista_respostas)
                    print("Bot:", resposta_sorteada)
                    encontrada = True
                    addPerguntaList(perguntas_respostas, pergunta, resposta_sorteada)
                    gerenciador.somar_contagem_uso()
                    estatisticas.registrar_interacao(pergunta, gerenciador.ativa)
                    if "tchau" in chaves:
                        e_despedida = True
                    break

            if not encontrada:
                print("Desculpe! Não entendi.")
                resposta_usuario = input("Digite a resposta correta ou 's' para pular: ")
                if resposta_usuario.lower() != "s":
                    with open("relatorio_aprendizagem.txt", "a", encoding="utf-8") as rel:
                        rel.write(f"Nova pergunta: {pergunta}\n")
                        rel.write(f"Nova resposta: {resposta_usuario}\n")
                        rel.write("-" * 40 + "\n")

        if 'e_despedida' in locals() and e_despedida:
            break

        pergunta = input("Digite sua próxima pergunta: ")

    # Salva histórico e gera relatório
    salvarHistorico(perguntas_respostas)
    estatisticas.gerar_relatorio()

    print("\nChat encerrado. Relatório salvo em relatorio.txt")
    print("\nSugestões de perguntas frequentes:")
    for s in estatisticas.sugestoes_perguntas():
        print(f"- {s}")

# =============================
# Executa o chatbot
# =============================
if __name__ == "__main__":
    from gerenciador import GerenciadorPersonalidades  # Importa sua classe já feita
    gerenciador = GerenciadorPersonalidades()
    main(gerenciador)

