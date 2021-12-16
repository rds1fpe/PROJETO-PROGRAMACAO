from io import TextIOWrapper
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
lista_cliente = []
lista_livros = []
lista_numeros = []
lista_email = []
dic_endereco = {}


#adicionando as informações do arquivo no dicionario
arquivo_livro = open("livros.txt","r")
arquivo_cliente = open("cliente.txt","r")
for linha in arquivo_livro:
    linha = linha.strip()
    lista_livros.append(linha)
arquivo_livro.close()

for linha in arquivo_cliente:
    linha = linha.strip()
    lista_cliente.append(linha)
arquivo_cliente.close()

auxiliar = 0
for livro in lista_livros:
    #criando uma lista separando cada item por virgula(arquivo separado por virgula no arquivo)
    lista_separada = (lista_livros[auxiliar].split(","))
    #lista onde cada item é uma informação do livro
    info_id = [lista_separada[1].lower(), lista_separada[2], lista_separada[3].lower(), lista_separada[4]]
    info_titulo_autor = [lista_separada[0].lower(),lista_separada[1].lower(), lista_separada[2], lista_separada[3].lower(), lista_separada[4]] 
    dic_livros[lista_separada[0].lower()] = info_id
    dic_titulo[lista_separada[1].lower()] = info_titulo_autor
    dic_autor [lista_separada[3].lower()] = info_titulo_autor
    lista_autor.append(info_titulo_autor)
    auxiliar += 1

auxiliar_cliente = 0
for cliente in lista_cliente:
    lista_sep_cliente = (lista_cliente[auxiliar_cliente].split(","))
    info_cliente = [lista_sep_cliente[0].lower(), lista_sep_cliente[1].lower(), lista_sep_cliente[2].lower(), lista_sep_cliente[3].lower(),
                    lista_sep_cliente[4].lower(), lista_sep_cliente[5].lower(), lista_sep_cliente[6].lower(), lista_sep_cliente[7].lower(),
                    lista_sep_cliente[8].lower()]
    dic_cliente[lista_sep_cliente[0].lower()] = info_cliente
    lista_numeros.append(lista_sep_cliente[3])
    lista_email.append(lista_sep_cliente[2])
    auxiliar_cliente += 1
print(dic_cliente)
#botão para fechar a tela
def sair(tela):
    tela.destroy()

#Limpa a pesquisa
def limpar(tv):
    for item in tv.get_children():
        tv.delete(item)

#mostra todos os livros cadastrados na tela de pesquisa
def mostrar_tudo():
    limpar(tv)
    for item in dic_livros:
        tv.insert("","end", values=(item,
        dic_livros[item][0],
        dic_livros[item][1],
        dic_livros[item][2],
        dic_livros[item][3]))
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
    limpar(tv)

    if entrada_pesquisa.get() == "":
        messagebox.showerror("Ops!", "Digite o ISBN, Título ou Autor do livro que deseja pesquisar")

    elif radioValue.get() == 1:
        if  entrada_pesquisa.get() == "":
            messagebox.showerror("Ops!", "Digite o ISBN do livro que deseja pesquisar")

        elif (entrada_pesquisa.get().lower()) in dic_livros:
            tv.insert("","end", values=(entrada_pesquisa.get().lower(), #inserindo ID na grade
            dic_livros[entrada_pesquisa.get().lower()][0], #inserindo Título na grande
            dic_livros[entrada_pesquisa.get().lower()][1], #inserindo Ano na grade
            dic_livros[entrada_pesquisa.get().lower()][2],#inserindo Autor na grade
            dic_livros[entrada_pesquisa.get().lower()][3]))#inserindo quantidade na grade
        else:
            messagebox.showerror("Ops!","Livro não encontrado!")
    
    elif radioValue.get() == 2:

        if entrada_pesquisa.get() == "":
            messagebox.showerror("Ops!", "Digite o título do livro que deseja pesquisar")

        elif entrada_pesquisa.get().lower() in dic_titulo:
            tv.insert("","end", values=(dic_titulo[entrada_pesquisa.get().lower()][0], # inserindo ID na grade
            dic_titulo[entrada_pesquisa.get().lower()][1], #inserindo Título na grade
            dic_titulo[entrada_pesquisa.get().lower()][2], #inserindo ano na grade
            dic_titulo[entrada_pesquisa.get().lower()][3], #inserindo autor na grade
            dic_titulo[entrada_pesquisa.get().lower()][4]))#insetindo quantidade na grade
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
                    lista_autor[aux_autor][3], #inserindo autor na grade
                    lista_autor[aux_autor][4]))
            
                aux_autor += 1


