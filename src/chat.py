def chat(pergunta):
    if pergunta=="sair":
        return break
    if pergunta.lower() == "mudar":
        gerenciador.trocar_personalidade()
        personalidade_ativa = gerenciador.ativa
    else:
        encontrada = False
        e_despedida = False

        #Percorre todos os items do array ate encontrar uma pergunta semelhante 
        for i in dados:

        # pegar palavras-chave de cada item do array 
            chaves = next((v for k, v in i.items() if k.startswith("palavras_chaves")), [])            
            
            #Comparar as palavras da pergunta com as palaras-chave
            if any(chave in pergunta for chave in chaves):
                lista_de_respostas = i["respostas"][personalidade_ativa]
                resposta_sorteada = random.choice(lista_de_respostas)
                print(resposta_sorteada)

                encontrada = True
                
                addPerguntaList(perguntas_respostas, pergunta, resposta_sorteada)
                gerenciador.somar_contagem_uso()

                if "tchau" in chaves:
                    e_despedida = True
                break


        if not encontrada:
            print(f"Desculpe! Não consegui compreender sua pergunta.")
            resposta_usuario = str(input(f"Se possível, insira a resposta dela para que eu possa auxiliar você melhor posteriormente (Digite 's' para sair sem responder):\n"))

            if resposta_usuario.lower() != "s":
                with open("relatorio_aprendizagem.txt", 'a', encoding="utf-8") as relatorio:
                    relatorio.write(f"Nova pergunta: {pergunta}\n")
                    relatorio.write(f"Nova resposta: {resposta_usuario}\n")
                    relatorio.write(f"---------------------------------------\n")
    if e_despedida:
        break