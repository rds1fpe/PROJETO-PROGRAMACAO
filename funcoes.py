from io import TextIOWrapper
from tkinter import*
from tkinter import ttk
from tkinter import font
from types import BuiltinFunctionType
from typing import ValuesView
from PIL import ImageTk, Image
from datetime import date, timedelta
from tkinter import messagebox


#dicionários e listas que serão manipulados durante a execução do programa
dic_livros = {}
dic_titulo = {}
dic_autor = {}
dic_cliente = {}
dic_endereco = {}
dic_locacao = {}
lista_autor = []
lista_cliente = []
lista_livros = []
lista_numeros = []
lista_email = []
lista_locados = []


#adicionando as informações do arquivo no dicionario
#arquivo de Livro, Cliente e Livro locados precisa iniciar com pelo menos 1 linha em cada arquivo(será corrigido até entrega final)
arquivo_livro = open("livros.txt","r")
arquivo_cliente = open("cliente.txt","r")
arquivo_locado = open("locados.txt","r")
for linha in arquivo_livro:
    linha = linha.strip()
    lista_livros.append(linha)
arquivo_livro.close()

#Transformando Arquivo de clientes em Lista para ser inserido no Dicionário
for linha in arquivo_cliente:
    linha = linha.strip()
    lista_cliente.append(linha)
arquivo_cliente.close()

#Transformando Arquivo de livros locados em Lista para ser inserido no Dicionário de Livros Locados
for linha in arquivo_locado:
    linha = linha.strip()
    lista_locados.append(linha)
arquivo_locado.close()

#CRIANDO OS 3 DICIONÁRIOS COM OS DADOS DO ARQUIVO
auxiliar = 0
for livro in lista_livros:
    #criando uma lista separando cada item por virgula(Linha separada por virgula no arquivo)
    lista_separada = (lista_livros[auxiliar].split(","))
    #print(lista_separada)
    #lista onde cada item é uma informação do livro
    info_id = [lista_separada[1].lower(), lista_separada[2].lower(), lista_separada[3].lower(), lista_separada[4]]
    info_titulo_autor = [lista_separada[0].lower(),lista_separada[1].lower(), lista_separada[2], lista_separada[3].lower(), lista_separada[4]] 
    dic_livros[lista_separada[0].lower()] = info_id
    dic_titulo[lista_separada[1].lower()] = info_titulo_autor
    dic_autor [lista_separada[3].lower()] = info_titulo_autor
    lista_autor.append(info_titulo_autor)
    auxiliar += 1
#print(dic_livros)
#print(dic_autor)
print(dic_titulo)
#print(lista_autor)

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


auxiliar_locado = 0
for locado in lista_locados:
    lista_sep_loc = lista_locados[auxiliar_locado].split(",")
    info_locado = [lista_sep_loc[0], lista_sep_loc[1], lista_sep_loc[2]] #Nome do cliente, Livro, e Data de devolução
    dic_locacao[lista_sep_loc[0]] = info_locado
    auxiliar_locado += 1

######################################################################################################################
#FUNÇÕES QUE SÃO USADAS EM MAIS DE UMA TELA
#botão para fechar a tela
def sair(tela):
    tela.destroy()

#Limpa a pesquisa
def limpar(tv):
    for item in tv.get_children():
        tv.delete(item)

#################################################################################################################

#mostra todos os livros cadastrados na tela de pesquisa
def mostrar_tudo():
    limpar(tv)
    for item in dic_livros:
        tv.insert("","end", values=(item,
        dic_livros[item][0],
        dic_livros[item][1],
        dic_livros[item][2],
        dic_livros[item][3]))

#FUNÇÃO DE PESQUISA DE LIVROS
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
            dic_livros[entrada_pesquisa.get().lower()][3]))#inserindo o status na grade
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
            dic_titulo[entrada_pesquisa.get().lower()][4]))#insetindo o status na grade
        else:
            messagebox.showerror("Ops!","Livro não encontrado!")

    elif radioValue.get() == 3:

        aux_autor = 0
        if entrada_pesquisa.get() == "":
            messagebox.showerror("Ops!", "Digite o Autor que deseja pesquisar")

        elif entrada_pesquisa.get().lower() not in dic_autor:
            messagebox.showerror("Ops!","Livro não encontrado!")
        else:
            for autor in lista_autor: #Retorna todos os livros que possuem os mesmos autores
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
    tv.column('ISBN',minwidth=0, width=40)
    tv.column('Título',minwidth=0, width=130) 
    tv.column('Ano',minwidth=0, width=55) 
    tv.column('Autor',minwidth=0, width=156)
    tv.column('Qntd', minwidth=0, width=45) 

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

