from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox


aux = 0
caminho = "PROJETO-PROGRAMACAO/app1/images/"

dic_livros = {1:['Era uma vez em Hollywood','Ronaldo','2021','terror'], 2:['O Capital','Karl Marx', '1880','Sociologia']}


tela_inicial =Tk()
tela_inicial.geometry ("640x480+300+100")
tela_inicial.title("Library Sis")
tela_inicial.iconbitmap(caminho+"icon.ico")   
tela_inicial.resizable(0,0)

#imagem de fundo
img_bg = ImageTk.PhotoImage(Image.open(caminho+"bg.jpg"))
label_tela = Label(tela_inicial, image = img_bg).place(x=-5,y=0)

#logo
logo = ImageTk.PhotoImage(Image.open(caminho+"logo.png"))
label_logo = Label(tela_inicial, image = logo, borderwidth=0).place(x=223,y=10)

#Label para Matricula e Senha
label_ms = Label(tela_inicial, background='#04344c', width=30, height=10, borderwidth=2, relief='ridge')
label_ms.place(x=215, y=170)

#Label tela de Login
label_user = Label(tela_inicial, text="USUÁRIO",foreground='white',  font=('Helvetica',11, 'bold'), bg='#04344c')
label_user.place(x=230, y=180)

label_passw = Label(tela_inicial, text="SENHA",foreground='white',  font=('Helvetica', 11, 'bold'), bg='#04344c',)
label_passw.place(x=230, y=240)

#Entry da tela de Login
texto_user = StringVar()
user_entry = Entry(tela_inicial, width=30, textvariable=texto_user)
user_entry.place(x=230, y=205)

texto_passw = StringVar()
user_passw = Entry(tela_inicial, width=30, textvariable=texto_passw)
user_passw.config(show='*')
user_passw.place(x=230, y=265)



#botão para fechar as duas telas
def sair(tela1, tela2):
    tela1.destroy()
    tela2.destroy()


#Criando Janela principal com TopLevel
def principal():
    janela_principal = Toplevel(tela_inicial)
    janela_principal.title("Library Sis")
    janela_principal.geometry("640x480+300+100")
    janela_principal.resizable(0, 0)
    janela_principal.config(bg='#04344c')

    #Criando Abas e definindo tamanho e estilo
    aba_notebook = ttk.Notebook(janela_principal)
    aba_notebook.place(x=20, y=50)
    mostrar_frame  = Frame(aba_notebook, width=600, height=360, borderwidth=4, relief='ridge')
    pesquisa_frame = Frame(aba_notebook, width=600, height=360, borderwidth=4, relief='ridge')
    cadastro_frame = Frame(aba_notebook, width=600, height=360, borderwidth=4, relief='ridge')
    aluguel_frame  = Frame(aba_notebook, width=600, height=360, borderwidth=4, relief='ridge')
    devolver_frame = Frame(aba_notebook, width=600, height=360, borderwidth=4, relief='ridge')
    #Adicionando abas em seus respectivos Frames
    aba_notebook.add(mostrar_frame,  text= 'Mostrar tudo' )
    aba_notebook.add(pesquisa_frame, text= 'Pesquisar') 
    aba_notebook.add(cadastro_frame, text= 'Cadastrar')
    aba_notebook.add(aluguel_frame,  text= 'Alugar')
    aba_notebook.add(devolver_frame, text= 'Devolver')

   
    #função para mostrar tudo
    
    def mostrar_tudo():
        aux = 1
        for item in dic_livros:
            listar_livros.insert(END,f"Nome: {dic_livros[aux][0]}")
            listar_ano.insert(END,f"Ano: {dic_livros[aux][2]}")
            aux += 1

    #botão para mostrar todos os livros
    button_mostrar = Button(mostrar_frame, text= 'Mostrar tudo', command=mostrar_tudo)
    button_mostrar.place(x=10, y=5)
    #Listbox para mostrar todos os livros
    listar_livros = Listbox(mostrar_frame,  width=47, height=18)
    listar_livros.place(x=10, y=30) 
    listar_ano = Listbox(mostrar_frame,  width=47, height=18)
    listar_ano.place(x=299, y=30)
    

    #Label para texto de boas vinda
    label_welcome = Label(janela_principal, text='Bem-vindo ao Library Sis', font=('Helvetica', 20, 'bold'), bg='#04344c')
    label_welcome.config(foreground= '#f49c62')
    label_welcome.place(x=20, y=10)

    #Botão para sair do programa!
    botao1 = Button(janela_principal, text='Sair',font=('Helvetica', 8, 'bold'), width=10, command=lambda:sair(janela_principal,tela_inicial))
    botao1.place(x=545, y=443)



#Função de login e crição da tela principal
def login():
    if texto_user.get() == 'admin' and user_passw.get() == "admin":
        principal()
    else:
        messagebox.showinfo("Tente novamente", "Apenas o Administrador pode fazer login")
        
#Botão de Login
Login_button = Button(tela_inicial, text= "Login", font=('Helvetica', 8, 'bold') , width=10, command=login)
Login_button.place(x=230, y=295)


#mainloop executa o loop que permite a janela permanecer aberta
tela_inicial.mainloop()


