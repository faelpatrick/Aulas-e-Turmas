import pyautogui
from time import sleep

sleep(1)
pyautogui.moveTo(x=36, y=964,duration=1)
sleep(0.5)
pyautogui.click()
sleep(0.5)
pyautogui.click()
sleep(0.5)
pyautogui.write("novo nome",interval=0.25)
sleep(0.5)
pyautogui.press('enter')
sleep(0.5)
pyautogui.press('enter')
sleep(1)
pyautogui.write('Hello World',interval=0.25)
