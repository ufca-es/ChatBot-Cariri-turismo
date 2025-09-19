"""Módulo que gerencia as estatísticas da sessão de conversa."""

class Estatisticas:
    """Coleta e processa dados estatísticos de uma única sessão do chatbot."""

    def __init__(self):
        """Inicializa os contadores da sessão."""
        self.total_interacoes = 0
        self.perguntas = []
        self.personalidades_usadas = []  

    def registrar_interacao(self, pergunta, personalidade): 
        """Registra os dados de uma nova interação bem-sucedida."""
        self.total_interacoes += 1
        self.perguntas.append(pergunta)
        self.personalidades_usadas.append(personalidade) 

    def pergunta_mais_frequente(self):
        """Calcula qual foi a pergunta mais feita na sessão."""
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
    
    def contar_personalidades(self):
        """Conta quantas vezes cada personalidade foi usada nesta sessão."""
        contador = {} 
        for personalidade in self.personalidades_usadas:
            contador[personalidade] = contador.get(personalidade, 0) + 1
        return contador
    
    def gerar_relatorio_txt(self, nome_arquivo="relatorio.txt"):
        """Gera e salva um relatório de texto formatado com as estatísticas."""
        from datetime import datetime
        
        relatorio = []
        relatorio.append("=" * 60)
        relatorio.append("RELATÓRIO ESTATÍSTICO - CHATBOT DE TURISMO")
        relatorio.append("=" * 60)
        relatorio.append(f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        relatorio.append("")
        
        relatorio.append(" ESTATÍSTICAS GERAIS")
        relatorio.append("-" * 40)
        relatorio.append(f" Número total de interações: {self.total_interacoes}")
        
    
        mais_frequente = self.pergunta_mais_frequente()
        if mais_frequente:
            pergunta, frequencia = mais_frequente
            relatorio.append(f" Pergunta mais frequente: '{pergunta}'")
            relatorio.append(f" Quantidade de vezes: {frequencia}")
        else:
            relatorio.append("• Nenhuma pergunta registrada")
        relatorio.append("")
        
    
        relatorio.append("USO DE PERSONALIDADES")
        relatorio.append("-" * 40)
        contador_personalidades = self.contar_personalidades()
        total_personalidades = sum(contador_personalidades.values())
        
        for personalidade, quantidade in contador_personalidades.items():
            porcentagem = (quantidade / total_personalidades) * 100 if total_personalidades > 0 else 0
            nome_bonito = personalidade.replace('_', ' ').title()
            relatorio.append(f"• {nome_bonito}: {quantidade} vez(es) ({porcentagem:.1f}%)")
        
        relatorio.append("")
        relatorio.append("=" * 60)
        relatorio.append("Relatório gerado automaticamente")
        relatorio.append("=" * 60)

        with open(nome_arquivo, 'w', encoding='utf-8') as file:
            file.write('\n'.join(relatorio))
        
        return f"Relatório salvo como '{nome_arquivo}'"