import tkinter as tk
import random
from PIL import Image, ImageTk  # Importar PIL para manusear a imagem PNG

pontuacao = 0      # Variável de pontuação global

def iniciar_jogo():
    global pontuacao
    pontuacao = 0  # Resetar pontuação
    atualizar_pontuacao()
    aparecer_fantasma()  # Inicia a aparição do fantasma

def aparecer_fantasma(): # Obter as dimensões da janela
    largura_tela = janela.winfo_width()
    altura_tela = janela.winfo_height()

    # Definir margens
    margem_topo = 200  # Margem segura para evitar o texto e o botão
    margem_laterais = 20  # Pequena margem nas laterais da tela
    margem_inferior = 80  # Margem para a parte inferior da tela, se necessário

    # Calcular posições aleatórias considerando as margens e dimensões da imagem
    x = random.randint(margem_laterais, largura_tela - margem_laterais - 80)  # Largura da imagem é 80px
    y = random.randint(margem_topo, altura_tela - margem_inferior - 80)  # Altura da imagem é 80px

    # Colocar o fantasma na posição calculada
    lbl_fantasma.place(x=x, y=y)

def clicar_fantasma(event):
    global pontuacao
    pontuacao += 1  # Incrementa a pontuação a cada clique
    atualizar_pontuacao()
    aparecer_fantasma()  # Fantasma reaparece em outra posição

def atualizar_pontuacao():
    lbl_pontuacao.config(text=f"PONTOS: {pontuacao}")

# Configuração da interface gráfica com tkinter
janela = tk.Tk()
janela.title("Jogo do Clique Fantasmagórico")
janela.geometry("800x800")
janela.configure(bg="black")  # Define a cor de fundo como preto

# Definir a fonte instalada
fonte_halloween = ("Scary Halloween Font", 18)  # Use o nome exato da fonte após instalá-la no sistema

# Configuração dos textos com a fonte de Halloween
lbl_instrucoes = tk.Label(janela, text="CLIQUE NO FANTASMA PARA GANHAR PONTOS!", fg="orange", bg="black", font=fonte_halloween)
lbl_instrucoes.pack()

lbl_pontuacao = tk.Label(janela, text="PONTOS: 0", fg="orange", bg="black", font=fonte_halloween)
lbl_pontuacao.pack()

# Botão de início com a fonte de Halloween
btn_iniciar = tk.Button(janela, text="⏯️ INICIAR JOGO", command=iniciar_jogo, fg="orange", bg="gray", font=fonte_halloween, width=15, height=2)
btn_iniciar.pack(pady=10)

# Carregar a imagem do fantasma
imagem_fantasma_original = Image.open("abobora.png").convert("RGBA")
imagem_fantasma_resized = imagem_fantasma_original.resize((80, 80), Image.LANCZOS)  # Redimensiona, se necessário
imagem_fantasma = ImageTk.PhotoImage(imagem_fantasma_resized)

# Label "fantasma" com a imagem redimensionada e transparência
lbl_fantasma = tk.Label(janela, image=imagem_fantasma, bg="black")
lbl_fantasma.bind("<Button-1>", clicar_fantasma)  # Vincula o clique na Label ao evento

# Iniciar o loop da interface gráfica
janela.mainloop()
