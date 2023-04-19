from tkinter import *

tela = Tk()
tela.title("Oberon")

#Dimensões da janela

largura = 800
altura= 300

#Resolução do sistema(Sistema Operacional)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#Visualização do tamanho da tela no terminal
print(largura_screen, altura_screen)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()