from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

#caminho imagem de fundo da tela principal
path = "PROJETO-PROGRAMACAO/app1/images/bg1.jpg"

#caminho para capa teste
path_capa  = f"PROJETO-PROGRAMACAO/app1/images/capa2.jpg"
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


#entrada de busca de livro por nome.
entrada_busca = Entry(tela_inicial, width=30)
entrada_busca.place(height=26,x=72, y=0)

# função que será usada no botão
def Procurar():
    print("O livro que você procurou foi: " , entrada_busca.get())

#Imagens/Capas dos livros
img_capa1 = ImageTk.PhotoImage(Image.open(path_capa))
botao_capa1 =Button(tela_inicial, image = img_capa1).place(x=20,y=85)

img_capa2 = ImageTk.PhotoImage(Image.open(path_capa2))
botao_capa2 = Button(tela_inicial, image = img_capa2).place(x=150,y=85)

img_capa3 = ImageTk.PhotoImage(Image.open(path_capa3))
botao_capa3 = Button(tela_inicial, image = img_capa3).place(x=280,y=85)

img_capa4 = ImageTk.PhotoImage(Image.open(path_capa4))
botao_capa4 = Button(tela_inicial, image = img_capa4).place(x=410,y=85)

img_capa5 = ImageTk.PhotoImage(Image.open(path_capa5))
botao_capa5 = Button(tela_inicial, image = img_capa5).place(x=20,y=223)

img_capa6 = ImageTk.PhotoImage(Image.open(path_capa6))
botao_capa6 = Button(tela_inicial, image = img_capa6).place(x=150,y=223)

img_capa7 = ImageTk.PhotoImage(Image.open(path_capa7))
botao_capa7 = Button(tela_inicial, image = img_capa7).place(x=280,y=223)

img_capa8 = ImageTk.PhotoImage(Image.open(path_capa8))
botao_capa8 = Button(tela_inicial, image = img_capa8).place(x=410,y=223)


#BOTAO
#Quando se passa argumentos numa função que será realizada por um botão, é necessario usar o lambda.
cmd = Button(tela_inicial, text = "Procurar", command= Procurar).place(x=0, y=0)
cmd = Button(tela_inicial, text = "Filtrar").place(x=300, y=0)


#filtro para busca
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

check1 = Checkbutton(tela_inicial, text='Autor', variable=var1, onvalue=1, offvalue=0)
check1.place(x=350, y=0)
check2 = Checkbutton(tela_inicial, text='Genêro',variable=var2, onvalue=1, offvalue=0)
check2.place(x=400, y=0)
check3 = Checkbutton(tela_inicial, text='Ano',variable=var3, onvalue=1, offvalue=0)
check3.place(x=460, y=0)


#mainloop executa o loop que permite a janela permanecer aberta
tela_inicial.mainloop()

