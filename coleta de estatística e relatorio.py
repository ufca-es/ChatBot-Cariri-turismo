import json
import random

class Estatisticas:
    def __init__(self):
        self.total_interacoes = 0
        self.perguntas = []
        self.uso_personalidades = {}

    def registrar_interacao(self, pergunta, personalidade):
        self.total_interacoes += 1
        self.perguntas.append(pergunta)
        if personalidade in self.uso_personalidades:
            self.uso_personalidades[personalidade] += 1
        else:
            self.uso_personalidades[personalidade] = 1

    def pergunta_mais_frequente(self):
        if not self.perguntas:
            return None
        freq = {}
        for p in self.perguntas:
            freq[p] = freq.get(p, 0) + 1
        max_freq = 0
        mais_frequente = None
        for p, count in freq.items():
            if count > max_freq:
                max_freq = count
                mais_frequente = p
        return (mais_frequente, max_freq)

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
        freq = {}
        for p in self.perguntas:
            freq[p] = freq.get(p, 0) + 1
        mais_frequentes = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [p for p, _ in mais_frequentes[:n]]
