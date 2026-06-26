import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senai",
        database="saep_estoque"
    );

    return conexao;

def cadastrar_produto( nome, categoria , quantidade , preco ):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    insert into produtos  ( nome, categoria , quantidade , preco)
    values ( %s , %s , %s , %s )
    """

    valores = ( nome , categoria , quantidade , preco )

    cursor.execute( sql, valores )
    conexao.commit()

    cursor.close()
    conexao.close()


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("select id, nome, categoria, quantidade, preco from produtos")
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos

def excluir_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM produtos WHERE id = %s"
    cursor.execute(sql, (id_produto))

    conexao.commit()

    cursor.close()
    conexao.close()