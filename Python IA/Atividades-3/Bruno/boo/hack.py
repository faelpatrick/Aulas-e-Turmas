import pyautogui

while True:
    bixo = pyautogui.locateCenterOnScreen('bixoprint.png', confidence=0.8)
    pyautogui.moveTo(bixo, duration=0.5)
    pyautogui.click()