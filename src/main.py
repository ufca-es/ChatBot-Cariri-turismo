perguntas_respostas=[
    {
    "pergunta":"",
    "resposta": "",
    },{
    "pergunta":"",
    "resposta": "",
    },{
    "pergunta":"",
    "resposta": "",
    }
]

print("Olá! Sou o ChatBot Cariri, seu guia de turismo!", "\n" \
"Que tal conhecer mais o Cariri? Tente me fazer uma pergunta ou escolha alguma das sugestões!","\n" \
"(Encerre o chat com 'sair')")
entrada = str(input("Digite olá para iniciar: "))
if entrada.lower() == "ola":
    while True:
        personalidade = int(input("Por padrão, a personalidade do chat é guia turístico"))
        pergunta=str(input("escreva sua pergunta:"))
        
        if (pergunta.lower()=="sair"):
            print("Chat encerrado, até mais!")
            break

        for i in range(len(perguntas_respostas)):
            #modulo: lógica para identificar pergunta/resposta
            if (perguntas_respostas[i-1]["pergunta"] == pergunta): 
                print(perguntas_respostas[i-1]["resposta"])
            else:
                print("Desculpe! Não consegui compreender sua pergunta.")
            #modulo: módulo caso a pergunta não esteja na base de dados
elif entrada.lower() != "sair":
    print("Inválido! O bot não foi iniciado.")
else:
    print("Chat encerrado, até mais!")