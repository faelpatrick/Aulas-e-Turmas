
from tkinter import *
from tkinter import messagebox

# Definição de cores
branco = '#ffffff'
azul = '#8f88ba'

# Nome do arquivo onde as tarefas serão salvas
FICHEIRO_TAREFAS = "tarefas.txt"

# Criar janela principal
tela1 = Tk()
tela1.title('To Do List')  # Corrigido o fechamento da string
tela1.geometry('700x900+400+100')  # Define tamanho e posição da janela
tela1.wm_resizable(width=False, height=False)  # Impede redimensionamento
tela1.configure(bg=branco)  # Define fundo da janela

# Dicionário para armazenar tarefas e seus checkboxes
tarefas = {}

# Função para carregar tarefas do ficheiro
def carregar_tarefas():
    try:
        with open(FICHEIRO_TAREFAS, "r") as f:
            for linha in f.readlines():
                tarefa, status = linha.strip().split(" | ")
                var = IntVar(value=int(status))  # 1 = Feita, 0 = Pendente
                adicionar_checkbox(tarefa, var)
    except FileNotFoundError:
        pass

# Função para salvar as tarefas no ficheiro
def salvar_tarefas():
    with open(FICHEIRO_TAREFAS, "w") as f:
        for tarefa, var in tarefas.items():
            f.write(f"{tarefa} | {var.get()}\n")

# Função para adicionar checkbox de tarefa
def adicionar_checkbox(tarefa, var=None):
    if not var:
        var = IntVar(value=0)
    chk = Checkbutton(frame_tarefas, text=tarefa, variable=var, font="Arial 14", bg=branco, command=salvar_tarefas)
    chk.pack(anchor="w", pady=2)
    tarefas[tarefa] = var

# Adicionar nova tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get().strip()
    if tarefa:
        if tarefa in tarefas:
            messagebox.showwarning("Aviso", "Essa tarefa já existe!")
        else:
            adicionar_checkbox(tarefa)
            entrada_tarefa.delete(0, END)
            salvar_tarefas()

# Remover tarefas concluídas
def remover_tarefas():
    for tarefa, var in list(tarefas.items()):
        if var.get() == 1:  # Se marcada como concluída
            tarefas.pop(tarefa)
            for widget in frame_tarefas.winfo_children():
                if widget.cget("text") == tarefa:
                    widget.destroy()
    salvar_tarefas()

# Label do título
lb_title = Label(tela1, text='TO-DO LIST', font='Times 20 bold', bg=azul, fg=branco, anchor='w', padx=260)
lb_title.place(width=700, height=50, x=0, y=0)

# Entrada de texto para adicionar tarefas
entrada_tarefa = Entry(tela1, width=40, font="Arial 14")
entrada_tarefa.place(x=50, y=70, width=500, height=40)

# Botão para adicionar tarefa
btn_adicionar = Button(tela1, text="Adicionar Tarefa", font="Arial 12 bold", bg=azul, fg=branco, command=adicionar_tarefa)
btn_adicionar.place(x=560, y=70, width=130, height=40)

# Frame para lista de tarefas
frame_tarefas = Frame(tela1, bg=branco)
frame_tarefas.place(x=50, y=130, width=600, height=600)

# Botão para remover tarefas concluídas
btn_remover = Button(tela1, text="Remover Concluídas", font="Arial 12 bold", bg=azul, fg=branco, command=remover_tarefas)
btn_remover.place(x=250, y=750, width=200, height=40)

# Carregar tarefas do ficheiro ao iniciar
carregar_tarefas()

# Iniciar interface gráfica
tela1.mainloop()
