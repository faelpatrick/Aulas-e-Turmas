import tkinter as tk
from PIL import Image, ImageTk
import threading

# Caminho do ficheiro GIF (deve estar na mesma pasta do ficheiro .ipynb)
gif_path = "img.gif"  # Substitui pelo nome do teu ficheiro

# Função que exibe o GIF animado numa janela gráfica
def exibir_gif():
    root = tk.Tk()                          # Criar a janela
    root.title("GIF Animado")              # Título da janela

    gif = Image.open(gif_path)             # Abrir o ficheiro GIF
    frames = []                            # Lista para guardar os frames

    # Ler todos os frames do GIF
    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))  # Avançar para o próximo frame
    except EOFError:
        pass  # Fim dos frames

    label = tk.Label(root)                 # Criar rótulo (label) para mostrar o GIF
    label.pack()

    # Função para atualizar os frames em loop
    def atualizar(i):
        frame = frames[i]
        label.configure(image=frame)
        root.after(100, atualizar, (i+1) % len(frames))  # Próximo frame após 100ms

    atualizar(0)                           # Iniciar a animação
    root.mainloop()                        # Iniciar a janela gráfica

# Executar a janela em thread separada para não bloquear o Jupyter
threading.Thread(target=exibir_gif).start()
