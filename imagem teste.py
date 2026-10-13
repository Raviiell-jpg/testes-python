import tkinter as tk
from PIL import ImageTk, Image

app = tk.Tk()
app.title("Imagem")
app.geometry("400x400")
app.configure(bg="pink")

def trocar_imagem():
    lbl_imagem.config(image=imagem_tk2)
    lbl_imagem.image = imagem_tk2
    lbl_imagem.config(image = imagem_tk1)
    



img_pil = Image.open(r"C:\Users\RAFAELVICTORSOARESBI\Documents\python\images.jpg")
img_pil2 = Image.open(r"C:\Users\RAFAELVICTORSOARESBI\Documents\python\ally.png")
img_tk1 = img_pil.resize((200, 200))
img_tk2 = img_pil2.resize((200, 200))

imagem_tk1 = ImageTk.PhotoImage(img_tk1)
imagem_tk2 = ImageTk.PhotoImage(img_tk2)

lbl_texto = tk.Label(app, text="Imagem Exibida", font=("Comic Sans MS", 16))
lbl_texto.pack(pady=10)
lbl_imagem = tk.Label(app, image=imagem_tk1)
lbl_imagem.image = imagem_tk1
lbl_imagem.pack(pady=20)


btn = tk.Button(app, text="Trocar imagem", image=imagem_tk1, compound="right", bg = "green", fg = "purple", activebackground = "purple", disabledforeground = "pink")
btn.config(command=trocar_imagem)
btn.image = imagem_tk2
btn.pack(pady=10)


app.mainloop()