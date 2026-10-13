import tkinter as tk
def somar (event):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        lbl_res.config(text=f"Resultado: {n1 + n2}")
    except ValueError:
        lbl_res.config(text="Digite valores válidos!")

def subtrair (event):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        lbl_res.config(text=f"Resultado: {n1 - n2}")
    except ValueError:
        lbl_res.config(text="Digite valores válidos!")
def dividir (event):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        lbl_res.config(text=f"Resultado: {n1 / n2}")
    except ValueError:
        lbl_res.config(text="Digite valores válidos!")
def multiplicar (event):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        lbl_res.config(text=f"Resultado: {n1 * n2}")
    except ValueError:
        lbl_res.config(text="Digite valores válidos!")


app = tk.Tk()
app.title ("Calculadora")
app.geometry("500x400")


entry1 = tk.Entry(app); entry1.pack(pady=5)
entry2 = tk.Entry(app); entry2.pack(pady=5)
btn = tk.Button(app, text="+", command=somar); btn.place(x=200 , y=100)
btn = tk.Button(app, text="-", command=subtrair); btn.place(x = 200 , y = 150)
btn = tk.Button(app, text="/", command=dividir); btn.place(x = 300 , y = 100)
btn = tk.Button(app, text="*", command=multiplicar); btn.place(x = 300 , y = 150)
app.bind("<Return>", somar)
app.bind("<Insert>", subtrair)
app.bind("<Delete>", dividir)
app.bind("<Home>", multiplicar)
lbl_res = tk.Label(app, text="Resultado: "); lbl_res.place(x =230 , y = 200)


app.mainloop()