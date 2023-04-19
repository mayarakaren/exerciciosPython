from tkinter import *
tela = Tk()
tela.title("Teste de Radio Button")

Label(tela, text="Escolha uma das cidades do Vale do ribeira", padx=20).pack()

Cidades = [
    ("Juquiá", "Juquiá"),
    ("Registro", "Registro"),
    ("Pariquera-Açu", "Pariquera-Açu"),
    ("Cajati", "Cajati"),
    ("Jacupiranga", "jacupiranga"),
]

localPizza = StringVar()
localPizza.set("Cajati")

for text, valor in Cidades:
    Radiobutton(tela, text=text, variable=localPizza, value=valor).pack(anchor=W)

def choseRadio(value):
    lbl_cidade = Label(tela, text=value)
    lbl_cidade.pack()

btn_botao = Button(tela, text="Escolha uma das cidades", command=lambda: choseRadio(localPizza.get()))
btn_botao.pack()
tela.mainloop()