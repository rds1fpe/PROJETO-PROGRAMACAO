from tkinter import*
from tkinter import ttk
from tkinter import font
from types import BuiltinFunctionType
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
def sair(tela):
    tela.destroy()

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
        if  entrada_pesquisa.get() == "":
            messagebox.showerror("Ops!", "Digite o ISBN do livro que deseja pesquisar")

        elif (entrada_pesquisa.get().lower()) in dic_livros:
            tv.insert("","end", values=(entrada_pesquisa.get().lower(), #inserindo ID na grade
            dic_livros[entrada_pesquisa.get().lower()][0], #inserindo Título na grande
            dic_livros[entrada_pesquisa.get().lower()][1], #inserindo Ano na grade
            dic_livros[entrada_pesquisa.get().lower()][2]))#inserindo Autor na grade
        else:
            messagebox.showerror("Ops!","Livro não encontrado!")
    
    elif radioValue.get() == 2:

        if entrada_pesquisa.get() == "":
            messagebox.showerror("Ops!", "Digite o título do livro que deseja pesquisar")

        elif entrada_pesquisa.get().lower() in dic_titulo:
            tv.insert("","end", values=(dic_titulo[entrada_pesquisa.get().lower()][0], # inserindo ID na grade
            dic_titulo[entrada_pesquisa.get().lower()][1], #inserindo Título na grade
            dic_titulo[entrada_pesquisa.get().lower()][2], #inserindo ano na grade
            dic_titulo[entrada_pesquisa.get().lower()][3])) #inserindo autor na grade
        else:
            messagebox.showerror("Ops!","Livro não encontrado!")

    elif radioValue.get() == 3:

        aux_autor = 0
        if entrada_pesquisa.get() == "":
            messagebox.showerror("Ops!", "Digite o Autor que deseja pesquisar")

        elif entrada_pesquisa.get().lower() not in dic_autor:
            messagebox.showerror("Ops!","Livro não encontrado!")
        else:
            for autor in lista_autor:
                if lista_autor[aux_autor][3] == entrada_pesquisa.get().lower():
                    tv.insert("","end", values=(lista_autor[aux_autor][0].lower(), # inserindo ID na grade
                    lista_autor[aux_autor][1], #inserindo Título na grade
                    lista_autor[aux_autor][2], #inserindo ano na grade
                    lista_autor[aux_autor][3])) #inserindo autor na grade
            
                aux_autor += 1


#criando tela de cadastro
def criar_tela_pesquisa():
    global tv
    global entrada_pesquisa
    global radioValue

    tela_pesquisa = Toplevel()
    tela_pesquisa.geometry("480x480+641+0")
    tela_pesquisa.config(bg="#D3D3D3")
    tela_pesquisa.resizable(0, 0)

    titulo_tela_pes = Label(tela_pesquisa, text= "PESQUISAR LIVROS", relief='groove')
    titulo_tela_pes.config(font='Arial 18 bold',fg='black', width=37, height=2, bg="white")
    titulo_tela_pes.place(x=-30, y=0)

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
    radio_pesquisa1.config(text='ID', font='Arial 10 bold', fg="black", bg="#D3D3D3", variable=radioValue, value= 1)
    radio_pesquisa1.place(x=2, y=100)

    radio_pesquisa2 = Radiobutton(tela_pesquisa, )
    radio_pesquisa2.config(text='Título', font='Arial 10 bold', fg="black", bg="#D3D3D3", variable= radioValue, value= 2)
    radio_pesquisa2.place(x=60, y=100)

    radio_pesquisa3 = Radiobutton(tela_pesquisa)
    radio_pesquisa3.config(text='Autor',font='Arial 10 bold',fg="black",bg="#D3D3D3",variable=radioValue,value= 3)
    radio_pesquisa3.place(x=128, y=100) 

    #Entrada da pesquisas
    entrada_pesquisa = Entry(tela_pesquisa, width=30)
    entrada_pesquisa.place(x=2, y=70, height= 25)

    botao_pesquisa = Button(tela_pesquisa, text='Pesquisa', font='Times 10 bold', command=pesquisar)
    botao_pesquisa.place(x=200,y=70)

    botao_limpar = Button(tela_pesquisa, text='Limpar',font='Time 10 bold', command=limpar)
    botao_limpar.place(x=392,y=70)

    botao_mostrar_tudo = Button(tela_pesquisa, text="MOSTRAR TUDO", font='Arial 10 bold', width=22, fg="black", command=mostrar_tudo)
    botao_mostrar_tudo.place(x=2, y=380)

    botao_selecionar = Button(tela_pesquisa, text= 'SELECIONAR', font="Arial 10 bold", width=20, command=selecionar)
    botao_selecionar.place(x=280, y=380)

    botao_fechar = Button(tela_pesquisa, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(tela_pesquisa))
    botao_fechar.place(x=2, y=420)

