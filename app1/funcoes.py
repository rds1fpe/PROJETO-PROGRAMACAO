from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox

#dicionários que serão manipulados durante a execução do programa
dic_livros = {}
dic_cliente = {}


#botão para fechar a tela
def sair(tela1):
    tela1.destroy()

def cadastrar():
    arquivo_livros = open('livros.txt','a')
    if id_livro.get() in dic_livros:
        print('oi')
        messagebox.showinfo("Ops!","Livro já regitrado.")
    else:
        dic_livros[id_livro.get()] = [nome_livro.get(), ano_livro.get(), autor_livro.get()]
    for item in dic_livros:
        arquivo_livros.write(id_livro.get()+",")
        arquivo_livros.write(nome_livro.get()+",")
        arquivo_livros.write(ano_livro.get()+",")
        arquivo_livros.write(autor_livro.get()+"\n")
    
    arquivo_livros.close()



def criar_tela_cadastro():
    janela_cadastro = Toplevel()
    janela_cadastro.geometry("300x300+300+100")
    global id_livro
    global nome_livro
    global ano_livro
    global autor_livro

    #Entradas do usuario qu serão salvas no dicionário
    label_id = Label(janela_cadastro, width=15, text='ID(Identificador)', font="Times 12")
    label_id.place(x=-15,y=30)
    id_livro = Entry(janela_cadastro, width=30)
    id_livro.place(x=2, y=50)

    label_nome = Label(janela_cadastro, width=10, height=1, text='NOME',font="Times 12 bold")
    label_nome.place(x=-20,y=80)
    nome_livro = Entry(janela_cadastro, width=30)
    nome_livro.place(x=2, y=100)

    label_ano = Label(janela_cadastro, width=10, height=1 ,text='ANO',font="Times 12 bold")
    label_ano.place(x=-27,y=130)
    ano_livro = Entry(janela_cadastro, width=30)
    ano_livro.place(x=2, y=150)

    label_autor = Label(janela_cadastro, width=10, height=1, text='AUTOR',font="Times 12 bold")
    label_autor.place(x=-17,y=180)
    autor_livro = Entry(janela_cadastro, width=30)
    autor_livro.place(x=2, y=200)

    botao_cadastrar = Button(janela_cadastro,text="CADASTRAR",font='Times 10 bold',command=cadastrar)
    botao_cadastrar.place(x=5, y=270)

    botao_fechar = Button(janela_cadastro, text="VOLTAR", command=lambda:sair(janela_cadastro))
    botao_fechar.place(x=235, y=270)
    



































