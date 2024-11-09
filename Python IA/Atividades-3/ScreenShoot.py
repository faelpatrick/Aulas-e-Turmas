
import tkinter as tk
from pynput import mouse
import pyautogui
from datetime import datetime
import os
import time
from threading import Thread

# Variável de controle do monitoramento e tempo de clique
start_time = None
monitoring = False
listener = None

# Cria a pasta 'prints' caso não exista
if not os.path.exists("prints"):
    os.makedirs("prints")

# Função para tirar e salvar screenshot
def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filepath = f"prints/{timestamp}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"Screenshot salva em {filepath}")

# Função que monitora o clique do mouse
def on_click(x, y, button, pressed):
    global start_time
    if pressed:
        start_time = time.time()
    elif start_time and time.time() - start_time >= 3:
        take_screenshot()
        start_time = None

# Função para iniciar o monitoramento
def start_monitoring():
    global monitoring, listener
    if not monitoring:
        print("Start")
        monitoring = True
        listener = mouse.Listener(on_click=on_click)
        listener.start()

# Função para parar o monitoramento
def stop_monitoring():
    global monitoring, listener
    if monitoring:
        print("Stop")
        monitoring = False
        if listener:
            listener.stop()
            listener = None

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Controle de Monitoramento")

# Botões de Start e Stop
start_button = tk.Button(root, text="Start", command=start_monitoring)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_monitoring)
stop_button.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()