#criando tela de cadastro
def criar_tela_pesquisa():
    global tv
    global entrada_pesquisa
    global radioValue
    global tela_pesquisa


    tela_pesquisa = Toplevel()
    tela_pesquisa.geometry("480x480+641+0")
    tela_pesquisa.config(bg="#D3D3D3")
    tela_pesquisa.resizable(0, 0)

    titulo_tela_pes = Label(tela_pesquisa, text= "PESQUISAR LIVROS", relief='groove')
    titulo_tela_pes.config(font='Arial 18 bold',fg='black', width=37, height=2, bg="white")
    titulo_tela_pes.place(x=-30, y=0)

    main_label_livro = Label(tela_pesquisa, width=65, height=25, relief="groove")
    main_label_livro.place(x=10, y=65)

    #Label pesquisa
    label_pesquisa = Label(main_label_livro, text="* ISBN")
    label_pesquisa.place(x=2, y=0)

    #Entrada da pesquisas
    entrada_pesquisa = Entry(main_label_livro, width=30)
    entrada_pesquisa.place(x=5, y=20, height= 25)

    #Criando janela para visualização do conteudo em grade(TREEVIEW)
    tv=ttk.Treeview(main_label_livro,columns=('ISBN','Título','Ano','Autor','Qntd'),show='headings', selectmode=BROWSE)
    #Scrollbar para facilitar a visualização do conteudo dentro do TreeView
    scroll_tv = Scrollbar(main_label_livro, orient='vertical', command=tv.yview)
    scroll_tv.place(x=432, y=125 ,height=200)
    tv.configure(yscrollcommand=scroll_tv.set)

    #Definições das colunas da grade
    tv.column('ISBN',minwidth=0, width=80)
    tv.column('Título',minwidth=0, width=130) 
    tv.column('Ano',minwidth=0, width=55) 
    tv.column('Autor',minwidth=0, width=121)
    tv.column('Qntd', minwidth=0, width=40) 

    tv.heading('ISBN', text='ISBN')
    tv.heading('Título', text='Título')
    tv.heading('Ano', text='Ano')
    tv.heading('Autor', text='Autor')
    tv.heading('Qntd', text='Qntd')
    tv.place(x=2, y=100)

    #Estilo da TreeView
    style_tv = ttk.Style()
    style_tv.theme_use("clam")
    style_tv.configure("TreeView")


    #Criação dos Radiobuttons que serão usados como forma de filtrar o contéudo pesquisado
    #Variável responsável por obter o valor do RadioButton
    radioValue = IntVar(tela_pesquisa) 

    radio_pesquisa1 = Radiobutton(main_label_livro)
    radio_pesquisa1.config(text='ISBN', font='Arial 10 bold', fg="black",  variable=radioValue, value= 1)
    radio_pesquisa1.place(x=2, y=50)

    radio_pesquisa2 = Radiobutton(main_label_livro, )
    radio_pesquisa2.config(text='Título', font='Arial 10 bold', fg="black", variable= radioValue, value= 2)
    radio_pesquisa2.place(x=60, y=50)

    radio_pesquisa3 = Radiobutton(main_label_livro)
    radio_pesquisa3.config(text='Autor',font='Arial 10 bold',fg="black", variable=radioValue,value= 3)
    radio_pesquisa3.place(x=128, y=50) 

    botao_pesquisa = Button(main_label_livro, text='Pesquisar', font='Times 10 bold', command=pesquisar)
    botao_pesquisa.place(x=200,y=20)

    botao_limpar = Button(main_label_livro, text='Limpar',font='Time 10 bold', command=lambda:limpar(tv))
    botao_limpar.place(x=374,y=20)

    botao_mostrar_tudo = Button(main_label_livro, text="MOSTRAR TUDO", font='Arial 10 bold', width=22, fg="black", command=mostrar_tudo)
    botao_mostrar_tudo.place(x=2, y=340)

    botao_selecionar = Button(main_label_livro, text= 'SELECIONAR', font="Arial 10 bold", width=20, command=selecionar)
    botao_selecionar.place(x=262, y=340)

    botao_fechar = Button(tela_pesquisa, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(tela_pesquisa))
    botao_fechar.place(x=15, y=450)

