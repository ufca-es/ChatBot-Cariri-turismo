import json
from GerenciadorPersonalidades import GerenciadorPersonalidades
from historico import addPerguntaList, salvarHistorico, carregarHistorico

#Ler dados do arquivo perguntas_respostas.json
with open("perguntas_respostas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
chaves=dados

gerenciador = GerenciadorPersonalidades()


print("Olá! Sou o ChatBot Cariri, seu guia de turismo!", "\n" \
"Que tal conhecer mais o Cariri? Tente me fazer uma pergunta ou escolha alguma das sugestões!","\n" \
"(Para trocar de personalidade, digite 'mudar' | Para sair, digite 'sair' | Para carregar histórico, digite 'historico')")

personalidade_ativa = gerenciador.ativa
print(f"Personalidade ativa: {personalidade_ativa.replace('_', ' ').title()}")


pergunta = str(input("Digite sua pergunta para iniciar ou sair para encerrar: "))
resposta=""
perguntas_respostas=[]

while pergunta.lower() != "sair":   

    if pergunta.lower() == "mudar":
        gerenciador.trocar_personalidade()
        personalidade_ativa = gerenciador.ativa
    else:
        encontrada = False

        #Percorre todos os items do array ate encontrar uma pergunta semelhante 
        for i in dados:

        # pegar palavras-chave de cada item do array 
            chaves = next((v for k, v in i.items() if k.startswith("palavras_chaves")), [])            
            
            #Comparar as palavras da pergunta com as palaras-chave
            if any(chave in pergunta for chave in chaves):
                resposta=i["respostas"][personalidade_ativa][0]
                print(resposta)
                encontrada = True
                
                addPerguntaList(perguntas_respostas, pergunta, resposta)
                gerenciador.incrementar_uso()
                break


        if not encontrada:
            print("Desculpe! Não consegui compreender sua pergunta.")
    
    pergunta = str(input("Digite qualquer coisa para iniciar ou sair para encerrar: "))
salvarHistorico(perguntas_respostas)
print("Chat encerrado, até mais!")