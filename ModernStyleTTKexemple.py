# -*- coding: utf-8 -*-
from tkinter import Tk, PhotoImage
from tkinter import Entry as tkEntry
from tkinter.ttk import Frame, Label, Button, Entry, Separator, Style


# funcoes
def login():
    et_email.delete(0, 'end')
    et_senha.delete(0, 'end')
    et_email.focus_force()

def nova_conta():
    et_email.focus_force()

# primeira linha
root = Tk()

# frames
borda = Frame(root, style='Borda.TFrame')
borda.pack(fill='x', expand=True)

topo = Frame(borda)
topo.pack()

centro = Frame(borda)
centro.pack()

base = Frame(borda)
base.pack()

# logo = PhotoImage(file=r'img/logo_d.png')
# lb_logo = Label(topo, image=logo)
# lb_logo.image = logo
# lb_logo.pack()

Label(centro, text='E-mail').pack(anchor='w', pady=(10,0))
et_email = tkEntry(centro, font=('Montserrat', 12, 'bold'), fg='#666', relief='flat', 
        highlightbackground='white', highlightcolor='white')
et_email.focus_force()
et_email.pack(fill='x')
Separator(centro, orient='horizontal').pack(fill='x')

Label(centro, text='Senha').pack(anchor='w', pady=(10,0))
et_senha =  tkEntry(centro, show='*', font=('Montserrat', 12, 'bold'), fg='#666', relief='flat', 
        highlightbackground='white', highlightcolor='white')
et_senha.pack()
Separator(centro, orient='horizontal').pack(fill='x', pady=(0,20))

Button(base, text='ENTRAR', command=login, cursor='hand1').pack(fill='x', pady=(0,10))
Label(base, text='Ainda não tens uma conta? ', style='Small.TLabel').pack(side='left')
Button(base, text='Crie agora.', command=nova_conta, cursor='hand1', style='Small.TButton').pack(side='left')


# fontes
Tfont = ('Montserrat ExtraBold', 22)
Pfont = ('Montserrat', 10)
Pfontb = ('Montserrat', 12, 'bold')
Sfont = ('Montserrat', 8)


# estilo
style = Style()
style.theme_use('default')
style.configure('TFrame', background='#fff')
style.configure('Borda.TFrame', width=300)
style.configure('TLabel', justify='right', font=Pfont, background='#fff', foreground='#808080')
style.configure('Small.TLabel', font=Sfont)
style.configure('TButton', padding=(60,7), font=Pfontb, foreground='#fff', background='#20bcbb', relief='')
style.configure('Small.TButton', padding=(0,-3), font=Sfont, width=0, height=0, foreground='#20bcbb', background='#fff', relief='')
style.configure('TSeparator', background='#bafafa')

style.map('TButton',
        foreground=[('pressed', '#e25ca5'), ('active', '#fff')],
        background=[('pressed', '!focus', '#3f8efc'), ('active', '#025b5a')],
        relief=[('pressed', 'flat'), ('!pressed', 'flat')])

style.map('Small.TButton',
        foreground=[('pressed', '#f3bb30'), ('active', '#025b5a')],
        background=[('pressed', '!focus', '#3f8efc'), ('active', '#fff')],
        relief=[('pressed', 'flat'), ('!pressed', 'flat')])

# ultimas linhas
root.title('Design moderno - tkinter')
root.geometry('400x550+100+100')
# root.iconphoto(False, PhotoImage(file='img/logo_da.png'))
root.configure(bg='#fff')
root.mainloop()
