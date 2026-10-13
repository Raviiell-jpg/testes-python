import tkinter as tk 

def mostrar_tela2():
    frame_tela1.pack_forget()
    frame_tela2.pack(fill="both", expand=True)
def mostrar_tela1():
    frame_tela2.pack_forget()
    frame_tela1.pack(fill="both", expand=True)
app = tk.Tk(); app.title("Aplicação Multi-Telas"); app.geometry("300x200")

frame_tela1 = tk.Frame(app)
tk.Label(frame_tela1, text="Tela 1", font=("Comic Sans MS", 16)).pack(pady=20)
tk.Button(frame_tela1, text="Ir para Tela 2",width=40, height=4, command=mostrar_tela2).pack(pady=10)
frame_tela2 = tk.Frame(app)
tk.Label(frame_tela2, text="Tela 2", font=("Comic Sans MS", 16)).pack(pady=20)
tk.Button(frame_tela2, text="Voltar para Tela 1", width=40, height=4, command=mostrar_tela1).pack(pady=10)
frame_tela1.pack(fill="both", expand=True)
app.mainloop()