import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

# Variáveis globais para as imagens
imagem_original = None
imagem_editada = None

# Função para abrir imagem
def abrir_imagem():
    caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if caminho:
        global imagem_original, imagem_editada
        imagem_original = Image.open(caminho)
        imagem_editada = imagem_original.copy()
        exibir_imagem(imagem_editada)

# Função para exibir imagem
def exibir_imagem(img):
    img.thumbnail((400, 400))  # Redimensiona para caber na tela
    img_tk = ImageTk.PhotoImage(img)
    canvas.img_tk = img_tk
    canvas.create_image(200, 200, anchor=tk.CENTER, image=img_tk)

# Restaurar imagem original
def restaurar_original():
    global imagem_editada
    if imagem_original:
        imagem_editada = imagem_original.copy()
        exibir_imagem(imagem_editada)

# Aplicar filtro em tons de cinza
def filtro_cinza():
    global imagem_editada
    imagem_editada = imagem_original.convert("L")
    exibir_imagem(imagem_editada)

# Aplicar filtro sépia
def filtro_sepia():
    global imagem_editada
    img = imagem_original.convert("RGB")
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            pixels[i, j] = (min(tr, 255), min(tg, 255), min(tb, 255))
    imagem_editada = img
    exibir_imagem(imagem_editada)

# Aplicar filtro negativo
def filtro_negativo():
    global imagem_editada
    img = imagem_original.convert("RGB")
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            pixels[i, j] = (255 - r, 255 - g, 255 - b)
    imagem_editada = img
    exibir_imagem(imagem_editada)

# Ajustar brilho
def ajustar_brilho(valor):
    global imagem_editada
    enhancer = ImageEnhance.Brightness(imagem_original)
    imagem_editada = enhancer.enhance(float(valor))
    exibir_imagem(imagem_editada)

# Salvar imagem editada
def salvar_imagem():
    if imagem_editada:
        caminho = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")])
        if caminho:
            imagem_editada.save(caminho)

# Criar interface gráfica
root = tk.Tk()
root.title("Editor de Imagem Simples")

# Canvas para exibir a imagem
canvas = tk.Canvas(root, width=400, height=400, bg="gray")
canvas.pack()

# Botões
frame = tk.Frame(root)
frame.pack()

btn_abrir = tk.Button(frame, text="Abrir Imagem", command=abrir_imagem)
btn_abrir.grid(row=0, column=0)

btn_cinza = tk.Button(frame, text="Tons de Cinza", command=filtro_cinza)
btn_cinza.grid(row=0, column=1)

btn_sepia = tk.Button(frame, text="Sépia", command=filtro_sepia)
btn_sepia.grid(row=0, column=2)

btn_negativo = tk.Button(frame, text="Negativo", command=filtro_negativo)
btn_negativo.grid(row=0, column=3)

btn_restaurar = tk.Button(root, text="Restaurar Original", command=restaurar_original)
btn_restaurar.pack()

# Slider para brilho
brilho_slider = tk.Scale(root, from_=0.5, to=2.0, resolution=0.1, label="Brilho", orient="horizontal", command=ajustar_brilho)
brilho_slider.set(1.0)
brilho_slider.pack()

btn_salvar = tk.Button(root, text="Salvar Imagem", command=salvar_imagem)
btn_salvar.pack()

root.mainloop()
