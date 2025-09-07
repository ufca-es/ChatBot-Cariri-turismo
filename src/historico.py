def addPerguntaList(lista, pergunta, resposta):
    lista.append(pergunta)
    lista.append(resposta)

def salvarHistorico(lista):
    with open("historico.txt", "a", encoding='utf-8') as arquive:
        for i in lista:
            arquive.write(i+"\n")
    print("Conteúdo adicionado!")   

def carregarHistorico():
    try:

        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            linhas=arquivo.readlines()
        ultimas_10 = linhas[-10:] if len(linhas) >= 10 else linhas
        print("\nÚltimas 5 interações: ")
        for numero, linha in enumerate(ultimas_10, 1):
            if numero%2!=0:
                print(f"pergunta: {linha.strip()}")
            else:
                print(f"Resposta: {linha.strip()}\n")   
    except FileNotFoundError:
        print("erro ao carregar histórico.")