########################################################################################################################################
#FUNÇÃO QUE PEGA OS ITENS SELECIONADOS NA PESQUISA DE LIVROS E ABRE A TELA DE CADASTRO DE CLIENTE PARA PROSSEGUIR COM A LOCAÇÃO DO MESMO
def selecionar():
    global selecionados

    selected = tv.focus() # Pegar as informações do livro selecionado na TreeView
    selecionados = tv.item(selected, 'values') # Tupla com as informações dos livros
    print(selecionados)
    if selected:
        if selecionados[4] == "N/D":
                messagebox.showerror("Ops!","Este Livro não está disponível")
        else:
            ask = messagebox.askquestion("Continuar?","Livro selecionado, deseja abrir tela de cadastro de cliente?")
            if ask == "yes":
                sair(tela_pesquisa)
                criar_tela_cliente()

#FUNÇÃO QUE PEGA O ÚSUARIO CADASTRADO OU SELECIONADO E ABRE A TELA DE LOCAÇÃO
def avancar():

    selected_venda = tv_cliente.focus() #Pegar as informações dos clientes selecionados na TreeView
    cliente_selecionado = tv_cliente.item(selected_venda, 'values') #Tupla com as informações dos clientes
    if selected_venda:       
        ask2 = messagebox.askquestion("Continuar?", "Deseja prosseguir para locação?")
        if ask2 == "yes": 
            if cliente_selecionado[0] in dic_locacao: # Se o cliente já locou um livro a tela de locação mostra o cliente e o livro locado
                messagebox.showinfo("Ops!","Esse Cliente já possui locações pendentes")
                sair(tela_cliente)
                criar_tela_venda()
                nome = cliente_selecionado[0]
                titulo = dic_locacao[nome][1]
                data_dev = int(dic_locacao[nome][2]) # Transforma o item selecionado no Combobox em inteiro para somar na data(semanas)
                data_atual = date.today()
                devolucao = data_atual + timedelta(weeks = data_dev)
                tv_locar.insert("","end", values=(nome, titulo, devolucao))
            else:
                try:
                    if selecionados and cliente_selecionado:
                        criar_tela_venda()
                        sair(tela_cliente)
                        botao_selecionado['state'] = NORMAL
                        tv_locar_info.insert("","end", values=(cliente_selecionado[0],selecionados[1]))
                except:
                    ask3 =  messagebox.askquestion("Ops!","Antes de prosseguir é necessário selecionar um livro na tela de pesquisa\nDeseja abrir tela de pesquisa?")
                    if ask3 == "yes":
                        sair(tela_cliente)
                        criar_tela_pesquisa()


##########################################################################################################
#FUNÇÃO RESPONSÁVEL POR CADASTRAR OS CLIENTES E ESCREVER AS  INFORMAÇÕES NO ARQUIVO
def cadastrar_cliente():
    
    arquivo_cliente = open("cliente.txt","a")

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
        #Limpando todos os entrys
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
        
        #Desabilitando os Entrys
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

################################################################################################################################################################
#FUNÇÃO PARA PESQUISAR CLIENTES
def pesquisar_cliente():
    limpar(tv_cliente)
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


#CRIAÇÃO DA TELA DE CADASTRO E BUSCA DE CLIENTES
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


