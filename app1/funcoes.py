from os import truncate
from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox


#dicionários que serão manipulados durante a execução do programa
dic_livros = {}
dic_titulo = {}
dic_autor = {}
lista_autor = [] # Lista para a busca de autores 
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
    info_id = [lista_separada[1].lower(), lista_separada[2], lista_separada[3].lower()]
    info_titulo_autor = [lista_separada[0].lower(),lista_separada[1].lower(), lista_separada[2], lista_separada[3].lower()] 
    dic_livros[lista_separada[0].lower()] = info_id
    dic_titulo[lista_separada[1].lower()] = info_titulo_autor
    dic_autor [lista_separada[3].lower()] = info_titulo_autor
    lista_autor.append(info_titulo_autor)
    auxiliar += 1

#botão para fechar a tela
def sair(tela1):
    tela1.destroy()

#Limpa a pesquisa
def limpar():
    for item in tv.get_children():
        tv.delete(item)

#mostra todos os livros cadastrados na tela de pesquisa
def mostrar_tudo():
    limpar()
    for item in dic_livros:
        tv.insert("","end", values=(item,
        dic_livros[item][0],
        dic_livros[item][1],
        dic_livros[item][2]))
    sep = 100*("-")
    print(dic_livros)
    print(sep)
    print(dic_titulo)
    print(sep)
    print(dic_autor)
    print(sep)
    print(lista_autor)

#Compara a entrada do Entry com o item no dicionário, se True, retorna as informações dos livros
def pesquisar():
    #Limpa a pesquisa antes de mostrar um novo resultado
    limpar()

    if radioValue.get() == 1:
        if (entrada_pesquisa.get().lower()) in dic_livros:
            tv.insert("","end", values=(entrada_pesquisa.get().lower(), #inserindo ID na grade
            dic_livros[entrada_pesquisa.get().lower()][0], #inserindo Título na grande
            dic_livros[entrada_pesquisa.get().lower()][1], #inserindo Ano na grade
            dic_livros[entrada_pesquisa.get().lower()][2]))#inserindo Autor na grade
        else:
            messagebox.showerror("Ops!","Livro não encontrado!")
    
    elif radioValue.get() == 2:
        if entrada_pesquisa.get().lower() in dic_titulo:
            tv.insert("","end", values=(dic_titulo[entrada_pesquisa.get().lower()][0], # inserindo ID na grade
            dic_titulo[entrada_pesquisa.get().lower()][1], #inserindo Título na grade
            dic_titulo[entrada_pesquisa.get().lower()][2], #inserindo ano na grade
            dic_titulo[entrada_pesquisa.get().lower()][3])) #inserindo autor na grade
        else:
            messagebox.showerror("Ops!","Livro não encontrado!")

    elif radioValue.get() == 3:
        aux_autor = 0
        if entrada_pesquisa.get().lower() not in dic_autor: #dicionario de autor necessário apenas para verificação da existencia do autor no dicionario
                messagebox.showerror("Ops!","Livro não encontrado!")
        else:
            for autor in lista_autor:
                if lista_autor[aux_autor][3] == entrada_pesquisa.get().lower():
                    tv.insert("","end", values=(lista_autor[aux_autor][0].lower(), # inserindo ID na grade
                    lista_autor[aux_autor][1], #inserindo Título na grade
                    lista_autor[aux_autor][2], #inserindo ano na grade
                    lista_autor[aux_autor][3])) #inserindo autor na grade
            
                aux_autor += 1

def editar():
   
    dic_livros[id_livro_ed.get()] = [nome_livro_ed.get(), ano_livro_ed.get(), autor_livro_ed.get()]
    dic_titulo[nome_livro_ed.get()] = [id_livro_ed.get(), nome_livro_ed.get(), ano_livro_ed.get(), autor_livro_ed.get()]
    dic_autor[id_livro_ed.get()] = [[autor_livro_ed.get()  ,nome_livro_ed.get(), ano_livro_ed.get(), autor_livro_ed.get()]]

    

    arquivo_livro = open("livros.txt","a")
    arquivo_livro.truncate(0)
    lista_autor.append([id_livro_ed.get(), nome_livro_ed.get(), ano_livro_ed.get(), autor_livro_ed.get()])
        
    
    aux_editar = 0
    for livro in dic_livros:
        arquivo_livro.write(str(lista_autor[aux_editar][0])+",")
        arquivo_livro.write(str(lista_autor[aux_editar][1])+",")
        arquivo_livro.write(str(lista_autor[aux_editar][2])+",")
        arquivo_livro.write(str(lista_autor[aux_editar][3])+"\n")

        aux_editar += 1
    arquivo_livro.close()






