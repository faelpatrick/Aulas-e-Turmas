import tkinter as tk
from tkinter import filedialog, simpledialog, ttk
import vlc
import yt_dlp
import threading
import platform

janela = tk.Tk()
janela.title("Player de Vídeo")
janela.geometry("800x500")

# Instância do VLC
instancia = vlc.Instance()
player = instancia.media_player_new()

# Estado
em_tela_cheia = False
atualizando_slider = False

# --- FRAME DE VÍDEO (expansível)
video_frame = tk.Frame(janela, bg="black")
video_frame.pack(fill=tk.BOTH, expand=True)

# --- SLIDER (barra de progresso)
def atualizar_slider():
    global atualizando_slider
    if player.is_playing():
        atualizando_slider = True
        tempo = player.get_time()
        duracao = player.get_length()
        if duracao > 0:
            progresso.set((tempo / duracao) * 100)
    janela.after(500, atualizar_slider)

def ao_arrastar_slider(event):
    if player.get_length() > 0:
        nova_pos = progresso.get() / 100
        player.set_position(nova_pos)

progresso = tk.DoubleVar()
slider = ttk.Scale(janela, variable=progresso, from_=0, to=100, orient="horizontal", command=ao_arrastar_slider)
slider.pack(fill=tk.X, padx=10, pady=2)

# --- CONTROLES
controles = tk.Frame(janela)
controles.pack(pady=2)

def embutir_video():
    janela.update()
    if platform.system() == "Windows":
        player.set_hwnd(video_frame.winfo_id())
    elif platform.system() == "Linux":
        player.set_xwindow(video_frame.winfo_id())

def abrir_video_pc():
    caminho = filedialog.askopenfilename()
    if caminho:
        tocar_video(caminho)

def abrir_video_link():
    url = simpledialog.askstring("URL", "Cola o link do vídeo:")
    if url:
        threading.Thread(target=tocar_video_youtube, args=(url,), daemon=True).start()

def tocar_video_youtube(url):
    opcoes = {
        'format': 'best[ext=mp4]/best',
        'quiet': True,
        'noplaylist': True
    }
    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            info = ydl.extract_info(url, download=False)
            stream_url = info["url"]
            tocar_video(stream_url)
    except Exception as e:
        print("Erro:", e)

def tocar_video(caminho):
    media = instancia.media_new(caminho)
    player.set_media(media)
    embutir_video()
    player.play()
    atualizar_slider()

def pausar_ou_tocar():
    if player.is_playing():
        player.pause()
    else:
        player.play()

def parar_video():
    player.stop()

def voltar():
    player.set_time(max(0, player.get_time() - 5000))

def avancar():
    player.set_time(player.get_time() + 5000)

def alternar_tela_cheia():
    global em_tela_cheia
    em_tela_cheia = not em_tela_cheia
    janela.attributes("-fullscreen", em_tela_cheia)

# --- BOTÕES
btn_abrir = tk.Button(controles, text="Abrir", command=abrir_video_pc)
btn_voltar = tk.Button(controles, text="⏮️", command=voltar)
btn_play = tk.Button(controles, text="▶️/⏸️", command=pausar_ou_tocar)
btn_avancar = tk.Button(controles, text="⏭️", command=avancar)
btn_parar = tk.Button(controles, text="⏹️", command=parar_video)
btn_url = tk.Button(controles, text="YouTube", command=abrir_video_link)
btn_full = tk.Button(controles, text="🖥️ Fullscreen", command=alternar_tela_cheia)

btn_abrir.grid(row=0, column=0, padx=5)
btn_voltar.grid(row=0, column=1, padx=5)
btn_play.grid(row=0, column=2, padx=5)
btn_avancar.grid(row=0, column=3, padx=5)
btn_parar.grid(row=0, column=4, padx=5)
btn_url.grid(row=0, column=5, padx=5)
btn_full.grid(row=0, column=6, padx=5)

# Iniciar
janela.mainloop()
