import tkinter as tk
from pathlib import Path


app = tk.Tk()
app.title("Minha primeira tela")
app.geometry("500x500")
app.configure(bg="Black")

label = tk.Label(text="Blablabla", fg="blue", font=("Comic Sans MS", 20))
label.pack(pady=10)

def mostrar_conteudo():
    caminho = Path(__file__).with_name("ada.txt")
    try:
        print(caminho.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print("Arquivo não encontrado.")


def abrir_conteudo():
    try:
        with open("ada.txt", "r", encoding="utf-8") as ada:
            conteudo = ada.read()
            print (conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado")


btn = tk.Button(text="Clique Aqui", font=("Comic Sans MS",20), command=abrir_conteudo)
btn.pack(pady=10)



app.mainloop()