import tkinter as tk

def start_action():
    print("Start")

def stop_action():
    print("Stop")

root = tk.Tk()
root.title("Controle de Monitoramento")

start_button = tk.Button(root, text="Start", command=start_action)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_action)
stop_button.pack(pady=10)

root.mainloop()
