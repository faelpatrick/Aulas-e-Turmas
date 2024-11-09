from tkinter import *
from PIL import Image, ImageTk
import random2

pontuacao = 0

root = Tk()
root.geometry('900x700+900+800')
root.resizable(True,True)
root.title('Jogo de Hallowen')
root.configure(bg='black')
fonte = ('Arial', 18)
def iniciar_jogo():
    global pontuacao
    potuacao = 0
    atualizar_pontuacao()
    aparecer_fantasma()

def atualizar_pontuacao():
    lbl_pontuacao.config(text=f'PONTOS:{pontuacao}')

def aparecer_fantasma():
    largura_tela = root.winfo_width()
    altura_tela = root.winfo_height()






lbl_pontuacao = Label(root, text='PONTOS: O', font='Arial')
lbl_pontuacao.pack()

lbl_texto = Label(root, text='CLICK NO FANTASMA PARA GANHAR PONTOS!', font='Arial')
lbl_texto.pack()

btn_ij = Button(root, text='INICIAR JOGO', font='Arial')
btn_ij.pack()

btn_ij.config(command='iniciar_jogo')

root.mainloop()