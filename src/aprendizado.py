def registrar_aprendizado(pergunta):
    #aprendizado
    print("Desculpe, não consegui compreender sua pergunta.")
    resposta_usuario = str(input(f"Se possível, insira a resposta dela para que eu possa auxiliar você melhor posteriormente (Digite 's' para sair sem responder):\n"))
    if resposta_usuario.lower() != "s":
        with open("relatorio_aprendizagem.txt", 'a', encoding="utf-8") as relatorio:
            relatorio.write(f"Nova pergunta: {pergunta}\n")
            relatorio.write(f"Nova resposta: {resposta_usuario}\n")
            relatorio.write(f"---------------------------------------\n")