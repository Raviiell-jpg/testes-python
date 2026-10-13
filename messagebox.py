import tkinter as tk
from tkinter import messagebox


app = tk.Tk()
app.title("Exemplo MessageBox")
app.geometry("250x100")

def mostrar_mensagem():
    messagebox.showinfo("Aviso", "Operação realizada com sucesos!")


def fechar_programa():
    messagebox.showwarning("Aviso", "Programa fechando")
    exit()



btn = tk.Button(text="Cçoqie aqio", command=mostrar_mensagem)
btn.pack(pady=10)
btn = tk.Button(text="Fechar programa", command=fechar_programa)
btn.pack(pady=10)

app.mainloop()