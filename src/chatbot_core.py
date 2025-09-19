"""Módulo principal que contém a classe ChatBotCore, o cérebro do chatbot."""

from GerenciadorPersonalidades import GerenciadorPersonalidades
from BaseConhecimento import BaseConhecimento
from historico import Historico
from aprendizado import registrar_aprendizado
from estatística import Estatisticas
from perguntas_frequentes import  registrar_pergunta


class ChatBotCore:
    """Orquestra todos os módulos e gerencia a lógica principal da conversa."""

    def __init__(self):
        """Inicializa todos os módulos especialistas do chatbot."""

        self.base = BaseConhecimento("src/data/perguntas_respostas.json")
        self.historico = Historico("historico.txt")
        self.estatisticas = Estatisticas()
        self.gerenciador = GerenciadorPersonalidades()
        self.personalidade_ativa = self.gerenciador.ativa
        self.aguardando_personalidade = False
        self.bot_iniciado = False

    def iniciar(self):
        """Prepara a mensagem inicial do bot, incluindo o histórico de conversas."""
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
        mensagem_historico = f"📜 Histórico de interações:\n{historico_texto}\n"
        mensagem_final = (
        "Olá! Sou o ChatBot Cariri, seu guia de turismo!\n"
        "Tente me fazer uma pergunta ou escolha uma sugestão!\n"
        )
        return mensagem_historico, mensagem_final, "bot"
        

    def responder(self, pergunta):
        """Processa a pergunta do usuário e retorna a resposta apropriada."""
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

        # Procurar resposta na base
        chaves, resposta = self.base.buscar_palavras_e_blocos(pergunta, self.personalidade_ativa)


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
