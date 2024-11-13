from tkinter import *
import random
from time import sleep
from PIL import Image, ImageTk

pontuacao = 0

preto = "#000000"
laranja = "#d65104"

def iniciar_jogo():
    global pontuacao
    pontuacao = 0
    atualizar_pontuacao()  # estava escrito com acentuação foi corrigido
    aparecer_zombie()

def atualizar_pontuacao():
    pontos.config(text=f"PONTOS: {pontuacao}")

def aparecer_zombie():
    largura_tela = jogo.winfo_width()  # estava janela o certo era jogo
    altura_tela = jogo.winfo_height()  # estava janela o certo era jogo

    margem_topo = 200  
    margem_laterais = 20  
    margem_inferior = 70  

    x = random.randint( margem_laterais, largura_tela - margem_laterais - 80)  
    y = random.randint( margem_topo, altura_tela - margem_inferior - 80)  

    zombie.place(x=x, y=y, width=80, height=80)

def clicar_zombie(event): #a função precisa receber um event
    global pontuacao
    pontuacao += 1  
    atualizar_pontuacao()
    # aparecer_fantasma()  # Fantasma reaparece em outra posição
    aparecer_zombie()  # correção nome da função de fantasma para zombie
    print("Apos aparecer zombie")

y = random.randint(200, 930)
x = random.randint(20, 980)
topo = 200
lateral = 20
inferior = 70

# a imagem não abria pois era preciso iniciar o Tk() antes da imagem
jogo = Tk()
jogo.title("Kill the Zombie")
jogo.geometry("900x900+100+200")
jogo.configure(bg=preto)

# a imagem não abria pois era preciso iniciar o Tk() antes
zombie_OG = Image.open("abobora.png").convert("RGBA")
zombie2 = zombie_OG.resize((80, 80), Image.LANCZOS)
zombie_pronto = ImageTk.PhotoImage(zombie2)


iniciar = Button(jogo, text="Iniciar jogo", command=iniciar_jogo, bg=laranja)
iniciar.place(width=100, height=50, x=350, y=170)

zombie = Label(jogo, image=zombie_pronto, bg="black") #adicionado fundo preto
zombie.bind("<Button-1>", clicar_zombie)

# separar texto de introdução da variavel de pontos
texto_pontos = Label(
    jogo,
    text="Clique nos zombies para ganhar pontos",
    bg=preto,
    fg=laranja,
    font="Time 30 bold",
)
texto_pontos.place(width=700, height=60, x=240, y=100)
pontos = Label(jogo, text="PONTOS: 0", bg=preto, fg=laranja, font="Time 30 bold")
pontos.place(width=700, height=60, x=240, y=100)

jogo.mainloop()
