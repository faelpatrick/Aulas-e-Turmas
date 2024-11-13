from tkinter import *
import random
from time import sleep
from PIL import Image, ImageTk

pontuacao = 0

preto = '#000000'
laranja = '#d65104'

def iniciar_jogo():
    global pontuacao
    pontuacao = 0
    atualizar_pontuação()
    aparecer_zombie()

def atualizar_pontuacao():
    lbl_pontuacao.config(text=f"PONTOS: {pontuacao}")



def aparecer_zombie():
    largura_tela = janela.winfo_width()
    altura_tela = janela.winfo_height()

    # Definir margens
    margem_topo = 200  # Margem segura para evitar o texto e o botão
    margem_laterais = 20  # Pequena margem nas laterais da tela
    margem_inferior = 70  # Margem para a parte inferior da tela, se necessário

    # Calcular posições aleatórias considerando as margens e dimensões da imagem
    x = random.randint(margem_laterais, largura_tela - margem_laterais - 80)  # Largura da imagem é 80px
    y = random.randint(margem_topo, altura_tela - margem_inferior - 80)  # Altura da imagem é 80px

    # Colocar o fantasma na posição calculada
    zombie.place(x=x, y=y, width=80, height=80)


def clicar_zombie():
    global pontuacao
    pontuacao += 1  # Incrementa a pontuação a cada clique
    atualizar_pontuacao()
    aparecer_fantasma()  # Fantasma reaparece em outra posição


y = random.randint(200, 930)
x = random.randint(20, 980)
topo = 200
lateral = 20
inferior = 70

zombie_OG = Image.open('zombie.jpg').convert('RGBA')
zombie2 = zombie_OG.resize((80,80), Image.LANCZOS)
zombie_pronto = ImageTk.PhotoImage(zombie2)


jogo = Tk()

jogo.title('Kill the Zombie')
jogo.geometry('900x900+100+200')
jogo.configure(bg=preto)

iniciar = Button(jogo, text='Iniciar jogo', command=iniciar_jogo,bg=laranja)
iniciar.place(width=100, height=50, x=350, y=170)

zombie = Label(jogo, image=zombie_pronto)
zombie.bind('<Button-1>', clicar_zombie)

pontos = Label(jogo, text='Clique nos zombies para ganhar pontos', bg=preto, fg=laranja, font='Time 30 bold')
pontos.place(width=700, height=60, x=240, y=100)


jogo.mainloop()
