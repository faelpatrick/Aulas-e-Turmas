import tkinter as tk
from tkinter import messagebox, PhotoImage
import random
import os
import json

# Cores principais
COR_FUNDO = "#F0F0F0"
COR_TEXTO = "#222222"
COR_BOTAO = "#4CAF50"
COR_BOTAO_TEXTO = "#FFFFFF"

# Variáveis do jogo
perguntas = []
respondidas_certas = set()
nome_jogador = ""
acertos = 0
erros = 0
imagens = {}

# Carrega perguntas do arquivo JSON
def carregar_perguntas():
    global perguntas
    with open("perguntas.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        perguntas = dados["perguntas"]
    random.shuffle(perguntas)

# Salva o placar do jogador atual no placar.json
def salvar_placar():
    try:
        with open("placar.json", "r", encoding="utf-8") as f:
            historico = json.load(f)
    except FileNotFoundError:
        historico = {}

    historico[nome_jogador] = {"acertos": acertos, "erros": erros}

    with open("placar.json", "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)

    atualizar_placares_na_tela()

# Atualiza placar atual e histórico na tela principal
def atualizar_placares_na_tela():
    placar_atual.config(text=f"✅ Acertos: {acertos}   ❌ Erros: {erros}")

    try:
        with open("placar.json", "r", encoding="utf-8") as f:
            historico = json.load(f)
    except FileNotFoundError:
        historico = {}

    texto = "🏆 Placar Histórico:\n"
    for jogador, dados in historico.items():
        texto += f"{jogador}: {dados['acertos']} acertos, {dados['erros']} erros\n"

    placar_historico.config(text=texto.strip())

# Encerra o jogo corretamente
def fechar_e_sair(janela):
    salvar_placar()
    janela.destroy()
    root.destroy()

# Cria botão de resposta simples
def criar_botao_resposta(opcao, frame, correta, idx, janela):
    botao = tk.Button(
        frame,
        text=opcao,
        bg=COR_BOTAO,
        fg=COR_BOTAO_TEXTO,
        width=30,
        height=2,
        anchor="w"
    )

    def ao_clicar():
        global acertos, erros
        if opcao == correta:
            acertos += 1
            respondidas_certas.add(idx)
        else:
            erros += 1
        salvar_placar()
        janela.destroy()
        mostrar_pergunta()

    botao.config(command=ao_clicar)
    botao.pack(pady=5)

# Mostra uma nova pergunta
def mostrar_pergunta():
    global perguntas

    restantes = [i for i in range(len(perguntas)) if i not in respondidas_certas]
    if not restantes:
        messagebox.showinfo("Fim de Jogo", f"{nome_jogador}, parabéns!\nAcertos: {acertos} | Erros: {erros}")
        salvar_placar()
        root.destroy()
        return

    idx = random.choice(restantes)
    pergunta = perguntas[idx]

    janela = tk.Toplevel(bg=COR_FUNDO)
    janela.title("Pergunta")
    janela.minsize(400, 400)
    janela.protocol("WM_DELETE_WINDOW", lambda: fechar_e_sair(janela))

    tk.Label(janela, text=pergunta["pergunta"], font=("Arial", 14), bg=COR_FUNDO, fg=COR_TEXTO, wraplength=380).pack(pady=10)

    imagem_path = os.path.join("imagens", pergunta["img"])
    if not os.path.exists(imagem_path):
        imagem_path = os.path.join("imagens", "default.png")
    imagem = PhotoImage(file=imagem_path)
    imagens[imagem_path] = imagem
    tk.Label(janela, image=imagem, bg=COR_FUNDO).pack(pady=5)

    frame_opcoes = tk.Frame(janela, bg=COR_FUNDO)
    frame_opcoes.pack(pady=10)

    try:
        respostas = [
            pergunta["respostas"]["resposta1"],
            pergunta["respostas"]["resposta2"],
            pergunta["respostas"]["resposta3"],
            pergunta["respostas"]["resposta4"]
        ]
    except KeyError:
        messagebox.showerror("Erro", f"Erro no JSON da pergunta:\n{pergunta}")
        return

    random.shuffle(respostas)
    correta = pergunta["respostas"]["correta"]

    for opcao in respostas:
        criar_botao_resposta(opcao, frame_opcoes, correta, idx, janela)

    tk.Button(janela, text="Parar Jogo", command=lambda: fechar_e_sair(janela)).pack(pady=10)

# Inicia o jogo após digitar nome
def iniciar_jogo():
    global nome_jogador
    nome_jogador = entrada_nome.get().strip()
    if not nome_jogador:
        messagebox.showwarning("Atenção", "Digite seu nome para começar!")
        return
    entrada_nome.config(state="disabled")
    botao_iniciar.config(state="disabled")
    atualizar_placares_na_tela()
    mostrar_pergunta()

# Janela principal
root = tk.Tk()
root.title("Quiz Educativo")
root.configure(bg=COR_FUNDO)
root.minsize(400, 400)

tk.Label(root, text="Digite seu nome:", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 12)).pack(pady=10)
entrada_nome = tk.Entry(root, font=("Arial", 12))
entrada_nome.pack(pady=5)

botao_iniciar = tk.Button(root, text="Iniciar Jogo", bg=COR_BOTAO, fg=COR_BOTAO_TEXTO,
                          font=("Arial", 12), command=iniciar_jogo)
botao_iniciar.pack(pady=10)

# Exibição dos placares
placar_atual = tk.Label(root, text="", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 12))
placar_atual.pack(pady=5)

placar_historico = tk.Label(root, text="", bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 10), justify="left")
placar_historico.pack(pady=5)

carregar_perguntas()
root.mainloop()
