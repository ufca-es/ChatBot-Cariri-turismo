# chatbot-turismo

## Descrição
O Chatbot Cariri é um assistente virtual desenvolvido em Python com o objetivo de divulgar e responder dúvidas sobre os principais pontos turísticos da região do Cariri, no Ceará.

Ele utiliza uma base de conhecimento em JSON, permite personalização de respostas através de diferentes personalidades (formal, regional e pontual) e registra o histórico de interações em arquivos de texto. Além disso, o chatbot aprende novas respostas fornecidas pelo usuário, tornando-se cada vez mais inteligente e completo.

A iniciativa do projeto se deu com uma entrega para a disciplina de Fundamentos da Programação da Universidade Federal do Cariri (UFCA) e busca explorar a questão "Como um chatbot pode auxiliar as pessoas a interagirem melhor com sua cidade, sociedade ou comunidade?"

Nosso projeto responde à questão ao criar um guia turístico que vai além da simples informação. Através de personalidades distintas, que refletem a cultura local, e um modo de aprendizado colaborativo, o chatbot oferece uma experiência mais rica, engajadora e humana, transformando a tecnologia em uma ponte autêntica entre o usuário e a riqueza da região do Cariri.

---

## ⚙️Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📂 Estrutura de arquivos e pastas
<pre>
chatbot-cariri/
│── src/
│   ├── data/
│   │   ├── perguntas_frequentes.json
│   │   ├── perguntas_respostas.json
│   ├── main.py  
│   ├── chatbot_core.py
│   ├── chatbot_ui.py
│   ├── aprendizado.py
│   ├── estatística.py
│   ├── BaseConhecimento.py
│   ├── GerenciadorPersonalidade.py
│   ├── historico.py
│   ├── perguntas_frequentes.py
│── .gitignore
└── README.md
</pre>
---

## 🚀 Como Executar

Siga os passos abaixo para executar o ChatBot Cariri Turismo em sua máquina local.

**1. Pré-requisitos**
* [Python 3.10](https://www.python.org/downloads/) ou superior.
* [Git](https://git-scm.com/downloads) instalado.

**2. Clone o Repositório -**
Abra seu terminal ou Git Bash e utilize o comando abaixo para criar uma cópia local do projeto.
```bash
git clone https://github.com/ufca-es/ChatBot-Cariri-turismo.git
```
**3. Navegue até a pasta -**
Entre na pasta do projeto que foi recém-criada.
```bash
cd ChatBot-Cariri-turismo
```
**4. Execute -**
O programa principal que inicia a interface gráfica é o main.py. Para executá-lo, utilize o seguinte comando a partir da pasta raiz do projeto:
```bash
python src/main.py
```

---
## 👨‍💻 Equipe e Funções

Este projeto foi desenvolvido de forma colaborativa pelos seguintes integrantes:

* **Francisco Vitor** - *Desenvolvimento da Interface GUI, da classe Histórico, do loop de conversação e da organização do Kanban e do repositório.*
* **Levi Farias** - *Desenvolvimento da classe Gereciamento de personalidades, refatoração do projeto em módulos e classes, documentação.*
* **Henrique Coimbra** - *Desenvolvimento do relatório,da base do banco de dados JSON e da apresentação.*
* **Malaquias Oliveira** - *Desenvolvimento da classe Esatísticas, atualização do banco de dados do banco de dados.*
---
## 📷Demonstrações


**1. Tela Inicial e Histórico -**
A tela principal do chatbot apresenta uma interface limpa, exibindo as últimas interações do histórico para dar contexto ao usuário.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/2a75c767-ad70-4302-accb-e139d3745987" />


---
**2. Sistema de Personalidades Dinâmicas -**
O principal diferencial do chatbot é a capacidade de responder à mesma pergunta de formas diferentes. O usuário pode trocar de personalidade a qualquer momento clicando nos botões das personaliades

<img width="1919" height="1079" alt="Sem título" src="https://github.com/user-attachments/assets/6b03b11f-5f8c-4e13-9c60-bfc96e59f7bc" />


---
**3. Modo de Aprendizagem -**
Quando o chatbot não reconhece uma pergunta, ele entra em modo de aprendizado, permitindo que o usuário ensine novas respostas e expanda a base de conhecimento.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/3530e9eb-aeca-4e1a-bf88-421f6dd81b55" />


---
**4. Relatório Final de Estatísticas**
Ao final de cada sessão, um relatório completo é gerado com as estatísticas de uso, como o total de interações, a pergunta mais frequente e o uso de cada personalidade.

<img width="360" height="156" alt="image" src="https://github.com/user-attachments/assets/411511e3-70d8-4be7-9794-bb0e2d5bf3e3" />
<img width="548" height="355" alt="image" src="https://github.com/user-attachments/assets/ae63d24f-63e5-46b2-b473-5a86de5303e4" />

