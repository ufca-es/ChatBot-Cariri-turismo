# chatbot_ui.py
import tkinter as tk
from chatbot_core import ChatBotCore
from perguntas_frequentes import top_perguntas

class ChatBotApp:
    def __init__(self):
        self.core = ChatBotCore()
        self.janela = tk.Tk()
        self.janela.title("ChatBot Cariri turismo")
        self.janela.state("zoomed")

        self._criar_interface()
        self._inserir_texto("Bot: Por favor, diga 'olá' para iniciar o chat.\n", "bot-alert")

    # ---------------- UI ----------------
    def _criar_interface(self):
        # Header
        frame_topo = tk.Frame(self.janela, bg="#4CAF50", height=20)
        frame_topo.grid(row=0, column=0, sticky="nsew")
        tk.Label(frame_topo, text="🤖", bg="#4CAF50", fg="white", font=("Arial", 14)).pack(side="left", padx=10)
        tk.Label(frame_topo, text="ChatBot Cariri turismo", bg="#4CAF50", fg="white", font=("Arial", 14)).pack(side="left")

        # Chat
        frame_chat = tk.Frame(self.janela, bg="#F9F9F9", bd=2, relief="groove", padx=8, pady=8)
        frame_chat.grid(row=1, column=0, sticky="nsew")
        self.texto_chat = tk.Text(frame_chat, wrap="word", state="disabled", bg="#F5F5F5",
                                  fg="#333", font=("Segoe UI", 11), relief="flat", padx=10, pady=10)
        self.texto_chat.pack(expand=True, fill="both")

        self.texto_chat.tag_config("user", foreground="blue", font=("Arial", 11))
        self.texto_chat.tag_config("bot", foreground="green", font=("Arial", 11))
        self.texto_chat.tag_config("bot-erro", foreground="red", font=("Arial", 11))
        self.texto_chat.tag_config("bot-alert", foreground="gray", font=("Arial", 11))

        # Footer
        frame_bottom = tk.Frame(self.janela, bg="#ddd", height=10)
        frame_bottom.grid(row=2, column=0, sticky="nsew")

        self.entrada = tk.Entry(frame_bottom, font=("Arial", 10))
        self.entrada.pack(side="left", expand=True, fill="x", padx=5, pady=8)
        self.entrada.bind("<Return>", lambda e: self.processar_entrada())

        self.botao = tk.Button(frame_bottom, text="Enviar", bg="#4CAF50", fg="white", font=("Arial", 10),
                               relief="raised", bd=0, activebackground="#45a049", activeforeground="white",
                               cursor="hand2", command=self.processar_entrada)
        self.botao.pack(side="right", padx=5, pady=5)

        self.janela.grid_rowconfigure(1, weight=1)
        self.janela.grid_columnconfigure(0, weight=1)

    def _inserir_texto(self, mensagem, tag="bot"):
        self.texto_chat.config(state="normal")
        self.texto_chat.insert("end", mensagem + "\n", tag)
        self.texto_chat.config(state="disabled")
        self.texto_chat.see("end")

    # ---------------- Lógica ----------------
    def processar_entrada(self):
        pergunta = self.entrada.get().strip()
        if not pergunta:
            return

            # 🔹 se o usuário pedir as perguntas mais frequentes
        if pergunta.lower() in ["top", "perguntas frequentes", "faq"]:
            top = top_perguntas(5)
            if top:
                resposta = "📊 Perguntas mais frequentes:\n" + "\n".join(f"- {p}" for p in top)
            else:
                resposta = "Ainda não há perguntas registradas."
            self._inserir_texto(f"Bot: {resposta}", "bot")
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

        # Se ainda não iniciado
        mensagem, tag = self.core.iniciar(pergunta)
        if mensagem:
            self._inserir_texto(f"Bot: {mensagem}", tag)
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
