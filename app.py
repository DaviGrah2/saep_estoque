import tkinter as tk
from tkinter import messagebox
from banco import cadastrar_produto
#import customtkinter as ctk

janela = tk.Tk()
janela.title("SAEP Estoque Fácil");
janela.geometry("500x400");



titulo = tk.Label(
    janela,
    text="SAEP Estoque Fácil",
    font=("Arial", 18 , "bold")
);
titulo.pack(pady=10);

tk.Label(janela, text="Nome do Produto:").pack
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()

tk.Label(janela, text="Catrgoria:").pack
entrada_categoria = tk.Entry(janela, width=40)
entrada_categoria.pack()

tk.Label(janela, "Quantidade:").pack
entrada_quantidade = tk.Entry(janela, width=40)
entrada_quantidade.pack()

tk.Label(janela, text="Preço:").pack
entrada_preco = tk.Entry(janela, width=40)
entrada_preco.pack()

