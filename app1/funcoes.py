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

def mostrar():
    print(criar_tela_cadastro.id_livro.get())
#arquivo que será usado como banco de dados e jogados nos dicionários
arquivo_livros = open("livros.txt","a")
arquivo_clientes = open("cliente.txt","a")


def criar_tela_cadastro():
    janela_cadastro = Toplevel()
    janela_cadastro.geometry("300x300+300+100")

    #Entradas do usuario qu serão salvas no dicionário
    label_id = Label(janela_cadastro, width=10, text='ID', font="Times 15 bold italic")
    label_id.place(x=-42,y=30)
    id_livro = Entry(janela_cadastro, width=20)
    id_livro.place(x=2, y=50)

    label_nome = Label(janela_cadastro, width=10, height=1, text='NOME',font="Times 15 bold italic")
    label_nome.place(x=-25,y=80)
    nome_livro = Entry(janela_cadastro, width=20)
    nome_livro.place(x=2, y=100)

    label_ano= Label(janela_cadastro, width=10, height=1 ,text='ANO',font="Times 15 bold italic")
    label_ano.place(x=-32,y=130)
    ano_livro = Entry(janela_cadastro, width=20)
    ano_livro.place(x=2, y=150)

    label_autor = Label(janela_cadastro, width=10, height=1, text='AUTOR',font="Times 15 bold italic")
    label_autor.place(x=-22,y=180)
    autor_livro = Entry(janela_cadastro, width=20)
    autor_livro.place(x=2, y=200)

    botao_cadastrar = Button(janela_cadastro,text="CADASTRAR",command=mostrar)
    botao_cadastrar.place(x=5, y=270)

    botao_fechar = Button(janela_cadastro, text="VOLTAR", command=lambda:sair(janela_cadastro))
    botao_fechar.place(x=235, y=270)
    
#def cadastrar():
    





































arquivo_livros.close()
arquivo_clientes.close()




