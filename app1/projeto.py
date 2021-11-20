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
path_busca = f"PROJETO-PROGRAMACAO/app1/images/lupa.png"
path_reset = f"PROJETO-PROGRAMACAO/app1/images/reset.png"


#definindo o menu inicial
tela_inicial = Tk()

#definindo titulo e geometria da tela inicial
tela_inicial.title("Biblioteca")
tela_inicial.geometry("624x626+0+0")
tela_inicial.resizable(False, False)



#definindo imagem de fundo da tela inicial
img_tela1 = ImageTk.PhotoImage(Image.open(path))
label_tela1 = Label(tela_inicial, image = img_tela1).place(x=0,y=33)

#Label principal
img_mlabel = ImageTk.PhotoImage(Image.open(path))
main_label = Label(tela_inicial, image=img_mlabel)
main_label.place(x=0, y=33)


#Imagens/Capas dos livros
img_capa1 = ImageTk.PhotoImage(Image.open(path_capa))
botao_capa1 = Button(main_label, image = img_capa1)
botao_capa1.place(x=20,y=54)

img_capa2 = ImageTk.PhotoImage(Image.open(path_capa2))
botao_capa2 = Button(main_label, image = img_capa2)
botao_capa2.place(x=150,y=54)

img_capa3 = ImageTk.PhotoImage(Image.open(path_capa3))
botao_capa3 = Button(main_label, image = img_capa3).place(x=280,y=54)

img_capa4 = ImageTk.PhotoImage(Image.open(path_capa4))
botao_capa4 = Button(main_label, image = img_capa4).place(x=410,y=54)

img_capa5 = ImageTk.PhotoImage(Image.open(path_capa5))
botao_capa5 = Button(main_label, image = img_capa5).place(x=20,y=192)

img_capa6 = ImageTk.PhotoImage(Image.open(path_capa6))
botao_capa6 = Button(main_label, image = img_capa6).place(x=150,y=192)

img_capa7 = ImageTk.PhotoImage(Image.open(path_capa7))
botao_capa7 = Button(main_label, image = img_capa7).place(x=280,y=192)

img_capa8 = ImageTk.PhotoImage(Image.open(path_capa8))
botao_capa8 = Button(main_label, image = img_capa8).place(x=410,y=192)

#filtro para busca
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

check1 = Checkbutton(tela_inicial, text='Título', variable=var1, onvalue=1, offvalue=0)
check1.place(x=20, y=0)
check2 = Checkbutton(tela_inicial, text='Genêro',variable=var2, onvalue=1, offvalue=0)
check2.place(x=90, y=0)
check3 = Checkbutton(tela_inicial, text='Autor',variable=var3, onvalue=1, offvalue=0)
check3.place(x=160, y=0)

#ComboBox para filtrar o conteudo selecionado no CheckBox
valores = ["Valores serão inseridos aqui..."]
filtro = ttk.Combobox(tela_inicial, values=valores, width=30, height=90).place(x=240, y=0)

#BOTAO
#Quando se passa argumentos numa função que será realizada por um botão, é necessario usar o lambda.
image_lupa = ImageTk.PhotoImage(Image.open(path_busca))
button_lupa = Button(tela_inicial, image=image_lupa, border="0", command=lambda: main_label.place(relx=0.0, rely=0.1))
button_lupa.place(x=445, y=0)

image_reset = ImageTk.PhotoImage(Image.open(path_reset))
button_reset = Button(tela_inicial, image=image_reset, border="0",command=lambda: main_label.place_forget())
button_reset.place(x=470, y=0)

#mainloop executa o loop que permite a janela permanecer aberta
tela_inicial.mainloop()