def selecionar():
    selected = tv.focus()
    selecionados = tv.item(selected, 'values')
    print(selecionados)


def criar_tela_cliente():
    
    tela_cliente = Toplevel()
    tela_cliente.geometry("480x480+641+0")
    tela_cliente.config(bg="#D3D3D3")
    tela_cliente.resizable(0, 0)

    titulo_tela_cli = Label(tela_cliente, text= "CADASTRAR CLIENTE", relief='groove')
    titulo_tela_cli.config(font='Arial 18 bold',fg='black', width=37, height=2, bg="white")
    titulo_tela_cli.place(x=-35, y=0)

    main_label_cli = Label(tela_cliente, width=65, height=20, relief="groove")
    main_label_cli.place(x=10, y=71)

    #Entry e Combobox para obter os dados do cliente
    entry_cpf = Entry(main_label_cli, width=30)
    entry_cpf.place(x=10, y=35)

    entry_nome = Entry(main_label_cli, width=30)
    entry_nome.place(x=260, y=35)

    entry_email = Entry(main_label_cli, width=30)
    entry_email.place(x=10, y=95)

    entry_numero = Entry(main_label_cli, width=30)
    entry_numero.place(x=260, y=95)

    selected_combo_sexo = StringVar()
    values_combo = ["Masculino","Feminino"]
    sexo_cliente = ttk.Combobox(main_label_cli, width=27, values=values_combo)
    sexo_cliente.place(x= 10, y=155)

    selected_combo_dia = StringVar()
    values_dia = []
    for x in range(1,31):
        values_dia.append(x)

    combo_dia = ttk.Combobox(main_label_cli, width=3, values=values_dia)
    combo_dia.place(x=260, y=155)

    selected_combo_mes = StringVar()
    values_mes = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    combo_mes = ttk.Combobox(main_label_cli, width=9, values=values_mes)
    combo_mes.place(x=308, y=155)

    selected_combo_ano = StringVar()
    values_ano = []
    for x in range(1900,2021):
        values_ano.append(x)
    combo_ano = ttk.Combobox(main_label_cli, width=5, values=values_ano)
    combo_ano.place(x=390, y=155)

    entry_endereco = Entry(main_label_cli, width=50)
    entry_endereco.place(x=10, y=215)

    entry_numero = Entry(main_label_cli, width=5)
    entry_numero.place(x=330, y=215)

    selected_combo_estado = StringVar()
    values_estados = ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]
    entry_estado = ttk.Combobox(main_label_cli, width=5, values=values_estados)
    entry_estado.place(x=400, y=215, height=20)

    label_cpf = Label(main_label_cli, text="* CPF").place(x=5,y=13)
    label_nome = Label(main_label_cli, text="* Nome").place(x=260, y=13)
    label_email = Label(main_label_cli, text="* E-mail").place(x=5, y=73)
    label_numero = Label(main_label_cli, text="* Número").place(x=260, y=73)
    label_sexo = Label(main_label_cli, text="* Sexo").place(x=5, y=133)
    label_dma = Label(main_label_cli, text="* Data de Nascimento DD/MM/AAAA", font="Arial 8").place(x=258, y=133)
    label_endereco = Label(main_label_cli, text="* Endereço").place(x=5, y=193)
    label_n = Label(main_label_cli, text="* N°").place(x=325, y=193)
    label_uf = Label(main_label_cli, text="* UF").place(x=395, y=193)

    botao_salvar = Button(tela_cliente, text="SALVAR",font="Arial 9 bold" , width=22)
    botao_salvar.place(x=10, y=380)

    botao_voltar = Button(tela_cliente, text="VOLTAR", width=22, command=lambda:sair(tela_cliente))
    botao_voltar.place(x=10, y=420)








