from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image

#caminho imagem de fundo da tela principal
path = "PROJETO-PROGRAMACAO/app1/images/bg1.jpg"

#caminho para capa teste
path_capa = f"PROJETO-PROGRAMACAO/app1/images/capa2.jpg"
path_capa2 = f"PROJETO-PROGRAMACAO/app1/images/capa3.jpg"
path_capa3 = f"PROJETO-PROGRAMACAO/app1/images/capa4.jpg"
path_capa4 = f"PROJETO-PROGRAMACAO/app1/images/capa5.jpg"
path_capa5 = f"PROJETO-PROGRAMACAO/app1/images/capa6.png"
path_capa6 = f"PROJETO-PROGRAMACAO/app1/images/capa7.jpg"
path_capa7 = f"PROJETO-PROGRAMACAO/app1/images/capa8.png"
path_capa8 = f"PROJETO-PROGRAMACAO/app1/images/capa9.jpg"


#definindo o menu inicial
tela_inicial = Tk()

#definindo titulo e geometria da tela inicial
tela_inicial.title("Biblioteca")
tela_inicial.geometry("624x626+0+0")
tela_inicial.resizable(False, False)

#definindo imagem de fundo da tela inicial
img_tela1 = ImageTk.PhotoImage(Image.open(path))
label_tela1 = Label(tela_inicial, image = img_tela1).place(x=0,y=33)

#Imagens/Capas dos livros
img_capa1 = ImageTk.PhotoImage(Image.open(path_capa))
label_capa1 = Label(tela_inicial, image = img_capa1).place(x=20,y=85)

img_capa2 = ImageTk.PhotoImage(Image.open(path_capa2))
label_capa2 = Label(tela_inicial, image = img_capa2).place(x=130,y=85)

img_capa3 = ImageTk.PhotoImage(Image.open(path_capa3))
label_capa3 = Label(tela_inicial, image = img_capa3).place(x=240,y=85)

img_capa4 = ImageTk.PhotoImage(Image.open(path_capa4))
label_capa4 = Label(tela_inicial, image = img_capa4).place(x=350,y=85)

img_capa5 = ImageTk.PhotoImage(Image.open(path_capa5))
label_capa5 = Label(tela_inicial, image = img_capa5).place(x=20,y=223)

img_capa6 = ImageTk.PhotoImage(Image.open(path_capa6))
label_capa6 = Label(tela_inicial, image = img_capa6).place(x=130,y=223)

img_capa7 = ImageTk.PhotoImage(Image.open(path_capa7))
label_capa7 = Label(tela_inicial, image = img_capa7).place(x=240,y=223)

img_capa8 = ImageTk.PhotoImage(Image.open(path_capa8))
label_capa8 = Label(tela_inicial, image = img_capa8).place(x=350,y=223)


# função que será usada no botão
def cmd_Click(mensagem):
    print(mensagem)


#BOTAO
#Quando se passa argumentos numa função que será realizada por um botão, é necessario usar o lambda.
cmd = Button(tela_inicial, text = "Procurar", command=lambda: cmd_Click("Nova mensagem")).place(x=0, y=0)
cmd = Button(tela_inicial, text = "Filtrar", command=lambda: cmd_Click("Nova mensagem")).place(x=300, y=0)

#entrada de busca de livro por nome.
entrada_busca = Entry(tela_inicial, width=30).place(x=70, y=0, height=26)

#filtro para busca
lista_filtro = ["Gênero", "Autor", "Ano"]
cb_filtro = ttk.Combobox(tela_inicial, values=lista_filtro, width=30).place(x=350,y=0, height=26)









#mainloop executa o loop que permite a janela permanecer aberta
tela_inicial.mainloop()

