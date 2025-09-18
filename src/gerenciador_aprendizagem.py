import os

ARQUIVO_APRENDIZADO = "relatorio_aprendizagem.txt"
ARQUIVO_PENDENTE = "aprendizado_pendente.txt"

def verificar_pendencias():
    """Cria ou remove o arquivo de notificação com base no conteúdo do arquivo de aprendizado."""
    try:
        # Verifica se o arquivo de aprendizado existe e não está vazio
        if os.path.exists(ARQUIVO_APRENDIZADO) and os.path.getsize(ARQUIVO_APRENDIZADO) > 0:
            # Se não houver um arquivo de pendência, cria um
            if not os.path.exists(ARQUIVO_PENDENTE):
                with open(ARQUIVO_PENDENTE, 'w') as f:
                    f.write("Existem novas perguntas para serem implementadas.")
                print("[AVISO] Arquivo de notificação 'aprendizado_pendente.txt' criado.")
        else:
            # Se o arquivo de aprendizado estiver vazio ou não existir, remove o de pendência
            if os.path.exists(ARQUIVO_PENDENTE):
                os.remove(ARQUIVO_PENDENTE)
                print("[INFO] Arquivo de notificação 'aprendizado_pendente.txt' removido.")
    except Exception as e:
        print(f"Ocorreu um erro ao verificar pendências: {e}")

def visualizar_aprendizado():
    """Exibe o conteúdo do arquivo de aprendizado com números de linha."""
    print("\n--- Conteúdo de 'aprendizado.txt' ---")
    verificar_pendencias() # Garante que o arquivo de notificação esteja atualizado
    try:
        with open(ARQUIVO_APRENDIZADO, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        if not linhas:
            print("Nenhuma pergunta nova para implementar.")
            return

        for i, linha in enumerate(linhas, 1):
            print(f"{i}: {linha.strip()}")
        print("------------------------------------")

    except FileNotFoundError:
        print("Nenhuma pergunta nova para implementar.")

def implementar_pergunta():
    """Remove uma pergunta e resposta do arquivo de aprendizado por número de linha."""
    visualizar_aprendizado()
    try:
        with open(ARQUIVO_APRENDIZADO, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        if not linhas:
            return

        linha_str = input("\nDigite o número da primeira linha da pergunta que você implementou no JSON (ex: '1' para a primeira 'Nova pergunta:'): ")
        
        if not linha_str.isdigit():
            print("Entrada inválida. Por favor, digite um número.")
            return

        linha_para_remover = int(linha_str)
        
        # Cada bloco (pergunta, resposta, ---) tem 3 linhas
        # O índice da lista começa em 0, então subtraímos 1
        indice_inicio = linha_para_remover - 1

        if 0 <= indice_inicio < len(linhas):
            # Remove as 3 linhas do bloco
            del linhas[indice_inicio : indice_inicio + 3]

            # Reescreve o arquivo com as linhas restantes
            with open(ARQUIVO_APRENDIZADO, 'w', encoding='utf-8') as f:
                f.writelines(linhas)
            
            print(f"\nBloco da linha {linha_para_remover} removido com sucesso.")
            verificar_pendencias() # Atualiza o arquivo de notificação
        else:
            print("Número de linha inválido.")

    except FileNotFoundError:
        print("Arquivo de aprendizado não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# --- Menu Principal da Ferramenta ---
if __name__ == "__main__":
    while True:
        # Garante que a notificação esteja sempre sincronizada ao exibir o menu
        verificar_pendencias() 
        print("\n--- Ferramenta de Gerenciamento de Aprendizado ---")
        print("1. Visualizar perguntas pendentes")
        print("2. Marcar pergunta como implementada (remover da lista)")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            visualizar_aprendizado()
        elif escolha == '2':
            implementar_pergunta()
        elif escolha == '3':
            break
        else:
            print("Opção inválida.")