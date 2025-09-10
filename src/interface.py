import tkinter as tk
import json
from GerenciadorPersonalidades import GerenciadorPersonalidades
from buscar_respostas import buscar_respostas

# Criar a janela principal
janela = tk.Tk()
janela.title("ochantBot")
janela.geometry("300x500")

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

frame_chat = tk.Frame(janela, bg="#E6E6E6", height=70)
frame_chat.grid(row=1, column=0, sticky="nsew")

texto_chat = tk.Text(frame_chat, wrap="word", state="disable") #widget de texto - state="disable" bloqueia digitação
texto_chat.pack(expand=True, fill="both") # Preenche vertical e horizontalmente

# ------ FOOTER --------

frame_botom = tk.Frame(janela, bg="#ddd", height=10)
frame_botom.grid(row=2, column=0, sticky="nsew")

entrada = tk.Entry(frame_botom, font=("Arial",10))
entrada.pack(side="left", expand=True, fill="x", padx=5, pady=5)
entrada.bind("<Return>", lambda event: enviar_pergunta()) # Disparar evento

def enviar_pergunta():
    pergunta = entrada.get()

    if pergunta.strip() != "": # verifica se a perguta não é vazia

        texto_chat.config(state="normal") # Habilita o Text para add de textos
        texto_chat.insert("end", f"Você: {pergunta} \n") # "end" -> posição final

        resposta, e_despedida = buscar_respostas(pergunta, gerenciador, chaves, personalidade_ativa)

        texto_chat.insert("end", f"Bot: {resposta} \n\n")
        texto_chat.config(state="disabled") # Desabilita a inserção de texto no Text
        texto_chat.see("end") # Faz texto rolar automaticamente até o final
        entrada.delete(0, "end") # Limpa a entrada da pergunta
        if e_despedida:
            janela.destroy()



botao = tk.Button(frame_botom, text="Enviar", command=enviar_pergunta, bg="#4CAF50", fg="white", font=("Arial",10), relief="raised", bd=0, activebackground="#45a049", activeforeground="white", cursor="hand2")
botao.pack(side="right", padx=5, pady=5)

# ---------- GRID ----------
janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Loop principal
janela.mainloop()