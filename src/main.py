from BaseConhecimento import BaseConhecimento
from GerenciadorPersonalidades import GerenciadorPersonalidades
from historico import Historico
from estatística import Estatisticas
from aprendizado import registrar_aprendizado
from perguntas_frequentes import *

base_conhecimento = BaseConhecimento("src/data/perguntas_respostas.json")
gerenciador = GerenciadorPersonalidades()
historico = Historico("src/historico.txt")
estatistica = Estatisticas()

print("Olá! Sou o ChatBot Cariri, seu guia de turismo!", "\n" \
"Que tal conhecer mais o Cariri? Tente me fazer uma pergunta ou escolha alguma das sugestões!","\n" \
"(Para trocar de personalidade, digite 'mudar' | Para sair, digite uma mensagem de despedida (ex:'tchau', 'sair', etc)")

personalidade_ativa = gerenciador.ativa
print(f"Personalidade ativa: {personalidade_ativa.replace('_', ' ').title()}")

#exibe as 5 últimas interações
historico.carregarHistorico()

pergunta = str(input("Digite sua pergunta para iniciar ou se despeça para para encerrar: "))
while True:
    personalidade_ativa = gerenciador.ativa

    if pergunta.lower() == "mudar":
        print("Bot: Digite 1 para 'Guia Turístico', 2 para 'Cabra Arretado' ou 3 para 'Guia Aperreado':\n")
        nova_personalidade=int(input())
        gerenciador.trocar_personalidade(nova_personalidade)
        personalidade_ativa = gerenciador.ativa
        pergunta = str(input(f"\n({personalidade_ativa.replace('_', ' ').title()}) Personalidade alterada. Qual sua pergunta? "))
    else: 
        bloco_encontrado, resposta = base_conhecimento.buscar_palavras_e_blocos(pergunta, personalidade_ativa)

        if resposta:
            chaves_do_bloco = bloco_encontrado
            print(resposta)
            
            if any(chave in pergunta.lower() for chave in ["tchau", "obrigado", "encerrar", "sair"]):
                break 

            registrar_pergunta(pergunta)
            gerenciador.somar_contagem_uso()
            historico.registrar_interacao(pergunta,resposta)
            estatistica.registrar_interacao(pergunta)


        else:
              registrar_aprendizado(pergunta , None)              

        pergunta = str(input("Digite qualquer coisa para iniciar ou sair para encerrar: "))

estatistica.gerar_relatorio_txt()  


print(f" perguntas frequentes: {top_perguntas()}")
print("Chat encerrado, até mais!")
#estatistica.gerar_relatorio_final