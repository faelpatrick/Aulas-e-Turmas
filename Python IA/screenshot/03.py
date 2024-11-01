import pyautogui
from datetime import datetime
import os

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

# Teste simples de captura
take_screenshot()