def selecionar():
    global selecionados
    selected = tv.focus()
    selecionados = tv.item(selected, 'values')
    if selected:
        ask = messagebox.askquestion("Continuar?","Livro selecionado, deseja abrir tela de cadastro de cliente?")
        if ask == "yes":
            print("Livro Selecionado: "+ selecionados[1])
            sair(tela_pesquisa)
            criar_tela_cliente()

def avancar():
    selected_venda = tv_cliente.focus()
    cliente_selecionado = tv_cliente.item(selected_venda, 'values')
    if selected_venda:       
        ask2 = messagebox.askquestion("Continuar?", "Deseja prosseguir para locação?")
        if ask2 == "yes":
            criar_tela_venda()
            print("Livro Selecionado: "+ selecionados[1])

def cadastrar_cliente():
    
    arquivo_cliente = open("cliente.txt","a")
    print(dic_cliente)

    if entry_cpf.get() in dic_cliente:
        continuar = messagebox.askquestion("Continuar?", "Cliente já possui cadastro, deseja prosseguir?")
        if continuar == "yes":
            tela_cliente.destroy()
            criar_tela_venda()
            
    
    elif entry_email.get() in lista_email:
        messagebox.showerror("Ops!", "E-mail já cadastrado")
        #Implementar usuário associado e este e-mail

    elif entry_numero.get() in lista_numeros:
        messagebox.showerror("Ops!", "Número já cadastrado")
        #Implementar usuário associado a este número

    elif entry_cpf.get() == "" or entry_nome.get() == "" or entry_email.get() == "" or entry_numero.get() == "" or sexo_cliente.get == "" or combo_dia.get() == "" or combo_mes.get() == "" or combo_ano.get() == "" or entry_estado.get() == "":
        messagebox.showerror("Ops!", "Para continuar preencha todos os campos obrigatórios.")

    else:
        dic_cliente[entry_cpf.get()] = [entry_cpf.get().lower(), entry_nome.get().lower(), entry_email.get().lower(), entry_numero.get().lower(), sexo_cliente.get().lower(),
                                        combo_dia.get().lower(), combo_mes.get().lower(), combo_ano.get().lower(), entry_estado.get().lower()]
        lista_email.append(entry_email.get().lower())
        lista_numeros.append(entry_numero.get().lower())
        dic_endereco[entry_endereco.get().lower()] = [entry_endereco.get().lower(), entry_num.get().lower()]

        arquivo_cliente.write(entry_cpf.get().lower()+",")
        arquivo_cliente.write(entry_nome.get().lower()+",")
        arquivo_cliente.write(entry_email.get().lower()+",")
        arquivo_cliente.write(entry_numero.get().lower()+",")
        arquivo_cliente.write(sexo_cliente.get().lower()+",")
        arquivo_cliente.write(combo_dia.get().lower()+",")
        arquivo_cliente.write(combo_mes.get().lower()+",")
        arquivo_cliente.write(combo_ano.get().lower()+",")
        arquivo_cliente.write(entry_estado.get().lower()+"\n")
        messagebox.showinfo("Sucesso", "Cliente registrado com sucesso")
        entry_cpf.delete(0, "end")
        entry_nome.delete(0, "end")
        entry_email.delete(0, "end")
        entry_numero.delete(0, "end")
        sexo_cliente.delete(0, "end")
        combo_dia.delete(0, "end")
        combo_mes.delete(0, "end")
        combo_ano.delete(0, "end")
        entry_endereco.delete(0, "end")
        entry_num.delete(0, "end")
        entry_estado.delete(0, "end")

        entry_cpf['state'] = DISABLED
        entry_nome['state'] = DISABLED
        entry_email['state'] = DISABLED
        entry_numero['state'] = DISABLED
        sexo_cliente['state'] = DISABLED
        combo_dia['state'] = DISABLED
        combo_mes['state'] = DISABLED
        combo_ano['state'] = DISABLED
        entry_endereco['state'] = DISABLED
        entry_num['state'] = DISABLED
        entry_estado['state'] = DISABLED
        botao_salvar['state'] = DISABLED
    arquivo_cliente.close()


