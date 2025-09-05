pergunstas_respostas=[
    {
    "pergunta":"ttt",
    "resposta": "vrggrgrvgr",
    },{
    "pergunta":"",
    "resposta": "",
    },{
    "pergunta":"",
    "resposta": "",
    }
]

print("Olá! sou um bot de guia de turismo !")
print("Escreva 'sair' para encerar o chat.")
entrada = str(input("Digite olá para iniciar: "))
if entrada.lower() == "ola":
    while True:
        pergunta=str(input("escreva sua pergunta:"))
        
        if (pergunta.lower()=="sair"):
            print("Chat encerrado, até mais !")
            break

        for i in range(len(pergunstas_respostas)):
            if (pergunstas_respostas[i-1]["pergunta"] == pergunta): 
                print(pergunstas_respostas[i-1]["resposta"])
else:
    print("Inválido! O bot não foi iniciado")