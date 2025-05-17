import sqlite3
import tkinter as tk
from tkinter import messagebox, PhotoImage


# Banco de dados
conexao = sqlite3.connect('loja_roupas.db')
cursor = conexao.cursor()

# Tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT
)
''')
conexao.commit()

# Cores personalizadas
COR_FUNDO = "#FD99AA"
COR_TEXTO = "#D3D3D3"

# Função de cadastro
def cadastrar_cliente():
    nome = entrada_nome.get()
    email = entrada_email.get()
    telefone = entrada_telefone.get()

    if nome and email:
        cursor.execute('''
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
        ''', (nome, email, telefone))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        entrada_nome.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_telefone.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Nome e Email são obrigatórios.")

# Função de listagem
def listar_clientes():
    lista_texto.delete("1.0", tk.END)
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    if clientes:
        for cliente in clientes:
            linha = f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Telefone: {cliente[3]}\n"
            lista_texto.insert(tk.END, linha)
    else:
        lista_texto.insert(tk.END, "Nenhum cliente cadastrado.")

# Interface gráfica
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.configure(bg=COR_FUNDO)

# Labels e entradas
tk.Label(janela, text="Nome:", bg=COR_FUNDO, fg=COR_TEXTO).grid(row=0, column=0, sticky="e")
entrada_nome = tk.Entry(janela, width=30)
entrada_nome.grid(row=0, column=1)

tk.Label(janela, text="Email:", bg=COR_FUNDO, fg=COR_TEXTO).grid(row=1, column=0, sticky="e")
entrada_email = tk.Entry(janela, width=30)
entrada_email.grid(row=1, column=1)

tk.Label(janela, text="Telefone:", bg=COR_FUNDO, fg=COR_TEXTO).grid(row=2, column=0, sticky="e")
entrada_telefone = tk.Entry(janela, width=30)
entrada_telefone.grid(row=2, column=1)

# Botões
btn_cadastrar = tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente, bg=COR_TEXTO)
btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

btn_listar = tk.Button(janela, text="Listar Clientes", command=listar_clientes, bg=COR_TEXTO)
btn_listar.grid(row=4, column=0, columnspan=2)

# Área de texto
lista_texto = tk.Text(janela, height=10, width=50, bg="#ffffff", fg="#000000")
lista_texto.grid(row=5, column=0, columnspan=2, pady=10)



# Fecha a conexão
conexao.close()

# Inicia a janela
janela.mainloop()