def pesquisar_cliente():
    if entry_pesquisa.get() in dic_cliente:
        tv_cliente.insert("","end", values=(dic_cliente[entry_pesquisa.get()][1], dic_cliente[entry_pesquisa.get()][2], dic_cliente[entry_pesquisa.get()][3]))
        botao_avancar['state'] = NORMAL
    elif entry_pesquisa.get() == "":
        messagebox.showinfo("Ops!", "Para pesquisar preencha o campo CPF")

    else:
        ask_cliente = messagebox.askquestion("Ops!", "Cliente não encontrado, deseja adicionar?")
        if ask_cliente == "yes":
            entry_cpf['state'] = NORMAL
            entry_nome['state'] = NORMAL
            entry_email['state'] = NORMAL
            entry_numero['state'] = NORMAL
            sexo_cliente['state'] = NORMAL
            combo_dia['state'] = NORMAL
            combo_mes['state'] = NORMAL
            combo_ano['state'] = NORMAL
            entry_endereco['state'] = NORMAL
            entry_num['state'] = NORMAL
            entry_estado['state'] = NORMAL
            botao_salvar['state'] = NORMAL



def criar_tela_cliente():

    global entry_cpf
    global entry_nome
    global entry_email
    global entry_numero
    global sexo_cliente
    global combo_dia
    global combo_mes
    global combo_ano
    global entry_estado
    global entry_endereco
    global entry_num
    global tela_cliente
    global tv_cliente
    global entry_pesquisa
    global botao_salvar
    global botao_avancar
    
    tela_cliente = Toplevel()
    tela_cliente.geometry("480x480+641+0")
    tela_cliente.config(bg="#D3D3D3")
    tela_cliente.resizable(0, 0)

    titulo_tela_cli = Label(tela_cliente, text= "CADASTRAR CLIENTE", relief='groove')
    titulo_tela_cli.config(font='Arial 18 bold',fg='black', width=37, height=2, bg="white")
    titulo_tela_cli.place(x=-35, y=0)

    label_texto_cli = Label(tela_cliente)
    label_texto_cli.config(bg="#D3D3D3", fg="black", font='Arial 8', text='Todo os itens que possuem ( * ) são obrigatórios', width=50, height=1)
    label_texto_cli.place(x=170,y=440)

    main_label_cli = Label(tela_cliente, width=65, height=23, relief="groove")
    main_label_cli.place(x=10, y=65)

    #Entry e treeview para pesquisar e mostrar clientes
    entry_pesquisa = Entry(main_label_cli,width=30)
    entry_pesquisa.place(x=5, y=20, height=27)

    label_pesquisa = Label(main_label_cli, text="* Pesquisar Cliente(Digite o CPF)", font="Arial 8")
    label_pesquisa.place(x=5, y=0)

    tv_cliente = ttk.Treeview(main_label_cli)
    tv_cliente.config(columns=('Nome','Email','Número'),show='headings', selectmode=BROWSE, height=1)
    tv_cliente.column('Nome',minwidth=0, width=145)
    tv_cliente.column('Email',minwidth=0, width=191) 
    tv_cliente.column('Número',minwidth=0, width=100) 

    tv_cliente.heading('Nome', text='Nome')
    tv_cliente.heading('Email', text='Email')
    tv_cliente.heading('Número', text='Número')
    tv_cliente.place(x=5, y=55)

    style_tvc = ttk.Style()
    style_tvc.theme_use("clam")
    style_tvc.configure("TreeView")

    #Entry e Combobox para obter os dados do cliente
    entry_cpf = Entry(main_label_cli, width=30)
    entry_cpf['state'] = DISABLED
    entry_cpf.place(x=10, y=135)

    entry_nome = Entry(main_label_cli, width=30)
    entry_nome['state'] = DISABLED
    entry_nome.place(x=260, y=135)

    entry_email = Entry(main_label_cli, width=30)
    entry_email['state'] = DISABLED
    entry_email.place(x=10, y=195)

    entry_numero = Entry(main_label_cli, width=30)
    entry_numero['state'] = DISABLED
    entry_numero.place(x=260, y=195)

    selected_combo_sexo = StringVar()
    values_combo = ["Masculino","Feminino"]
    sexo_cliente = ttk.Combobox(main_label_cli, width=27, values=values_combo)
    sexo_cliente['state'] = DISABLED
    sexo_cliente.place(x= 10, y=255)

    selected_combo_dia = StringVar()
    values_dia = []
    for x in range(1,31):
        values_dia.append(x)

    combo_dia = ttk.Combobox(main_label_cli, width=3, values=values_dia)
    combo_dia['state'] = DISABLED
    combo_dia.place(x=260, y=255)

    selected_combo_mes = StringVar()
    values_mes = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
    combo_mes = ttk.Combobox(main_label_cli, width=9, values=values_mes)
    combo_mes['state'] = DISABLED
    combo_mes.place(x=308, y=255)

    selected_combo_ano = StringVar()
    values_ano = []
    for x in range(1900,2021):
        values_ano.append(x)
    combo_ano = ttk.Combobox(main_label_cli, width=5, values=values_ano)
    combo_ano['state'] = DISABLED
    combo_ano.place(x=390, y=255)

    entry_endereco = Entry(main_label_cli, width=50)
    entry_endereco['state'] = DISABLED
    entry_endereco.place(x=10, y=315)

    entry_num = Entry(main_label_cli, width=5)
    entry_num['state'] = DISABLED
    entry_num.place(x=330, y=315)

    selected_combo_estado = StringVar()
    values_estados = ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]
    entry_estado = ttk.Combobox(main_label_cli, width=5, values=values_estados)
    entry_estado['state'] = DISABLED
    entry_estado.place(x=390, y=315, height=20)

    label_cpf = Label(main_label_cli, text="* CPF").place(x=5,y=113)
    label_nome = Label(main_label_cli, text="* Nome").place(x=260, y=113)
    label_email = Label(main_label_cli, text="* E-mail").place(x=5, y=173)
    label_numero = Label(main_label_cli, text="* Celular").place(x=260, y=173)
    label_sexo = Label(main_label_cli, text="* Sexo").place(x=7, y=233)
    label_dma = Label(main_label_cli, text="* Data de Nascimento DD/MM/AAAA", font="Arial 8").place(x=258, y=233)
    label_endereco = Label(main_label_cli, text="Endereço").place(x=8, y=293)
    label_n = Label(main_label_cli, text="N°").place(x=328, y=293)
    label_uf = Label(main_label_cli, text="* UF").place(x=390, y=293)

    botao_pesquisar = Button(main_label_cli, text="BUSCAR",font="Arial 9 bold", command=pesquisar_cliente)
    botao_pesquisar.place(x=200, y=20)

    botao_avancar = Button(main_label_cli, text = "AVANÇAR", font="Arial 9 bold", command=avancar)
    botao_avancar['state'] = DISABLED
    botao_avancar.place(x=377, y=20)

    botao_limpar = Button(main_label_cli, text="LIMPAR", font="Arial 9", command=lambda:limpar(tv_cliente))
    botao_limpar.place(x=270, y=20)

    botao_salvar = Button(tela_cliente, text="SALVAR",font="Arial 9 bold" , width=22, command=cadastrar_cliente)
    botao_salvar['state'] = DISABLED
    botao_salvar.place(x=10, y=420)

    botao_voltar = Button(tela_cliente, text="VOLTAR", width=22, command=lambda:sair(tela_cliente))
    botao_voltar.place(x=10, y=450)


                                                                                                                                                                                                                                                                                                                                                                                                                                                          
