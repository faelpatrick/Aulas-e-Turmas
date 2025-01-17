from tkinter import *  # Importa todos os módulos do Tkinter
from tkinter import filedialog  # Para abrir a janela de seleção de arquivos
from tkinter import messagebox  # Para exibir mensagens pop-up
import os  # Manipulação de arquivos e diretórios
import pywhatkit  # Biblioteca para conversão de imagem em ASCII

# Definição de cores
branco = '#ffffff'
azul = '#364a85'

# -------------------------------------------------------------

# Configuração da janela principal
tela1 = Tk()
tela1.title('ASCII Art')  # Título da janela
tela1.geometry('700x900+400+100')  # Define tamanho e posição da janela
tela1.wm_resizable(width=False, height=False)  # Impede redimensionamento

# Função para converter a imagem selecionada em ASCII
def converter():
    global filename
    ler = pywhatkit.image_to_ascii_art(filename)  # Converte a imagem para ASCII

    # Exibe o resultado na tela
    lb_converter = Label(tela1, text=ler, font='Time 6', anchor=N)
    lb_converter.place(width=650, height=800, x=50, y=100)

# Função para abrir um arquivo de imagem
def open():
    global filename  # Variável global para armazenar o caminho do arquivo
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),  # Abre no diretório atual
        title='Select your Image ...',  # Título da janela de seleção
        filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'))  # Tipos de arquivos aceitos
    )
    converter()

# Função para salvar o resultado da conversão
def salvar():
    global filename
    pywhatkit.image_to_ascii_art(filename, 'Exemple')  # Salva como 'Exemple.txt'
    messagebox.showinfo("Information", "Saved 'Exemple.txt' in your folder")  # Exibe mensagem de sucesso

# -------------------------------------------------------------

# Label do título
lb_title = Label(tela1, text='ASCII ART', font='Time 20 bold', bg=azul, fg=branco, anchor='w', padx=260)
lb_title.place(width=700, height=50, x=0, y=0)

# Botão para abrir a imagem
b_open = Button(tela1, text='Converter', command=open, font='Time 10 bold', bg=branco, fg=azul)
b_open.place(width=85, height=30, x=100, y=70)

# Botão para salvar o resultado
b_salvar = Button(tela1, text='Gravar', command=salvar, font='Time 10 bold', bg=branco, fg=azul)
b_salvar.place(width=85, height=30, x=500, y=70)

tela1.mainloop()  # Mantém a janela aberta
