import tkinter as tk

app = tk.Tk()
app.geometry("500x500")
app.resizable(False, False)
app.title("Jogo da Cobrinha")

velocidade = 10
direcao = "Right"

pontos = tk.Label(app, text="0 Pontos", font=("Comic Sans MS",16))
pontos.pack(pady=10)


        




jogo = tk.Canvas(width="500", height="500", bg="Black")
jogo.pack()



m=jogo.create_oval(50, 10, 55, 20, outline="Red", width=20)
jogo.pack()
c=jogo.create_line(50, 50, 200, 50, fill="Green", width=10)

cima = app.bind("<Up>")
baixo = app.bind("<Down>")
esquerda = app.bind("<Left>")
direita = app.bind("<Right>")


jogo.pack()



app.mainloop()