#Função responsável por cadastrar o livro num dicionario e escrever as informações do mesmo no arquivo
def cadastrar():
    arquivo_livro = open('livros.txt','a')
    if id_livro.get() in dic_livros:
        messagebox.showinfo("Ops!","Livro já registrado.")
        sair(janela_cadastro)
    
    elif id_livro.get() == "" or nome_livro.get() == "" or ano_livro.get() == "" or qntd_livro.get() == "":
        messagebox.showerror("Ops!","Preencha todos os campos obrigatórios.")

    elif int(qntd_livro.get()) <= 0:
        messagebox.showerror("Ops!","A quantidade inserida deve ser maior que 0")

    elif autor_livro.get() == "":
        dic_livros[id_livro.get().lower()] = [nome_livro.get().lower(), ano_livro.get(), "desconhecido" , qntd_livro.get()]
        dic_titulo[nome_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido", qntd_livro.get()]
        dic_autor[autor_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido", qntd_livro.get()]
        lista_autor.append([id_livro.get(), nome_livro.get().lower(), ano_livro.get(), "desconhecido", qntd_livro.get()])
        arquivo_livro.write(id_livro.get().lower()+",")
        arquivo_livro.write(nome_livro.get().lower()+",")
        arquivo_livro.write(ano_livro.get().lower()+",")
        arquivo_livro.wirte(qntd_livro.get()+",")
        arquivo_livro.write("desconhecido"+"\n")
        messagebox.showinfo("Sucesso!","Livro adicionado com sucesso.")
        sair(janela_cadastro)
        arquivo_livro.close()

    else:
        dic_livros[id_livro.get().lower()] = [nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(), qntd_livro.get()]
        dic_titulo[nome_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(), qntd_livro.get()]
        dic_autor[autor_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(), qntd_livro.get()]
        lista_autor.append([id_livro.get(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(), qntd_livro.get()])
        arquivo_livro.write(id_livro.get().lower()+",")
        arquivo_livro.write(nome_livro.get().lower()+",")
        arquivo_livro.write(ano_livro.get().lower()+",")
        arquivo_livro.write(qntd_livro.get()+",")
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
    global qntd_livro

    janela_cadastro = Toplevel()
    janela_cadastro.geometry("480x480+641+0")
    janela_cadastro.config(bg="#D3D3D3")
    janela_cadastro.resizable(FALSE,FALSE)

    titulo_tela = Label(janela_cadastro, text= 'CADASTRAR LIVRO')
    titulo_tela.config(font='Arial 18 bold',fg='black', width=37, height=2, bg="white", relief='groove')
    titulo_tela.place(x=-30, y=0)

    main_label_cad = Label(janela_cadastro, width=65, height=23, relief="groove")
    main_label_cad.place(x=10, y=65)

    label_texto_pes = Label(main_label_cad)
    label_texto_pes.config(fg="black", font='Arial 7', text='Todo os itens que possuem ( * ) são obrigatórios', width=40, height=1)
    label_texto_pes.place(x=190,y=315)

    #Entradas do usuario que serão salvas no dicionário
    label_id = Label(main_label_cad, text='* ISBN', font="Arial 9", fg="black")
    label_id.place(x=0,y=0)
    id_livro = Entry(main_label_cad, width=30)
    id_livro.place(x=2, y=20)

    label_nome = Label(main_label_cad, text='* Nome',font="Arial 9", fg="black")
    label_nome.place(x=0,y=60)
    nome_livro = Entry(main_label_cad, width=30)
    nome_livro.place(x=2, y=80)

    label_ano = Label(main_label_cad ,text='* Ano',font="Arial 9", fg="black")
    label_ano.place(x=0,y=120)
    ano_livro = Entry(main_label_cad, width=30)
    ano_livro.place(x=2, y=140)

    label_autor = Label(main_label_cad,  text='Autor',font="Arial 9", fg="black")
    label_autor.place(x=0,y=180)
    autor_livro = Entry(main_label_cad, width=30)
    autor_livro.place(x=2, y=200)

    label_qntd = Label(main_label_cad, text="* Quantidade", font="Arial 9")
    label_qntd.place(x=0, y=240)
    qntd_livro = Entry(main_label_cad, width=12)
    qntd_livro.place(x=2, y=260)

    botao_cadastrar = Button(main_label_cad,text="CADASTRAR", width= 22, font='Arial 10 bold',command=cadastrar)
    botao_cadastrar.place(x=2, y=315)

    botao_fechar = Button(janela_cadastro, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(janela_cadastro))
    botao_fechar.place(x=15, y=420)
    

def criar_tela_venda():

    janela_venda = Toplevel()
    janela_venda.geometry("480x480+641+0")
    janela_venda.resizable(0, 0)  
    





































