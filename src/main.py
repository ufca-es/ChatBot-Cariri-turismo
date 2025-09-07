import json

#Ler dados do arquivo perguntas_respostas.json
with open("perguntas_respostas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
chaves=dados

print("Olá! Sou o ChatBot Cariri, seu guia de turismo!", "\n" \
"Que tal conhecer mais o Cariri? Tente me fazer uma pergunta ou escolha alguma das sugestões!","\n" \
"(Encerre o chat com 'sair')")

# personalidade = str(input("Por padrão, a personalidade do chat é guia turístico:"))
print("Por padrão, a personalidade do chat é guia turístico:")
personalidade="guia1"
pergunta = str(input("Digite sua pergunta para iniciar ou sair para encerrar: "))
while True:    
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
    
    pergunta = str(input("Digite qualquer coisa para iniciar ou sair para encerrar: "))

if pergunta.lower() != "sair":
    print("Inválido! O bot não foi iniciado.")
else:
    print("Chat encerrado, até mais!")