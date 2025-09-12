import tkinter as tk
import json
from GerenciadorPersonalidades import GerenciadorPersonalidades
from BaseConhecimento import BaseConhecimento
from historico import Historico
from aprendizado import registrar_aprendizado
from estatística import Estatisticas

# Inicializar componentes principais
base_conhecimento = BaseConhecimento("data/perguntas_respostas.json")
historico = Historico("historico.txt")
estatisticas= Estatisticas()
bot_iniciado = False

# Criar a janela principal
janela = tk.Tk()
janela.title("ochantBot")
janela.geometry("450x600")

# Constantes
font=("Arial", 14)
with open("./data/perguntas_respostas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
chaves=dados

gerenciador = GerenciadorPersonalidades()
personalidade_ativa = gerenciador.ativa

# ------ HEADER --------

frame_topo = tk.Frame(janela, bg="#4CAF50", height=20) #cria um container
frame_topo.grid(row=0,column=0, sticky="nsew") #posiciona o frame e faz ele se expandir

label_logo = tk.Label(frame_topo, text="🤖", bg="#4CAF50", fg="white", font=font)
label_logo.pack(side="left", padx=10)

label_nome = tk.Label(frame_topo, text="ochantBot",bg="#4CAF50", fg="white", font=font)
label_nome.pack(side="left")

# ------ MAIN --------


# Frame principal do chat
frame_chat = tk.Frame(
    janela,
    bg="#F9F9F9",       # fundo mais claro
    bd=2,               # borda fina
    relief="groove",    # estilo da borda
    padx=8,
    pady=8
)
frame_chat.grid(row=1, column=0, sticky="nsew")



# Widget de texto (área do chat)
texto_chat = tk.Text(
    frame_chat,
    wrap="word",
    state="disabled",
    bg="#F5F5F5",        # fundo branco
    fg="#333333",        # texto cinza escuro
    font=("Segoe UI", 11),  # fonte moderna
    relief="flat",       # sem borda "bruta"
    padx=10,
    pady=10,

)
texto_chat.pack(expand=True, fill="both")
texto_chat.tag_config("user", foreground="blue", font=("Arial", 11))
texto_chat.tag_config("bot", foreground="green", font=("Arial", 11))
texto_chat.tag_config("bot-erro", foreground="red", font=("Arial", 11))
texto_chat.tag_config("bot-alert", foreground="gray", font=("Arial", 11))

# ------ FOOTER --------

frame_botom = tk.Frame(janela, bg="#ddd", height=10)
frame_botom.grid(row=2, column=0, sticky="nsew")

entrada = tk.Entry(frame_botom, font=("Arial",10))
entrada.pack(side="left", expand=True, fill="x", padx=5, pady=8)
entrada.bind("<Return>", lambda event: verificar_bot(bot_iniciado)) # Disparar evento

botao = tk.Button(frame_botom, text="Enviar", bg="#4CAF50", fg="white", font=("Arial",10), relief="raised", bd=0, activebackground="#45a049", activeforeground="white", cursor="hand2")
botao.pack(side="right", padx=5, pady=5)

def verificar_bot(bot_iniciado):
    pergunta = entrada.get().strip()
    if pergunta == "olá" and not bot_iniciado:
        entrada.bind("<Return>", lambda event: enviar_pergunta()) # Disparar evento
        # Inserir mensagem inicial
        texto_chat.config(state="normal")
        texto_chat.insert("end", "Olá! Sou o ChatBot Cariri, seu guia de turismo! \nQue tal conhecer mais o Cariri? Tente me fazer uma pergunta ou escolha alguma das sugestões! \n(Para trocar de personalidade, digite 'mudar' | Para sair, digite uma mensagem de despedida (ex:'tchau', 'sair', etc)\n\n", "gray")
        texto_chat.config(state="disabled")
        
        bot_iniciado = True
    else:
        texto_chat.config(state="normal")
        texto_chat.insert("end", "Bot: Por favor, diga 'olá' para iniciar o chat.\n\n", "bot-alert")
        texto_chat.config(state="disabled")
    entrada.delete(0, "end")
    texto_chat.see("end")

def enviar_pergunta():
    pergunta = entrada.get().strip()

    if not pergunta:
        return
    
    if pergunta.lower() in ["carregar histórico", "histórico", "mostrar histórico","historico"]:
        historicoa = historico.carregarHistorico()
        texto_chat.config(state="normal")
        texto_chat.insert("end", f"EXIBINDO HISTÓRICO(5 últimas interações):\n\n", "bot")

        for i in range(0, len(historicoa), 2):
            perg = historicoa[i].strip()                                    #recupera pergunta
            resp = historicoa[i+1].strip() if i+1 < len(historicoa) else "" #recupera resposta
            texto_chat.insert("end", f"{perg}\n", "user")
            texto_chat.insert("end", f"{resp}\n\n", "bot")

        entrada.delete(0, "end")
        texto_chat.config(state="disabled")
        texto_chat.see("end")
        return

    # Exibe pergunta no chat
    texto_chat.config(state="normal")
    texto_chat.insert("end", f"Você: {pergunta}\n", "user")

    if pergunta.lower() == "mudar":
        texto_chat.insert(
            "end",
            "Bot: Digite 1 para 'Guia Turístico', 2 para 'Cabra Arretado' ou 3 para 'Guia Aperreado':\n",
            "bot"
        )
        texto_chat.see("end")
        texto_chat.config(state="disabled")

        def escolher():
            try:
                escolha_personalidade = int(entrada.get().strip())
                gerenciador.trocar_personalidade(escolha_personalidade)
                personalidade_ativa = gerenciador.ativa
                texto_chat.config(state="normal")
                texto_chat.insert(
                    "end",
                    f"Bot: Personalidade alterada para {personalidade_ativa.replace('_', ' ').title()}.\n\n ",
                    "bot-alert"
                )
                texto_chat.config(state="disabled")
            except ValueError:
                texto_chat.config(state="normal")
                texto_chat.insert("end", "Bot: Opção inválida, digite apenas números (1, 2 ou 3).\n\n", "bot-erro")
                texto_chat.config(state="disabled")

            entrada.delete(0, "end")
            botao.config(command=enviar_pergunta)
            entrada.bind("<Return>", lambda event: enviar_pergunta())

        # Temporariamente muda ação do botão e tecla Enter
        botao.config(command=escolher)
        entrada.bind("<Return>", lambda event: escolher())
        entrada.delete(0, "end")
        return

    # Busca resposta
    chaves_do_bloco, resposta = base_conhecimento.buscar_palavras_e_blocos(pergunta, gerenciador.ativa)

    if any(palavra in chaves_do_bloco for palavra in ["tchau", "obrigado", "encerrar", "sair"]):
        texto_chat.config(state="normal")
        texto_chat.insert("end", f"Bot: {resposta}\n\n","bot")
        texto_chat.config(state="disabled")
        global bot_iniciado
        bot_iniciado = False
        entrada.bind("<Return>", lambda event: verificar_bot(bot_iniciado)) # Disparar evento
        botao.config(command=lambda: verificar_bot(bot_iniciado)) # Muda ação do botão
        entrada.delete(0, "end")
        texto_chat.see("end")
        return
    
    if resposta is None:
        # Caso não entenda a pergunta
        texto_chat.insert("end", "Bot: Desculpe, não consegui compreender sua pergunta.\n", "bot-alert")
        texto_chat.insert("end", "Bot: Se possível, insira a resposta dela para que eu possa auxiliar você melhor posteriormente (Digite 's' para sair sem responder):\n\n", "bot-alert")

        # Cria um campo temporário para aprendizado
        def salvar_aprendizado():
            resposta_usuario = entrada.get().strip()
            if resposta_usuario.lower() != "s" and resposta_usuario != "":
                registrar_aprendizado(pergunta, resposta_usuario)
                historico.registrar_interacao(pergunta, resposta_usuario)
                texto_chat.config(state="normal")
                texto_chat.insert("end", f"Você: {resposta_usuario}\n","user")
                texto_chat.insert("end", f"Bot: Obrigado! Aprendi a responder: {pergunta}\n\n", "bot")
                texto_chat.config(state="disabled")
            entrada.delete(0, "end")
            texto_chat.see("end")

            # Remove o binding extra para não afetar a próxima pergunta
            botao.config(command=enviar_pergunta)
            entrada.bind("<Return>", lambda event: enviar_pergunta())

        # Troca temporariamente a ação do botão e Enter para salvar aprendizado
        botao.config(command=salvar_aprendizado)
        entrada.bind("<Return>", lambda event: salvar_aprendizado())

    else:
        # Caso encontre resposta
        texto_chat.insert("end", f"Bot: {resposta}\n\n", "bot")
        historico.registrar_interacao(pergunta, resposta)
        estatisticas.registrar_interacao(pergunta)

    # Atualiza interface
    texto_chat.config(state="disabled")
    texto_chat.see("end")
    entrada.delete(0, "end")

botao.config(command=verificar_bot(bot_iniciado))

# ---------- GRID ----------
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)

texto_chat.config(state="normal")
texto_chat.insert("end", "Bot: Por favor, diga 'olá' para iniciar o chat.\n\n", "bot-alert")
texto_chat.config(state="disabled")

# Loop principal
janela.mainloop()