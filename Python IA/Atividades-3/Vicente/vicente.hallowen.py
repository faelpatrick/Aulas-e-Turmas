from tkinter import *
from PIL import Image, ImageTk
import random

pontuacao = 0

root = Tk()
root.geometry("900x700+900+800")
root.resizable(True, True)
root.title("Jogo de Hallowen")
root.configure(bg="black")
fonte = ("Arial", 18)


def iniciar_jogo():
    global pontuacao
    potuacao = 0
    atualizar_pontuacao()
    aparecer_fantasma()


def atualizar_pontuacao():
    lbl_pontuacao.config(text=f"PONTOS:{pontuacao}")


def aparecer_fantasma():
    largura_tela = root.winfo_width()
    altura_tela = root.winfo_height()

    # faltou o codigo restante a usar o random para aparecer o fantasma randomicamente
    # Definir margens
    margem_topo = 200  # Margem segura para evitar o texto e o botão
    margem_laterais = 20  # Pequena margem nas laterais da tela
    margem_inferior = 80  # Margem para a parte inferior da tela, se necessário

    # Calcular posições aleatórias considerando as margens e dimensões da imagem
    x = random.randint(
        margem_laterais, largura_tela - margem_laterais - 80
    )  # Largura da imagem é 80px
    
    y = random.randint(
        margem_topo, altura_tela - margem_inferior - 80
    )  # Altura da imagem é 80px

    lbl_fantasma.place(x=x, y=y)


def clicar_fantasma(events):  # faltou a função para clicar no fantasma
    global pontuacao
    pontuacao += 1  # Incrementa a pontuação a cada clique
    atualizar_pontuacao()
    aparecer_fantasma()  # Fantasma reaparece em outra posição


lbl_pontuacao = Label(root, text="PONTOS: O", font="Arial")
lbl_pontuacao.pack()

lbl_texto = Label(root, text="CLICK NO FANTASMA PARA GANHAR PONTOS!", font="Arial")
lbl_texto.pack()

btn_ij = Button(root, text="INICIAR JOGO", font="Arial")
btn_ij.pack()
btn_ij.config(command=iniciar_jogo)

# FALTOU Carregar a imagem do fantasma
img_fantasma_original = Image.open("abobora.png").convert("RGBA")
img_fantasma_resized = img_fantasma_original.resize(
    (80, 80), Image.LANCZOS
)  # Redimensiona, se necessário
img_fantasma = ImageTk.PhotoImage(img_fantasma_resized)
lbl_fantasma = Label(root, image=img_fantasma, bg="black")
lbl_fantasma.bind("<Button-1>", clicar_fantasma)
root.mainloop()

# Sugestão final colocar o fundo dos textos em preto 
