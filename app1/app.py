#O objeto em si, é constituido fundamentalmente por metodos e eventos e um conjunto de atributos
#Atributos são caracteristicas ou as qualidades que definem cada objeto(cor,largura,titulo,tamanho,altura,icone e etc...)
#podemos alterar os atributos através do metodos e eventos
#metodos são disparados pelo utilizador (click num botão, por exemplo)
#eventos são os resultados das ações dos metodos ou pela nossas alterações.
#Mainloop é responsavel por fazer o sistema não fechar (rodar em loop)

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

menu_inicial = Tk()
menu_inicial.title("My Biblioteca")

menu_inicial.geometry("624x755+0+0")
# resizable recebe True(1) ou False(0) e define se posso ou não redimencionar a janela qnd estiver aberta
menu_inicial.resizable(True, True)
menu_inicial.minsize(600, 450)
# iconbitmap para trocar o icone da janela, basta apenas colocar o caminho
#menu_inicial.iconbitmap("images/icon.ico")

# função que será usada no botão
def cmd_Click(mensagem):
    print(mensagem)




#BOTAO
#Quando se passa argumentos numa função que será realizada por um botão, é necessario usar o lambda.
cmd = Button(menu_inicial, text = "Procurar", command=lambda: cmd_Click("Nova mensagem")).place(x=0, y=0)
cmd = Button(menu_inicial, text = "Filtrar", command=lambda: cmd_Click("Nova mensagem")).place(x=300, y=0)


#entrada de busca de livro por nome.
entrada_busca = Entry(menu_inicial, width=30).place(x=70, y=0, height=26)

#filtro para busca
lista_filtro = ["Gênero", "Autor", "Ano"]
cb_filtro = ttk.Combobox(menu_inicial, values=lista_filtro, width=30).place(x=350,y=0, height=26)

#definindo caminho e colocando a imagem dentro um Label
path = "images/bg1.jpg"
img = ImageTk.PhotoImage(Image.open(path))
label1 = Label(menu_inicial, image = img).place(x=0,y=33)


menu_inicial.mainloop()
# metodos que atraves dos quais podemos configurar dados da nossa janela
