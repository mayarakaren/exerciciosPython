from tkinter import *

tela = Tk()

tela.title("Acesso ao sistema")
tela.geometry("400x200")
tela.resizable(True, True)

largura = 400
altura = 200

lbl_usuario = Label(tela, text="Usuário").place (x=50, y=60)
lbl_senha = Label(tela, text="Senha").place(x=50, y=100)
txt_senha = Entry(tela, width=20).place(x=200, y=60)
txt_usuario = Entry(tela, width=20).place(x=100, y=60)
foto_acesso = PhotoImage(file = r"img/entrar.png")
foto_sair = PhotoImage(file = r"img/sair.png")
btn_usuario = Button(tela, text="Acessar", image= foto_acesso, compound= TOP).place(x=250, y=50)
btn_senha = Button(tela, text="Sair", image= foto_sair, compound = TOP).place(x=320, y=50)

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx= largura_screen/2 - largura/2
posy= altura_screen/2 - altura/2

print(largura_screen, altura_screen)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()