from tkinter import*
from tkinter import ttk

tk= Tk()

v = IntVar(tk)

c = Radiobutton(tk, text= 'OK', variable=v, value=1)
c.pack()

c2 = Radiobutton(tk, text = "meu pau", variable= v, value = 2)
c2.pack()

def mostrar():
    if v.get() == 1:
        print('gay')
    elif v.get() == 2:
        print('jesus')


b = Button(tk, text="teste", command=mostrar)
b.pack()

tk.mainloop()