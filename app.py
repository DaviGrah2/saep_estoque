import tkinter as tk
from tkinter import messagebox
from banco import cadastrar_produto, listar_produtos, excluir_produto
from tkinter import ttk
#import customtkinter as ctk

janela = tk.Tk();
janela.title("SAEP Estoque Fácil");
janela.geometry("500x400");

frame_botoes = tk.Frame(janela, bg="#f4f6f8")
frame_botoes.pack(pady=10)

tabela = ttk.Treeview(
    janela,
    columns=("id", "nome", "categoria", "quantidade", "preco"),
    show="headings"
)

tabela.heading("id", text="ID")
tabela.heading("nome", text="Nome")
tabela.heading("categoria", text="Categoria")
tabela.heading("quantidade", text="Quantidade")
tabela.heading("preco", text="Preco")

tabela.column("id", width=50)
tabela.column("nome", width=160)
tabela.column("categoria", width=140)
tabela.column("quantidade", width=80)
tabela.column("preco", width=80)

tabela.pack(pady=10)

def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)

    produtos = listar_produtos()

    for produto in produtos:
        tabela.insert("", tk.END,
values=produto)

def excluir():
    item_selecionado = tabela.selection()

    if not item_selecionado:
        messagebox.showwarning("Atenção", "Selecione um produto para excluir")
        return   
    
    item = tabela.item(item_selecionado)
    id_produto = item["values"][0]    

    excluir_produto(id_produto)
    atualizar_tabela()

    messagebox.showinfo("Sucesso", "Produto excluido com sucesso !")

botao_excluir = tk.Button(
      frame_botoes,
      text="Excluir Produto",
      command=excluir,
      width=20,
      bg="#e7490f",
      fg="white",
      font=("Arial", 10, "bold")
)
botao_excluir.grid(row=0, column=2, padx=5)

titulo = tk.Label(
    janela,
    text="SAEP Estoque Fácil",
    font=("Arial", 18 , "bold")
);
titulo.pack(pady=10);

tk.Label(janela, text="Nome do Produto:").pack();
entrada_nome = tk.Entry(janela, width=40);
entrada_nome.pack();

tk.Label(janela, text="Categoria:").pack();
entrada_categoria = tk.Entry(janela, width=40);
entrada_categoria.pack();

tk.Label(janela, text="Quantidade:").pack();
entrada_quantidade = tk.Entry(janela, width=40);
entrada_quantidade.pack();

tk.Label(janela, text="Preço:").pack();
entrada_preco = tk.Entry(janela, width=40);
entrada_preco.pack();

def salvar():
    nome = entrada_nome.get();
    categoria = entrada_categoria.get();
    quantidade = entrada_quantidade.get();
    preco = entrada_preco.get();

    try:
      quantidade = int(quantidade)
      preco = float(preco)
    except ValueError:
      messagebox.showwarning(
          "Atenção",
          "Quantidade deve ser número inteiro e preço deve usar ponto. Exemplo: 2.50"
      )
      return
   
    if quantidade < 0:
      messagebox.showwarning("Atenção", "A quantidade não pode ser negativa.")
      return
   
    if preco <= 0:
      messagebox.showwarning

    if nome == "" or categoria == "" or quantidade == "" or preco == "":
        messagebox.showerror("Atenção","Preencha todos os campos.");
        return
    
    cadastrar_produto( nome , categoria , int(quantidade) , float(preco) );
    messagebox.showinfo("Sucesso" , "Produto cadastrado com sucesso!");
    limpar_campos()
    atualizar_tabela()

    entrada_nome.delete(0, tk.END);
    entrada_categoria.delete(0, tk.END);
    entrada_quantidade.delete(0, tk.END);
    entrada_preco.delete(0, tk.END);

def limpar_campos():
      entrada_nome.delete(0, tk.END)
      entrada_categoria.delete(0, tk.END)
      entrada_quantidade.delete(0, tk.END)
      entrada_preco.delete(0, tk.END)
      messagebox.showinfo("Sucesso", "Cadastro limpo com sucesso !")

botao_salvar = tk.Button(
      frame_botoes,
      text="Cadastrar Produto",
      command=salvar,
      width=20,
      bg="#164193",
      fg="white",
      font=("Arial", 10, "bold")
)
botao_salvar.grid(row=0, column=0, padx=5)

botao_limpar = tk.Button(
      frame_botoes,
      text="Limpar Campos",
      command=limpar_campos,
      width=20
)
botao_limpar.grid(row=0, column=1, padx=5)

atualizar_tabela()
janela.mainloop();
