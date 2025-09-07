def addPerguntaList(lista, pergunta, resposta):
    lista.append(pergunta)
    lista.append(resposta)

def salvarHistorico(lista):
    with open("historico.txt", "a", encoding='utf-8') as arquive:
        for i in lista:
            arquive.write(i+"\n")
    print("Conteúdo adicionado!")   



