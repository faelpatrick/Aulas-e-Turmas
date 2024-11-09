import pyautogui
import tkinter as tk
import pyperclip
import time

click_coordinates = []
last_position = None
time_at_position = 0

def monitor_mouse():
    global last_position, time_at_position
    current_position = pyautogui.position()
    mouse_position_label.config(text=f"Mouse: {current_position}")

    if current_position != last_position:
        last_position = current_position
        time_at_position = time.time()

    if time.time() - time_at_position >= 3 and current_position not in click_coordinates:
        click_coordinates.append(current_position)
        coordinates_listbox.insert(tk.END, f"{current_position}")
        pyperclip.copy(str(current_position))

    root.after(100, monitor_mouse)

root = tk.Tk()
root.title("Monitor de Posição do Mouse")

mouse_position_label = tk.Label(root, text="Posição do mouse: ", font=("Arial", 12))
mouse_position_label.pack(pady=10)

coordinates_listbox = tk.Listbox(root, height=10, width=40)
coordinates_listbox.pack(pady=10)

# Iniciar a monitorização do mouse assim que o programa for executado
monitor_mouse()

root.mainloop()
