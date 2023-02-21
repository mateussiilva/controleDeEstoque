import sqlite3


class Dados():
    def __init__(self):
        conexao = sqlite3.connect('produtos.db')
        cursor = conexao.cursor()
        try:
            cursor.execute("""
                CREATE TABLE produtos(
                    nome text,
                    validade text,
                    quantidade text,
                    valor text,
                )               
            """)
            conexao.commit()
        except:
            print("ERR0")
        finally:
            cursor.close()
            conexao.close()
            
if __name__ == "__main__":
    banco = Dados()