#Função responsável por editar o conteudo do livro com excesso do ISBN
def tela_edicao():

    global id_livro_ed
    global nome_livro_ed
    global ano_livro_ed
    global autor_livro_ed

    tela_edicao = Toplevel()
    tela_edicao.geometry("360x360+641+0")
    tela_edicao.resizable(0, 0)

    titulo_tela_ed = Label(tela_edicao, text= 'EDITAR LIVRO')
    titulo_tela_ed.config(font='Arial 12 bold',fg='#1d475d', width=37, height=2, bg="white", relief='groove')
    titulo_tela_ed.place(x=0, y=0)

    fundo_tela_ed = Label(tela_edicao, width=66, height=15 ,borderwidth=4, relief='groove')
    fundo_tela_ed.place(x=-20, y=71)

    selected = tv.focus()
    selecionados = tv.item(selected, 'values')

    #Entradas do usuario que serão salvas no dicionário
    label_id_ed = Label(tela_edicao, width=15, text='* ISBN', font="Arial 9",fg="black")
    label_id_ed['state'] = DISABLED
    label_id_ed.place(x=-35,y=80)
    id_livro_ed = Entry(tela_edicao, width=30)
    id_livro_ed.insert(0, selecionados[0])
    id_livro_ed['state'] = DISABLED
    id_livro_ed.place(x=2, y=100)

    label_nome_ed = Label(tela_edicao, width=10, height=1, text='* Nome',font="Arial 9",fg="black")
    label_nome_ed.place(x=-15,y=130)
    nome_livro_ed = Entry(tela_edicao, width=30)
    nome_livro_ed.insert(0, selecionados[1])
    nome_livro_ed.place(x=2, y=150)

    label_ano_ed = Label(tela_edicao, width=10, height=1 ,text='* Ano',font="Arial 9",fg="black")
    label_ano_ed.place(x=-22,y=180)
    ano_livro_ed = Entry(tela_edicao, width=30)
    ano_livro_ed.insert(0, selecionados[2])
    ano_livro_ed.place(x=2, y=200)

    label_autor_ed = Label(tela_edicao, width=10, height=1, text='Autor',font="Arial 9",fg="black")
    label_autor_ed.place(x=-19,y=230)
    autor_livro_ed = Entry(tela_edicao, width=30)
    autor_livro_ed.insert(0, selecionados[3])
    autor_livro_ed['state'] = DISABLED
    autor_livro_ed.place(x=2, y=250)

    botao_cadastrar_ed = Button(tela_edicao,text="SALVAR", width=15 , command=editar)
    botao_cadastrar_ed.place(x=2, y=320)

    botao_fechar_ed = Button(tela_edicao, text="VOLTAR", width=15, fg="#042c44", command=lambda:sair(tela_edicao))
    botao_fechar_ed.place(x=240, y=320)



    
#criando tela de cadastro
def criar_tela_pesquisa():
    global tv
    global entrada_pesquisa
    global radioValue


    tela_pesquisa = Toplevel()
    tela_pesquisa.geometry("480x480+641+0")
    tela_pesquisa.config(bg="#D3D3D3")
    tela_pesquisa.resizable(0, 0)

    titulo_tela_pes = Label(tela_pesquisa, text= 'CONSULTAR LIVROS', relief='groove')
    titulo_tela_pes.config(font='Arial 18 bold',fg='#1d475d', width=37, height=2, bg="white")
    titulo_tela_pes.place(x=-43, y=0)

    #Criando janela para visualização do conteudo em grade(TREEVIEW)
    tv=ttk.Treeview(tela_pesquisa,columns=('ID','Título','Ano','Autor'),show='headings', selectmode=BROWSE)
    #Scrollbar para facilitar a visualização do conteudo dentro do TreeView
    scroll_tv = Scrollbar(tv, orient='vertical', command=tv.yview)
    scroll_tv.place(x=430, y=30 ,height=190)
    tv.configure(yscrollcommand=scroll_tv.set)

    #Definições das colunas da grade
    tv.column('ID',minwidth=0, width=80)
    tv.column('Título',minwidth=0, width=190) 
    tv.column('Ano',minwidth=0, width=55) 
    tv.column('Autor',minwidth=0, width=121) 

    tv.heading('ID', text='ID')
    tv.heading('Título', text='Título')
    tv.heading('Ano', text='Ano')
    tv.heading('Autor', text='Autor')
    tv.place(x=0, y=150)

    #Estilo da TreeView
    style_tv = ttk.Style()
    style_tv.theme_use("clam")
    style_tv.configure("TreeView")


    #Criação dos Radiobuttons que serão usados como forma de filtrar o contéudo pesquisado
    #Variável responsável por obter o valor do RadioButton
    radioValue = IntVar(tela_pesquisa) 

    radio_pesquisa1 = Radiobutton(tela_pesquisa)
    radio_pesquisa1.config(text='ID', font='Time 10 bold', fg="black", bg="#D3D3D3", variable=radioValue, value= 1)
    radio_pesquisa1.place(x=2, y=100)

    radio_pesquisa2 = Radiobutton(tela_pesquisa, )
    radio_pesquisa2.config(text='Título', font='Time 10 bold', fg="black", bg="#D3D3D3", variable= radioValue, value= 2)
    radio_pesquisa2.place(x=60, y=100)

    radio_pesquisa3 = Radiobutton(tela_pesquisa)
    radio_pesquisa3.config(text='Autor',font='Time 10 bold',fg="black",bg="#D3D3D3",variable=radioValue,value= 3)
    radio_pesquisa3.place(x=128, y=100) 

    #Entrada da pesquisas
    entrada_pesquisa = Entry(tela_pesquisa, width=30)
    entrada_pesquisa.place(x=2, y=70, height= 25)

    botao_pesquisa = Button(tela_pesquisa, text='Pesquisa', font='Times 10 bold', command=pesquisar)
    botao_pesquisa.place(x=200,y=70)

    botao_limpar = Button(tela_pesquisa, text='Limpar',font='Time 10 bold', command=limpar)
    botao_limpar.place(x=392,y=70)

    botao_mostrar_tudo = Button(tela_pesquisa, text="MOSTRAR TUDO", font='Time 10 bold', width=22, command=mostrar_tudo)
    botao_mostrar_tudo.place(x=2, y=380)

    botao_selecionar = Button(tela_pesquisa, text= 'SELECIONAR', font="Time 10 bold", width=20, command=tela_edicao)
    botao_selecionar.place(x=280, y=380)

    botao_fechar = Button(tela_pesquisa, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(tela_pesquisa))
    botao_fechar.place(x=2, y=420)

