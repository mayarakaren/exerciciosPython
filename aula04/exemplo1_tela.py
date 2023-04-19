#Importar biblioteca

from tkinter import *

#Criar variavel (tela)
tela = Tk()

#Titulo na barra de tarefas
tela.title("Oberon")

#Configuração da cor da tela
tela.configure(background="#876ABD")

#Configuração tamanho da tela
tela.geometry("700x600")

#Configuração do tamanho máximo da tela
tela.resizable(True, True)

#Tamanho máximo que a tela pode chegar
tela.maxsize(width= 900, height= 800)

#Tamanho mínimo que a tela pode chegar
tela.minsize(width= 500, height= 400)

#Adicionar label
lbl_teste= Label(tela, text="TESTE").place(x=10, y=10)

#lbl_teste (nome) 
#label é o tipo de componente
#Tela a váriavel que a label está ligada
#tetxt="" e o texto a ser exibido na tela
#place posicionamento na tela

lbl_nome = Label(tela, text="Nome", font= "Arial 20 bold italic", fg="#FFC800").place(x=10, y=10)
lbl_cpf = Label(tela, text="CPF", font= "times 15 italic", fg="#7CFC00").place(x=10, y=50)

tela.mainloop()