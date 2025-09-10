class estatisticas:
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
        frequencias = {}
        for p in self.perguntas:
            if p in frequencias:
                frequencias[p] += 1
            else:
                frequencias[p] = 1

        return max(frequencias, key=frequencias.get)