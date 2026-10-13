import tkinter as tk
def mudar_texto(event):
    label.config(text="Mensagem alteraeda!")


janela = tk.Tk()
janela.title("Evento Enter")
janela.geometry("350x180")
janela.configure(bg="pink")


label = tk.Label(janela, text="Presione Enter para mudar", font="Arial 12")
label.pack(pady=50)

janela.bind("<Return>", mudar_texto)
janela.mainloop()