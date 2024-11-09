from tkinter import *
import pyautogui
from time import sleep

root = Tk()

root.title("Buscador Goooogle")

root.geometry("400x800")
root.resizable(width=False, height=False)

label = Label(root, text="MEU BUSCADOR", font=("Arial", 22))
label.pack(pady=10)

img = PhotoImage(file="Buscador_Goooogle.png")
Label(root, image=img).pack()

label = Label(root, text="Digite o que deseja buscar", font=("Arial", 20))
label.pack(pady=10)

entry = Entry(root, font=("Arial", 20))
entry.pack(pady=0, fill=X, padx=16, ipady=10, ipadx=16, expand=True)

button = Button(root, text="Buscar", font=("Arial", 20))
button.pack(pady=10, fill=X, padx=16, ipady=10, ipadx=16, expand=True)


def buscar():
    pyautogui.hotkey("win", "r")
    pyautogui.write("www.google.com")
    pyautogui.press("enter")
    sleep(2)
    pyautogui.write(entry.get())
    pyautogui.press("enter")


button.config(command=buscar)

root.mainloop()