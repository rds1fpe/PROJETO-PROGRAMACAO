from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox


caminho = "PROJETO-PROGRAMACAO/app1/images/"


tela_inicial =Tk()
tela_inicial.geometry ("640x480+300+100")

#imagem de fundo
img_bg = ImageTk.PhotoImage(Image.open(caminho+"bg.jpg"))
label_tela = Label(tela_inicial, image = img_bg).place(x=0,y=0)

#logo
logo = ImageTk.PhotoImage(Image.open(caminho+"logo.png"))
label_logo = Label(tela_inicial, image = logo, borderwidth=0).place(x=223,y=10)

#Label para Matricula e Senha
label_ms = Label(tela_inicial, background='#04344c', width=30, height=10, borderwidth=2, relief='ridge')
label_ms.place(x=215, y=170)

#Label tela de Login
label_user = Label(tela_inicial, text="MATRÍCULA",foreground='white',  font=('Helvetica',11, 'bold'), bg='#04344c')
label_user.place(x=230, y=180)

label_passw = Label(tela_inicial, text="SENHA",foreground='white',  font=('Helvetica', 11, 'bold'), bg='#04344c',)
label_passw.place(x=230, y=240)

#Entry da tela de Login
user_entry = Entry(tela_inicial, width=30)
user_entry.place(x=230, y=205)

user_passw = Entry(tela_inicial, width=30)
user_passw.config(show='*')
user_passw.place(x=230, y=265)

#Botão de Login
Login_button = Button(tela_inicial, text= "Login", font=('Helvetica', 8, 'bold') , width=20)
Login_button.place(x=230, y=295)


#mainloop executa o loop que permite a janela permanecer aberta
tela_inicial.mainloop()


