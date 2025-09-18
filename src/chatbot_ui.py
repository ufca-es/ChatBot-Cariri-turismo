# chatbot_ui.py
import tkinter as tk
from chatbot_core import ChatBotCore
from perguntas_frequentes import top_perguntas
from tkinter import messagebox

class ChatBotApp:
    def __init__(self):
        self.core = ChatBotCore()
        self.janela = tk.Tk()
        self.janela.title("ChatBot Cariri turismo")
        self.janela.attributes("-fullscreen", True)

        # Personalidade inicial
        self.personalidade = tk.StringVar(value="Guia turístico")

        self._criar_interface()
        
        # Se ainda não iniciado
        mensagem_historico, mensagem, tag = self.core.iniciar()
        self._inserir_texto(mensagem_historico, "black")
        self._inserir_texto(f"{mensagem}", tag)

    # ---------------- UI ----------------
    def _criar_interface(self):
        # Header
        frame_topo = tk.Frame(self.janela, bg="#4CAF50", height=20)
        frame_topo.grid(row=0, column=0, sticky="nsew")

        # Ícone e título
        tk.Label(frame_topo, text="🤖", bg="#4CAF50", fg="white", font=("Arial", 14)).pack(side="left", padx=10)
        tk.Label(frame_topo, text="ChatBot Cariri turismo", bg="#4CAF50", fg="white", font=("Arial", 14)).pack(side="left")

        # Botão de sair
        btn_exit = tk.Button(
            frame_topo, text="❌",
            bg="#f44336", fg="white", font=("Arial", 10, "bold"),
            relief="flat", cursor="hand2",
            command=self.fechar_janela,
        )
        btn_exit.pack(side="right", padx=5, pady=5)

        # Select (OptionMenu) para personalidades
        opcoes = ["Guia turístico", "cabra arretado", "Guia aperreado"]
        menu_personalidade = tk.OptionMenu(
            frame_topo, self.personalidade, *opcoes, command=self.trocar_personalidade
        )
        menu_personalidade.config(
            bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
            relief="flat", cursor="hand2", highlightthickness=0
        )
        menu_personalidade.pack(side="right", padx=5, pady=5)

        # 🔹 Botão FAQ
        btn_faq = tk.Button(
            frame_topo, text="Perguntas frequentes",
            bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
            relief="flat", cursor="hand2",
            command=self.mostrar_faq
        )
        btn_faq.pack(side="right", padx=5, pady=5)

        # Chat
        frame_chat = tk.Frame(self.janela, bg="#F9F9F9", bd=2, relief="groove", padx=8, pady=8)
        frame_chat.grid(row=1, column=0, sticky="nsew")
        self.texto_chat = tk.Text(frame_chat, wrap="word", state="disabled", bg="#F5F5F5",
                                  fg="#333", font=("Segoe UI", 11), relief="flat", padx=10, pady=10)
        self.texto_chat.pack(expand=True, fill="both")

        self.texto_chat.tag_config("user", foreground="#0077A7", font=("Arial", 11))
        self.texto_chat.tag_config("bot", foreground="#1F8300", font=("Arial", 11))
        self.texto_chat.tag_config("bot-erro", foreground="#E53935", font=("Arial", 11))
        self.texto_chat.tag_config("bot-alert", foreground="#5F5F5F", font=("Arial", 11))
        self.texto_chat.tag_config("black", foreground="#181818", font=("Arial", 11, "italic"))

        # Footer
        frame_bottom = tk.Frame(self.janela, bg="#ddd", height=10)
        frame_bottom.grid(row=2, column=0, sticky="nsew")

        self.entrada = tk.Entry(
            frame_bottom,
            font=("Arial", 12),
            bg="#f5f5f5",
            fg="#222",
            relief="flat",
            bd=2,
            highlightthickness=2,
            highlightbackground="#B8CEB8",
            insertbackground="#222"
        )
        self.entrada.configure(
            width=1  # width=1 deixa o Entry expandir conforme o pack(fill="x")
        )
        self.entrada.pack(side="left", expand=True, fill="x", padx=15, pady=12, ipady=8)
        self.entrada.bind("<Return>", lambda e: self.processar_entrada())

        self.botao = tk.Button(
            frame_bottom, text="  Enviar  ", 
            bg="#4CAF50", fg="white", font=("Arial", 10), 
            bd=0, 
            activebackground="#45a049", 
            activeforeground="white",
            cursor="hand2", 
            command=self.processar_entrada
        )
        self.botao.pack(side="right", fill="x", padx=10, pady=8, ipady=8)

        self.janela.grid_rowconfigure(1, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)

    # ---------------- Lógica ----------------
    def trocar_personalidade(self, escolha):
        self._inserir_texto(f"Bot: Personalidade alterada para {escolha.upper()}!", "bot-alert")
        self.core.gerenciador.trocar_personalidade({"Guia turístico":1, "cabra arretado":2, "Guia aperreado":3}[escolha])
        self.core.personalidade_ativa = self.core.gerenciador.ativa

    def mostrar_faq(self):
        mensagem = top_perguntas(5)
        self._inserir_texto(mensagem, "bot-alert")
        
    def _inserir_texto(self, mensagem, tag):
        self.texto_chat.config(state="normal")
        self.texto_chat.insert("end", mensagem + "\n", tag)
        self.texto_chat.config(state="disabled")
        self.texto_chat.see("end")

    def fechar_janela(self):
        self.core.estatisticas.gerar_relatorio_txt()
        messagebox.showinfo("Estatística gerada", "✅ O arquivo de estatística foi gerado com sucesso!")
        self.janela.destroy()

    # ---------------- Lógica ----------------
    def processar_entrada(self):
        pergunta = self.entrada.get().strip()
        if not pergunta:
            return

        self._inserir_texto(f"Você: {pergunta}", "user")

        # Caso o bot esteja aguardando aprendizado
        if getattr(self, "aguardando_resposta", False):
            resposta = self.core.salvar_aprendizado(self.ultima_pergunta, pergunta)
            self._inserir_texto(f"Bot: {resposta}", "bot")

            # Resetar estado
            self.aguardando_resposta = False
            self.ultima_pergunta = None
            self.entrada.delete(0, "end")
            return

        # Pergunta normal
        resposta, tag = self.core.responder(pergunta)
        if resposta:
            self._inserir_texto(f"Bot: {resposta}", tag)

            # Se for caso de aprendizado (bot não compreendeu)
            if "não consegui compreender" in resposta.lower():
                self.aguardando_resposta = True
                self.ultima_pergunta = pergunta

        self.entrada.delete(0, "end")

    # ---------------- Run ----------------
    def run(self):
        self.janela.mainloop()
