class Historico:
    def __init__(self,caminho_arquivo="src/historico.txt"):
        self.caminho_arquivo = caminho_arquivo

    def registrar_interacao(self, pergunta, resposta):
        try:   
            with open(self.caminho_arquivo, "a", encoding='utf-8') as arquive:
                    arquive.write(f"Pergunta: {pergunta}\n")
                    arquive.write(f"Resposta: {resposta}\n")
            print("[SISTEMA]: Conteúdo adicionado ao histórico!")
        except IOError:
             print("ERRO: Não foi possível registrar a interação no histórico.")
           

    def carregarHistorico(self):
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
                linhas=arquivo.readlines()
            ultimas_10 = linhas[-10:] if len(linhas) >= 10 else linhas
            print("\nÚltimas 5 interações: ")
            for numero, linha in enumerate(ultimas_10, 1):
                if numero%2!=0:
                    print(f"pergunta: {linha.strip()}")
                else:
                    print(f"Resposta: {linha.strip()}\n")
            return linhas[-10:] if len(linhas) >= 10 else linhas
        except FileNotFoundError:
            print("erro ao carregar histórico.")