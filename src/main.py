from BaseConhecimento import BaseConhecimento
from GerenciadorPersonalidades import GerenciadorPersonalidades
from historico import Historico
from estatística import Estatisticas

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
        gerenciador.trocar_personalidade()
        personalidade_ativa = gerenciador.ativa
        pergunta = str(input(f"\n({personalidade_ativa.replace('_', ' ').title()}) Personalidade alterada. Qual sua pergunta? "))
    else: 
        bloco_encontrado, resposta = base_conhecimento.buscar_palavras_e_blocos(pergunta, personalidade_ativa)

        if resposta:
            print(resposta)
            gerenciador.somar_contagem_uso()
            historico.registrar_interacao(pergunta,resposta)
            estatistica.registrar_interacao(pergunta)
            chaves_do_bloco = bloco_encontrado.get("palavras_chaves", [])
            if "tchau" in chaves_do_bloco:
                break
        else:
              print("Desculpe, não consegui compreender sua pergunta.")
              #aprendizado
              resposta_usuario = str(input(f"Se possível, insira a resposta dela para que eu possa auxiliar você melhor posteriormente (Digite 's' para sair sem responder):\n"))
              if resposta_usuario.lower() != "s":
                with open("src/relatorio_aprendizagem.txt", 'a', encoding="utf-8") as relatorio:
                    relatorio.write(f"Nova pergunta: {pergunta}\n")
                    relatorio.write(f"Nova resposta: {resposta_usuario}\n")
                    relatorio.write(f"---------------------------------------\n")
        pergunta = str(input("Digite qualquer coisa para iniciar ou sair para encerrar: "))
print("Chat encerrado, até mais!")
#estatistica.gerar_relatorio_final