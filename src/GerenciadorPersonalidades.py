import json

class GerenciadorPersonalidades:
    def __init__(self):
        self.personalidades = ["guia_turistico", "cabra_arretado", "guia_aperreado"]
        self.ativa = self.personalidades[0]
        self.arquivo_contagem = "./data/contagem_personalidades.json"
        self.contador_uso = self.carregar_contagem()

    def carregar_contagem(self):
        try:
            with open(self.arquivo_contagem, 'r', encoding='utf-8') as arquivo_temporario1:
                return json.load(arquivo_temporario1)
        except FileNotFoundError:
            print("Arquivo de contagem não encontrado. Criando um novo.")
            return {personalidade: 0 for personalidade in self.personalidades}
        
    def salvar_contagem(self):
        try:
            with open(self.arquivo_contagem, 'w', encoding='utf-8') as arquivo_temporario1:
                json.dump(self.contador_uso, arquivo_temporario1, indent=4)
        except IOError as erro:
            print(f"Erro ao salvar a contagem: {erro}")

    def incrementar_uso(self):
        personalidade_usada = self.ativa
        self.contador_uso[personalidade_usada] += 1
        self.salvar_contagem()
    
    def trocar_personalidade(self):
        print(f"Por padrão, a personalidade do chat é guia turístico. ")
        try:
            decisao_personalidade = int(input("Digite 1 para manter, 2 para 'Cabra Arretado' ou 3 para 'Guia Aperreado': "))
            if decisao_personalidade > 0 and decisao_personalidade <= len(self.personalidades):
                self.ativa = self.personalidades[decisao_personalidade - 1]
            else:
                print("Opção inválida. Mantendo a personalidade atual.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número disponível.")