#Função responsável por cadastrar o livro num dicionario e escrever as informações do mesmo no arquivo
def cadastrar():
    arquivo_livro = open('livros.txt','a')
    if id_livro.get() in dic_livros:
        messagebox.showinfo("Ops!","Livro já registrado.")
        sair(janela_cadastro)
    elif id_livro.get() == "" or nome_livro.get() == "" or ano_livro.get() == "":
        messagebox.showerror("Ops!","Preencha todos os campos.")

    elif autor_livro.get() == "":
        dic_livros[id_livro.get().lower()] = [nome_livro.get().lower(), ano_livro.get(), "desconhecido" ]
        dic_titulo[nome_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido"]
        dic_autor[autor_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido"]
        lista_autor.append([id_livro.get(), nome_livro.get().lower(), ano_livro.get(), "desconhecido"])
        arquivo_livro.write(id_livro.get().lower()+",")
        arquivo_livro.write(nome_livro.get().lower()+",")
        arquivo_livro.write(ano_livro.get().lower()+",")
        arquivo_livro.write("desconhecido"+"\n")
        messagebox.showinfo("Sucesso!","Livro adicionado com sucesso.")
        sair(janela_cadastro)
        arquivo_livro.close()

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

    fundo_tela_casdastro = Label(janela_cadastro, width=66, height=15 ,borderwidth=4, relief='groove')
    fundo_tela_casdastro.place(x=-20, y=71)

    label_texto_pes = Label(janela_cadastro)
    label_texto_pes.config(bg="#D3D3D3", fg="black", font='Arial 7', text='Todo os itens que possuem ( * ) são obrigatórios', width=50, height=1)
    label_texto_pes.place(x=145,y=310)

    titulo_tela = Label(janela_cadastro, text= 'CADASTRAR LIVRO')
    titulo_tela.config(font='Arial 18 bold',fg='black', width=37, height=2, bg="white", relief='groove')
    titulo_tela.place(x=-30, y=0)

    #Entradas do usuario que serão salvas no dicionário
    label_id = Label(janela_cadastro, width=15, text='* ISBN', font="Arial 9", fg="black")
    label_id.place(x=-33,y=80)
    id_livro = Entry(janela_cadastro, width=30)
    id_livro.place(x=2, y=100)

    label_nome = Label(janela_cadastro, width=10, height=1, text='* Nome',font="Arial 9", fg="black")
    label_nome.place(x=-14,y=130)
    nome_livro = Entry(janela_cadastro, width=30)
    nome_livro.place(x=2, y=150)

    label_ano = Label(janela_cadastro, width=10, height=1 ,text='* Ano',font="Arial 9", fg="black")
    label_ano.place(x=-21,y=180)
    ano_livro = Entry(janela_cadastro, width=30)
    ano_livro.place(x=2, y=200)

    label_autor = Label(janela_cadastro, width=10, height=1, text='Autor',font="Arial 9", fg="black")
    label_autor.place(x=-19,y=230)
    autor_livro = Entry(janela_cadastro, width=30)
    autor_livro.place(x=2, y=250)

    botao_cadastrar = Button(janela_cadastro,text="CADASTRAR", width= 22, font='Arial 10 bold',command=cadastrar)
    botao_cadastrar.place(x=2, y=310)

    botao_fechar = Button(janela_cadastro, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(janela_cadastro))
    botao_fechar.place(x=2, y=350)
    

    
    





































