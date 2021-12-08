from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox

#dicionários que serão manipulados durante a execução do programa
dic_livros = {}
dic_cliente = {}
lista_livros = []


#adicionando as informações do arquivo no dicionario
arquivo_livro = open('livros.txt','r')
for linha in arquivo_livro:
    linha = linha.strip()
    lista_livros.append(linha)
arquivo_livro.close()

auxiliar = 0
for livro in lista_livros:
    #criando uma lista separando cada item por virgula(arquivo separado por virgula no arquivo)
    lista_separada = (lista_livros[auxiliar].split(","))
    #lista onde cada item é uma informação do livro
    info_livros = [lista_separada[1], lista_separada[2], lista_separada[3]]
    dic_livros[lista_separada[0]] = info_livros
    auxiliar += 1

#botão para fechar a tela
def sair(tela1):
    tela1.destroy()

#Função responsável por cadastrar o livro num dicionario e escrever as informações do mesmo no arquivo
def cadastrar():
    arquivo_livro = open('livros.txt','a')
    if id_livro.get() in dic_livros:
        print('oi')
        messagebox.showinfo("Ops!","Livro já registrado.")
        sair(janela_cadastro)
    elif id_livro.get() == "" or nome_livro.get() == "" or ano_livro.get() == "" or autor_livro == "":
        messagebox.showerror("Ops!","Preencha todos os campos.")
    else:
        dic_livros[id_livro.get()] = [nome_livro.get(), ano_livro.get(), autor_livro.get()]
        arquivo_livro.write(id_livro.get()+",")
        arquivo_livro.write(nome_livro.get()+",")
        arquivo_livro.write(ano_livro.get()+",")
        arquivo_livro.write(autor_livro.get()+"\n")
        messagebox.showinfo("Sucesso!","Livro adicionado com sucesso.")
        sair(janela_cadastro)
        
    arquivo_livro.close()
    
#Função que cria tela de cadastro
def criar_tela_cadastro():
    global janela_cadastro
    global id_livro
    global nome_livro
    global ano_livro
    global autor_livro

    janela_cadastro = Toplevel()
    janela_cadastro.geometry("480x480+641+0")
    janela_cadastro.config(bg="#1d475d")
    janela_cadastro.resizable(FALSE,FALSE)

    #Entradas do usuario qu serão salvas no dicionário
    label_id = Label(janela_cadastro, width=15, text='ID(Identificador)', font="Times 12",fg="white",bg="#1d475d")
    label_id.place(x=-15,y=30)
    id_livro = Entry(janela_cadastro, width=30)
    id_livro.place(x=2, y=50)

    label_nome = Label(janela_cadastro, width=10, height=1, text='NOME',font="Times 12 bold",fg="white",bg="#1d475d")
    label_nome.place(x=-20,y=80)
    nome_livro = Entry(janela_cadastro, width=30)
    nome_livro.place(x=2, y=100)

    label_ano = Label(janela_cadastro, width=10, height=1 ,text='ANO',font="Times 12 bold",fg="white",bg="#1d475d")
    label_ano.place(x=-27,y=130)
    ano_livro = Entry(janela_cadastro, width=30)
    ano_livro.place(x=2, y=150)

    label_autor = Label(janela_cadastro, width=10, height=1, text='AUTOR',font="Times 12 bold",fg="white",bg="#1d475d")
    label_autor.place(x=-17,y=180)
    autor_livro = Entry(janela_cadastro, width=30)
    autor_livro.place(x=2, y=200)

    botao_cadastrar = Button(janela_cadastro,text="CADASTRAR", width= 25, font='Times 10 bold',command=cadastrar, fg="#ed823b")
    botao_cadastrar.place(x=2, y=270)

    botao_fechar = Button(janela_cadastro, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(janela_cadastro))
    botao_fechar.place(x=2, y=310)
    
#Compara a entrada do Entry com o item no dicionário, se True, retorna as informações dos livros
def pesquisar():
    #Limpa a pesquisa antes de mostrar um novo resultado
    for item in tv.get_children():
        tv.delete(item)
    if entrada_pesquisa.get() in dic_livros:
        tv.insert("","end", values=(entrada_pesquisa.get(),
        dic_livros[entrada_pesquisa.get()][0],
        dic_livros[entrada_pesquisa.get()][1],
        dic_livros[entrada_pesquisa.get()][2]))
    else:
        messagebox.showerror("Ops!","Livro não encontrado!")

#Limpa a pesquisa
def limpar():
    for item in tv.get_children():
        tv.delete(item)

def criar_tela_pesquisa():
    global tv
    global entrada_pesquisa
    tela_pesquisa = Toplevel()
    tela_pesquisa.geometry("480x480+641+0")
    tela_pesquisa.config(bg="#1d475d")
    tela_pesquisa.resizable(0, 0)

    tv=ttk.Treeview(tela_pesquisa,columns=('ID','Título','Ano','Autor'),show='headings')
    tv.column('ID',minwidth=0, width=80)
    tv.column('Título',minwidth=0, width=190) 
    tv.column('Ano',minwidth=0, width=55) 
    tv.column('Autor',minwidth=0, width=121) 

    tv.heading('ID', text='ID')
    tv.heading('Título', text='Título')
    tv.heading('Ano', text='Ano')
    tv.heading('Autor', text='Autor')
    tv.place(x=0, y=80)

    radioValue = IntVar() 

    radio_pesquisa1 = Radiobutton(tela_pesquisa, text='ID', font='Time 10 bold', fg="black", bg="#1d475d", variable=radioValue)
    radio_pesquisa2 = Radiobutton(tela_pesquisa, text='Título', font='Time 10 bold', fg="black", bg="#1d475d", variable= radioValue)
    radio_pesquisa3 = Radiobutton(tela_pesquisa, text='Autor', font='Time 10 bold', fg="black", bg="#1d475d", variable=radioValue)

    radio_pesquisa1.place(x=2, y=30)
    radio_pesquisa2.place(x=60, y=30)
    radio_pesquisa3.place(x=128, y=30) 

    entrada_pesquisa = Entry(tela_pesquisa, width=30)
    entrada_pesquisa.place(x=2, y=0, height= 25)

    botao_pesquisa = Button(tela_pesquisa, text='Pesquisa', font='Times 10 bold', command=pesquisar)
    botao_pesquisa.place(x=200,y=0)

    botao_limpar = Button(tela_pesquisa, text='Limpar',font='Time 10 bold', command=limpar)
    botao_limpar.place(x=392,y=0)

    botao_mostrar_tudo = Button(tela_pesquisa, text="MOSTRAR TUDO", width=25, fg="#042c44")
    botao_mostrar_tudo.place(x=2, y=310)

    botao_fechar = Button(tela_pesquisa, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(tela_pesquisa))
    botao_fechar.place(x=2, y=350)

    
    





































