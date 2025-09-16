# chatbot_core.py
from GerenciadorPersonalidades import GerenciadorPersonalidades
from BaseConhecimento import BaseConhecimento
from historico import Historico
from aprendizado import registrar_aprendizado
from estatística import Estatisticas
from perguntas_frequentes import  registrar_pergunta


class ChatBotCore:
    def __init__(self):
        self.base = BaseConhecimento("src/data/perguntas_respostas.json")
        self.historico = Historico("historico.txt")
        self.estatisticas = Estatisticas()
        self.gerenciador = GerenciadorPersonalidades()
        self.personalidade_ativa = self.gerenciador.ativa
        self.aguardando_personalidade = False
        self.bot_iniciado = False

    def iniciar(self, mensagem):
        """Inicia o bot se o usuário disser 'olá'."""
        if mensagem.lower() == "olá" and not self.bot_iniciado:
            self.bot_iniciado = True

            # Carregar histórico
            linhas = self.historico.carregarHistorico()
            if linhas != None:
                historico_texto = ""
                for i, linha in enumerate(linhas, 1):
                    if i % 2 != 0:
                        historico_texto += f"Você: {linha.strip()}\n"
                    else:
                        historico_texto += f"Bot: {linha.strip()}\n\n"
            else:
                historico_texto = "Nenhum histórico encontrado.\n\n"

            mensagem_final = (
            "Olá! Sou o ChatBot Cariri, seu guia de turismo!\n"
            "Tente me fazer uma pergunta ou escolha uma sugestão!\n"
            "(Digite 'mudar' para trocar de personalidade | 'tchau' para sair | 'top' para exibir as perguntas frequentes))\n\n"
            f"Últimas 5 interações:\n{historico_texto}"
            )
            return mensagem_final, "bot-alert"
        
        elif not self.bot_iniciado:
            return "Por favor, diga 'olá' para iniciar o chat.", "bot-alert"
        return None, None

    def responder(self, pergunta):
        """Recebe uma pergunta e retorna a resposta e o tipo de mensagem."""
        if not pergunta:
            return None, None

        # Histórico
        if pergunta.lower() in ["carregar histórico", "histórico", "mostrar histórico", "historico"]:
            historicoa = self.historico.carregarHistorico()
            resposta = "EXIBINDO HISTÓRICO (5 últimas interações):\n\n"
            for i in range(0, len(historicoa), 2):
                perg = historicoa[i].strip()
                resp = historicoa[i+1].strip() if i+1 < len(historicoa) else ""
                resposta += f"Você: {perg}\nBot: {resp}\n\n"
            return resposta, "bot"


        # Trocar personalidade (entrada inicial)
        if pergunta.lower() == "mudar":
            self.aguardando_personalidade = True
            return ("Digite 1 para 'Guia Turístico', 2 para 'Cabra Arretado' ou 3 para 'Guia Aperreado':"), "bot"

        # Escolha da personalidade
        if self.aguardando_personalidade and pergunta in ["1", "2", "3"]:
            self.aguardando_personalidade = False
            self.gerenciador.trocar_personalidade(int(pergunta))
            self.personalidade_ativa = self.gerenciador.ativa
            return f"Beleza! Agora estou no modo {self.personalidade_ativa}.", "bot"
        

        # Procurar resposta na base
        chaves, resposta = self.base.buscar_palavras_e_blocos(pergunta, self.personalidade_ativa)

        # Encerrar
        if any(p in (chaves or []) for p in ["tchau", "obrigado", "encerrar", "sair"]):
            self.bot_iniciado = False
            self.estatisticas.gerar_relatorio_txt()
            return resposta or "Até mais! Encerrando o chat...", "bot"

        # Não entendeu → aprendizado
        if resposta is None:
            return ("Desculpe, não consegui compreender sua pergunta.\n"
                    "Se possível, insira a resposta dela (Digite 's' para pular)."), "bot-alert"

        # Resposta encontrada
        registrar_pergunta(pergunta)
        self.historico.registrar_interacao(pergunta, resposta)
        self.estatisticas.registrar_interacao(pergunta, self.personalidade_ativa)
        return resposta, "bot"

    def salvar_aprendizado(self, pergunta, resposta_usuario):
        """Salva uma nova resposta ensinada pelo usuário."""
        if resposta_usuario.lower() != "s" and resposta_usuario.strip() != "":
            registrar_aprendizado(pergunta, resposta_usuario)
            self.historico.registrar_interacao(pergunta, resposta_usuario)
            return f"Obrigado! Aprendi a responder: {pergunta}"
        return "Ok, não aprendi nada novo desta vez."
