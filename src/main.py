import json

#Ler dados do arquivo perguntas_respostas.json
with open("C:/Users/vitor/Documents/faculdade/fund-programacao/Chatbot-Cariri-turismo-/src/perguntas_respostas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
chaves=dados

print("Olá! Sou o ChatBot Cariri, seu guia de turismo!", "\n" \
"Que tal conhecer mais o Cariri? Tente me fazer uma pergunta ou escolha alguma das sugestões!","\n" \
"(Encerre o chat com 'sair')")

# personalidade = str(input("Por padrão, a personalidade do chat é guia turístico:"))
print("Por padrão, a personalidade do chat é guia turístico:")
personalidade="guia1"
entrada = str(input("Digite olá para iniciar: "))
if entrada.lower() == "ola":
    while True:
        pergunta= str(input("escreva sua pergunta:"))
        
        if (pergunta.lower()=="sair"):
            print("Chat encerrado, até mais!")
            break

        identify = 0
        encontrada = False

        #Percorre todos os items do array ate encontrar uma pergunta semelhante 
        for i in dados:
            identify += 1

            # pegar palavras-chave de cada item do array 
            chaves = next((v for k, v in i.items() if k.startswith("palavras_chaves")), [])
            
            #Comparar as palavras da pergunta com as palaras-chave
            if any(chave in pergunta for chave in chaves):
                print(i["respostas"][personalidade][0])
                encontrada = True
                continue

        if not encontrada:
            print("Desculpe! Não consegui compreender sua pergunta.")

elif entrada.lower() != "sair":
    print("Inválido! O bot não foi iniciado.")
else:
    print("Chat encerrado, até mais!")