#Função responsável por cadastrar o livro num dicionario e escrever as informações do mesmo no arquivo
def cadastrar():

    arquivo_livro = open('livros.txt','a')
    if id_livro.get() in dic_livros:
        messagebox.showinfo("Ops!","Livro já registrado.")

        sair(janela_cadastro)
    elif id_livro.get() == "" or nome_livro.get() == "" or ano_livro.get() == "" :
        messagebox.showerror("Ops!","Preencha todos os campos.")

    elif autor_livro.get() == "":
        dic_livros[id_livro.get().lower()] = [nome_livro.get().lower(), ano_livro.get(), "desconhecido"]
        dic_titulo[nome_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido"]
        dic_autor[autor_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido"]
        lista_autor.append([id_livro.get(), nome_livro.get().lower(), ano_livro.get(), "desconhecido"])
        arquivo_livro.write(id_livro.get().lower()+",")
        arquivo_livro.write(nome_livro.get().lower()+",")
        arquivo_livro.write(ano_livro.get().lower()+",")
        arquivo_livro.write("desconhecido"+"\n")
        messagebox.showinfo("Sucesso!","Livro adicionado com sucesso.")
        sair(janela_cadastro)

    else:
        dic_livros[id_livro.get().lower()] = [nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower()]
        dic_titulo[nome_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower()]
        dic_autor[autor_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower()]
        lista_autor.append([id_livro.get(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower()])
        arquivo_livro.write(id_livro.get().lower()+",")
        arquivo_livro.write(nome_livro.get().lower()+",")
        arquivo_livro.write(ano_livro.get().lower()+",")
        arquivo_livro.write(autor_livro.get().lower()+"\n")
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
    janela_cadastro.config(bg="#D3D3D3")
    janela_cadastro.resizable(FALSE,FALSE)

    fundo_tela_cadastro = Label(janela_cadastro, width=66, height=15 ,borderwidth=4, relief='groove')
    fundo_tela_cadastro.place(x=-20, y=71)

    label_texto_pes = Label(janela_cadastro)
    label_texto_pes.config(bg="#D3D3D3",
                        font= "Arial 7",
                        fg="black",
                        text='Todo os itens que possuem ( * ) são obrigatórios \n Caso o autor não seja preenchido \n será considerado Desconhecido',
                        width=50,
                        height=3)
    label_texto_pes.place(x=190,y=310)

    titulo_tela = Label(janela_cadastro, text= 'CADASTRAR LIVROS')
    titulo_tela.config(font='Arial 18 bold',fg='#1d475d', width=37, height=2, bg="white", relief='groove')
    titulo_tela.place(x=-35, y=0)

    #Entradas do usuario que serão salvas no dicionário
    label_id = Label(janela_cadastro, width=15, text='* ISBN', font="Arial 9",fg="black")
    label_id.place(x=-35,y=80)
    id_livro = Entry(janela_cadastro, width=30)
    id_livro.place(x=2, y=100)

    label_nome = Label(janela_cadastro, width=10, height=1, text='* Nome',font="Arial 9",fg="black")
    label_nome.place(x=-15,y=130)
    nome_livro = Entry(janela_cadastro, width=30)
    nome_livro.place(x=2, y=150)

    label_ano = Label(janela_cadastro, width=10, height=1 ,text='* Ano',font="Arial 9",fg="black")
    label_ano.place(x=-22,y=180)
    ano_livro = Entry(janela_cadastro, width=30)
    ano_livro.place(x=2, y=200)

    label_autor = Label(janela_cadastro, width=10, height=1, text='Autor',font="Arial 9",fg="black")
    label_autor.place(x=-19,y=230)
    autor_livro = Entry(janela_cadastro, width=30)
    autor_livro.place(x=2, y=250)

    botao_cadastrar = Button(janela_cadastro,text="CADASTRAR", width= 22, font='Arial 10 bold',command=cadastrar)
    botao_cadastrar.place(x=2, y=310)

    botao_fechar = Button(janela_cadastro, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(janela_cadastro))
    botao_fechar.place(x=2, y=350)
    

    
    





































