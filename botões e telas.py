import tkinter as tk
from PIL import ImageTk, Image


def tela_1():
    frame_tela1.pack_forget()
    frame_tela2.pack(fill="both", expand=True)

def tela_2():
    frame_tela2.pack_forget()
    frame_tela1.pack(fill="both", expand=True)

def trocar_cor1():
    btn1.config(bg="green" )
    btn2.config(bg="pink")
def trocar_cor2():
    btn1.config(bg="pink")
    btn2.config(bg="green")
def alterar_fundo(event):
    app.config(bg="yellow")


    

app = tk.Tk()
app.title("trocar cores entre botões")
app.geometry("400x400")
app.configure(bg="yellow")


frame_tela1 = tk.Frame(app)
btn3 = tk.Button(frame_tela1, text= "Trocar Tela", command=tela_1)
btn3.pack (pady=10)
btn1 = tk.Button(frame_tela1, text="Trocar Cor", bg="pink", command=trocar_cor1)
btn1.pack(pady=10)
label = tk.Label(frame_tela1, text="Alterar cor de fundo")
app.bind("<Return>", alterar_fundo)
label.pack(pady=10)

img1 = Image.open(r"C:\Users\RAFAELVICTORSOARESBI\Documents\python\imaagem.jpg")
img1 = ImageTk.PhotoImage(img1)
label_img1 = tk.Label(frame_tela1, image=img1)
label_img1.pack(pady=10)



frame_tela2 = tk.Frame(app)
btn4 = tk.Button(frame_tela2, text= "Trocar Tela", command=tela_2)
btn4.pack (pady=10)
btn2 = tk.Button(frame_tela2, text="Trocar Cor", bg="green", command=trocar_cor2)
btn2.pack(pady=10)
frame_tela1.pack(fill="both", expand=True)

img2 = Image.open(r"C:\Users\RAFAELVICTORSOARESBI\Documents\python\ally.png")
img2 = img2.resize((200,200))
img2 = ImageTk.PhotoImage(img2)
label_img2 = tk.Label(frame_tela2, image=img2)
label_img2.pack(pady=10)


app.mainloop()
