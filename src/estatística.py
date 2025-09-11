class Estatisticas:
    def __init__(self):
        self.total_interacoes = 0
        self.perguntas = []

    def registrar_interacao(self, pergunta):
        self.total_interacoes += 1
        self.perguntas.append(pergunta)

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




