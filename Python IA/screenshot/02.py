from pynput import mouse
import time

start_time = None

def on_click(x, y, button, pressed):
    global start_time
    if pressed:
        start_time = time.time()
    elif start_time and time.time() - start_time >= 5:
        print("Clique por mais de 5 segundos")
        start_time = None

# Inicia o monitoramento de cliques
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
