import tkinter as tk

janela = tk.Tk()
janela.title("Minha aplicação")
janela.geometry ("400x300")

label = tk.Label(janela, text = "Olá, Mundo!")
label.pack(pady=20)

def ao_clicar():
    label.config(text="Botão Clicado!")


botao = tk.Button(janela, text ="Clique Aqui", command=ao_clicar)
botao.pack()

janela.mainloop()