####################################################################################################################                                                                                                                                                                                                                                                                                                                                                                                                                                                          
#Função responsável por cadastrar o livro num dicionario e escrever as informações do mesmo no arquivo
def cadastrar():
    arquivo_livro = open('livros.txt','a')
    if id_livro.get() in dic_livros:
        messagebox.showinfo("Ops!","Livro já registrado.")
        sair(janela_cadastro)
    
    elif id_livro.get() == "" or nome_livro.get() == "" or ano_livro.get() == "":
        messagebox.showerror("Ops!","Preencha todos os campos obrigatórios.")

    elif autor_livro.get() == "":
        dic_livros[id_livro.get().lower()] = [nome_livro.get().lower(), ano_livro.get(), "desconhecido","D"]
        dic_titulo[nome_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido","D"]
        dic_autor[autor_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), "desconhecido","D"]
        lista_autor.append([id_livro.get(), nome_livro.get().lower(), ano_livro.get(), "desconhecido","D"])
        arquivo_livro.write(id_livro.get().lower()+",")
        arquivo_livro.write(nome_livro.get().lower()+",")
        arquivo_livro.write(ano_livro.get().lower()+",")
        arquivo_livro.write("desconhecido" +",")
        arquivo_livro.write("D"+"\n") # inserir o status do livro (sempre começa com disponivel ""D)
        
        messagebox.showinfo("Sucesso!","Livro adicionado com sucesso.")
        sair(janela_cadastro)
        arquivo_livro.close()

    else:
        dic_livros[id_livro.get().lower()] = [nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(),"D"]
        dic_titulo[nome_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(),"D"]
        dic_autor[autor_livro.get().lower()] = [id_livro.get().lower(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(),"D"]
        lista_autor.append([id_livro.get(), nome_livro.get().lower(), ano_livro.get(), autor_livro.get().lower(),"D"])
        arquivo_livro.write(id_livro.get().lower()+",")
        arquivo_livro.write(nome_livro.get().lower()+",")
        arquivo_livro.write(ano_livro.get().lower()+",")
        arquivo_livro.write(autor_livro.get().lower()+",")
        arquivo_livro.write("D"+"\n")
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

    botao_cadastrar = Button(main_label_cad,text="CADASTRAR", width= 22, font='Arial 10 bold',command=cadastrar)
    botao_cadastrar.place(x=2, y=315)

    botao_fechar = Button(janela_cadastro, text="VOLTAR", width=25, fg="#042c44", command=lambda:sair(janela_cadastro))
    botao_fechar.place(x=15, y=420)

#########################################################################################################################    
#MOSTRAR NA TREE VIEW OS LIVROS QUE FORAM LOCADOS
def mostrar_locados():
    limpar(tv_locar)
    
    for locado in dic_locacao:
        nome = dic_locacao[locado][0]
        titulo = dic_locacao[locado][1]
        data_dev = int(dic_locacao[locado][2])
        data_atual = date.today()
        devolucao = data_atual + timedelta(weeks= data_dev)
        tv_locar.insert("","end", values=(nome, titulo, devolucao))
    
        
#FUNÇÃO PARA DESBLOQUEAR A ESCOLHA DA QUANTIDADE DE TEMPO DA LOCAÇÃO
def select_locacao():
    combo_periodo['state'] = NORMAL
    botao_locar['state'] = NORMAL
    
#ABRE O ARQUIVO DE LOCADOS E ESCREVE AS INFORMAÇÕES DO CLIENTE E DO LIVRO LOCADO
def finalizar():

    arquivo_locado = open("locados.txt", "a")
    cliente_livro = tv_locar_info.focus() 
    cliente_livro_select = tv_locar_info.item(cliente_livro, 'values') #Lista dos valores selecionados da TreeView
    nome = cliente_livro_select[0]
    titulo = cliente_livro_select[1]
  
    ask_finalizar = messagebox.askquestion("Finalizar?","Deseja finalizar a locação?")
    if ask_finalizar == "yes":
        #Escreve no arquivo as informações da locação(Cliente, livro e data de devolução)
        dic_locacao[nome] = [nome, titulo, combo_periodo.get()]
        arquivo_locado.write(nome + ",")
        arquivo_locado.write(titulo + ",")
        arquivo_locado.write(combo_periodo.get() + "\n")
        arquivo_locado.close()

        combo_periodo['state'] = DISABLED
        botao_locar['state'] = DISABLED
        botao_selecionado['state'] = DISABLED
        
        # Muda a informação (disponível) no arquivo de livros
        #Foi necessário pegar essas informações do dicionário de Titulos porque...
        #A úinica chave disponível para pesquisa era "titulo"
        #Obtendo as Strings para concatenar e remover a linha do arquivo
        isbn = dic_titulo[titulo][0]
        titulo_l = dic_titulo[titulo][1]
        ano = dic_titulo[titulo][2]
        autor = dic_titulo[titulo][3]
        qntd = int(dic_livros[isbn][3])
        new_qntd = qntd - 1

        #Linha que será deletada do arquivo de livros
        string_del = isbn + "," + titulo_l + "," + ano + "," + autor + "," + str(qntd)
        
        #Se a quantidade for igual a 0, o valor (N/D) é inserido no arquivo
        if new_qntd == 0:
            new_string = isbn + "," + titulo_l + "," + ano + "," + autor + "," + "N/D"
            dic_livros[isbn][3] = "N/D" # muda a quantidade no dicionário para n/d para não ser necessário reabrir o arquivo
            with open("livros.txt", "r") as editar_arquivo: # abrindo o arquivo no modo de leitura
                lista_linhas = editar_arquivo.readlines() # criando uma lista de linhas
            with open("livros.txt", "w") as editar_arquivo:
                for linha in lista_linhas:
                    if linha.strip("\n") != string_del: # se a linha for diferente da string que vai ser removida, ele escreve essa linha no arquivo
                        editar_arquivo.write(linha)
                editar_arquivo.write(new_string+"\n")

        #Se a quantidade for maio que 0, apenas subtrai 1 da quantidade e escreve essa informação no arquivo
        elif new_qntd > 0:
            new_string = isbn + "," + titulo_l + "," + ano + "," + autor + "," + str(new_qntd) # nova linha que será colocada no arquivo de livros
            dic_livros[isbn][3] = new_qntd #Muda a informação no dicionário para n ser necessário reabrir o programa e ler o arquivo novamente
            with open("livros.txt", "r") as editar_arquivo: # abrindo o arquivo no modo de leitura
                lista_linhas = editar_arquivo.readlines() # criando uma lista de linhas
            with open("livros.txt", "w") as editar_arquivo:
                for linha in lista_linhas:
                    if linha.strip("\n") != string_del:
                        editar_arquivo.write(linha)
                editar_arquivo.write(new_string+"\n")
        
    

#CRIÇÃO DA TELA DE VENDA/LOCAÇÃO
def criar_tela_venda():
    global tv_locar_info
    global tv_locar
    global combo_periodo
    global botao_selecionado
    global botao_locar
    global data

    janela_venda = Toplevel()
    janela_venda.geometry("480x480+641+0")
    janela_venda.resizable(0, 0)  
    
    titulo_tela_venda = Label(janela_venda, text= 'LOCAR LIVRO')
    titulo_tela_venda.config(font='Arial 18 bold',fg='black', width=37, height=2, bg="white", relief='groove')
    titulo_tela_venda.place(x=-30, y=0)

    main_label_venda = Label(janela_venda, width=65, height=25, relief="groove")
    main_label_venda.place(x=10, y=65)

    label_tv = Label(main_label_venda, text="Consultar locações feitas", font="Arial 8 bold")
    label_tv.place(x=5, y=5)

    tv_locar = ttk.Treeview(main_label_venda)
    tv_locar.config(columns=('Cliente','Livro','Devolução'),show='headings', selectmode=BROWSE, height=1)
    tv_locar.column('Cliente',minwidth=0, width=145)
    tv_locar.column('Livro',minwidth=0, width=191) 
    tv_locar.column('Devolução',minwidth=0, width=100) 

    tv_locar.heading('Cliente', text='Cliente')
    tv_locar.heading('Livro', text='Livro')
    tv_locar.heading('Devolução', text='Devolução')
    tv_locar.place(x=5, y=30, height=160)

    style_tvv = ttk.Style()
    style_tvv.theme_use("clam")
    style_tvv.configure("TreeView")

    botao_mostrar_loc = Button(main_label_venda, text="Vizualizar Locações", font="Arial 8", width=16, command=mostrar_locados)
    botao_mostrar_loc.place(x=339, y=2)

    label_info = Label(main_label_venda, text="Dados do Cliente/Livro", font="Arial 8 bold")
    label_info.place(x=5, y=195)

    tv_locar_info = ttk.Treeview(main_label_venda)
    tv_locar_info.config(columns=("Cliente", "Livro"), show="headings")
    tv_locar_info.column("Cliente", minwidth=0, width=120)
    tv_locar_info.column("Livro", minwidth=0, width=120)

    tv_locar_info.heading("Cliente", text="Cliente")
    tv_locar_info.heading("Livro", text="Livro")
    tv_locar_info.place(x=5, y=220, height=100)

    botao_selecionado = Button(main_label_venda, text="Selecionar", font="Arial 9", width=16, command=select_locacao)
    botao_selecionado['state'] = DISABLED
    botao_selecionado.place(x=127, y=320)

    botao_locar = Button(main_label_venda, text="Finalizar", font="Arial 9", width=16, height=2, command=finalizar)
    botao_locar['state'] = DISABLED
    botao_locar.place(x=321 , y=320)

    label_info_data = Label(main_label_venda, text="Selecione o Período da locação)", font="Arial 8 bold")
    label_info_data.place(x=265,  y=195) 

    label_select = Label(main_label_venda, width=25, height=6, relief="groove", borderwidth=3)
    label_select.place(x=262, y=220) 

    data = date.today()
    label_info_atual = Label(label_select, text="Data Atual", font="Arial 8")
    label_info_atual.place(x=0,  y=0)

    label_data_atual = Label(label_select, text=data, width=8, fg="black")
    label_data_atual.place(x=0, y=30)

    label_info_dev = Label(label_select, text="Período de locação\n (semanas)", font="Arial 8")
    label_info_dev.place(x=77,  y=0)

    lista_periodo = ["1","2","3","4","5","6"]
    combo_periodo = ttk.Combobox(label_select , width=13, values=lista_periodo)
    combo_periodo['state'] = DISABLED
    combo_periodo.place(x=77, y=33)

    botao_voltar_loc = Button(janela_venda, text="VOLTAR", width=22, command=lambda:sair(janela_venda))
    botao_voltar_loc.place(x=10, y=450)






































