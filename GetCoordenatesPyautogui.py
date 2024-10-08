import pyautogui
import tkinter as tk
from tkinter import messagebox
import pyperclip
import time

# Lista para armazenar as coordenadas dos cliques
click_coordinates = []
recording = False  # Flag para indicar se estamos gravando ou não
last_position = None  # Última posição do mouse
time_at_position = 0  # Tempo que o mouse permaneceu na mesma posição

# Função para alternar a gravação de cliques
def toggle_recording():
    global recording, time_at_position
    recording = not recording
    if recording:
        record_button.config(text="STOP")
        time_at_position = time.time()  # Inicia o contador de tempo
        start_recording()
    else:
        record_button.config(text="START")

# Função que acompanha o mouse e grava as coordenadas se ele ficar parado por mais de 3 segundos
def start_recording():
    global last_position, time_at_position
    if recording:
        current_position = pyautogui.position()  # Captura a posição atual do mouse

        # Atualiza o display da posição do mouse em tempo real
        update_mouse_position_display(current_position)

        # Se a posição mudou, reseta o tempo
        if current_position != last_position:
            last_position = current_position
            time_at_position = time.time()  # Atualiza o tempo de permanência na nova posição

        # Verifica se o mouse ficou parado por mais de 3 segundos
        if time.time() - time_at_position >= 3 and current_position not in click_coordinates:
            click_coordinates.append(current_position)  # Adiciona a coordenada
            update_coordinates_display()

        # Chama a função novamente após 100ms para continuar monitorando o mouse
        root.after(100, start_recording)

# Função para atualizar a exibição das coordenadas no modo reverso
def update_coordinates_display():
    coordinates_listbox.delete(0, tk.END)  # Limpa a lista de exibição
    for coord in reversed(click_coordinates):  # Exibe a lista de coordenadas em ordem reversa
        coordinates_listbox.insert(tk.END, f"Coordenada: {coord}")

# Função para copiar a coordenada selecionada para a área de transferência
def copy_selected_position(event):
    selection = coordinates_listbox.curselection()  # Obtém o índice do item selecionado
    if selection:
        selected_text = coordinates_listbox.get(selection)  # Obtém o texto da lista
        coord = selected_text.split(": ")[1]  # Extrai apenas as coordenadas
        pyperclip.copy(coord)  # Copia as coordenadas para a área de transferência
        messagebox.showinfo("Coordenada Copiada", f"Coordenada {coord} copiada para a área de transferência!")

# Função para copiar todas as coordenadas da lista para a área de transferência
def copy_all_positions():
    if click_coordinates:
        coords_string = "\n".join([str(coord) for coord in reversed(click_coordinates)])  # Junta todas as coordenadas
        pyperclip.copy(coords_string)  # Copia todas as coordenadas para a área de transferência
        messagebox.showinfo("Coordenadas Copiadas", "Todas as coordenadas foram copiadas para a área de transferência!")
    else:
        messagebox.showwarning("Sem Coordenadas", "Nenhuma coordenada para copiar.")

# Função para limpar as coordenadas gravadas
def clear_coordinates():
    click_coordinates.clear()
    coordinates_listbox.delete(0, tk.END)  # Limpa a exibição no campo de texto
    messagebox.showinfo("Coordenadas Limpas", "Todas as coordenadas foram removidas.")

# Função para atualizar a posição do mouse em tempo real
def update_mouse_position_display(current_position):
    mouse_position_label.config(text=f"Posição atual do mouse: {current_position}")

# Criando a janela principal com Tkinter
root = tk.Tk()
root.title("Gravador de Cliques com PyAutoGUI")

# Criando os botões
record_button = tk.Button(root, text="START", command=toggle_recording, width=30, height=2)
record_button.pack(pady=10)

clear_button = tk.Button(root, text="Limpar Coordenadas Gravadas", command=clear_coordinates, width=30, height=2)
clear_button.pack(pady=10)

copy_all_button = tk.Button(root, text="Copiar Todas as Coordenadas", command=copy_all_positions, width=30, height=2)
copy_all_button.pack(pady=10)

# Label para exibir a posição atual do mouse em tempo real
mouse_position_label = tk.Label(root, text="Posição atual do mouse: ", font=("Arial", 12))
mouse_position_label.pack(pady=10)

# Título para a lista de coordenadas
coordinates_title_label = tk.Label(root, text="Lista das Coordenadas", font=("Arial", 12, "bold"))
coordinates_title_label.pack(pady=10)

# Lista para exibir as coordenadas
coordinates_listbox = tk.Listbox(root, height=10, width=40)
coordinates_listbox.pack(pady=10)

# Vincula o evento de clique na lista à função que copia a coordenada
coordinates_listbox.bind('<Double-1>', copy_selected_position)

# Iniciando o loop da interface
root.mainloop()
