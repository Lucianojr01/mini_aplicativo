from modulos import *


class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.data_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.categoria_entry.delete(0, END)

    def conectar_banco_dados(self):
        self.mydb = sqlite3.connect("gastos.bd")
        self.cursor = self.mydb.cursor()

    def desconectar_banco(self):
        self.mydb.close()

    def montar_tabela(self):

        self.conectar_banco_dados()
        print('conectado ao banco de dados')
        # criando tabela
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS gastos(
                                cod INTEGER PRIMARY KEY,
                                 data DATE,
                                  categoria CHAR(40),
                                   valor REAL(20)
                                    );""")
        self.mydb.commit()
        print("banco de dados criado")
        self.desconectar_banco()
        print('banco de dados desconectado')

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.data = self.data_entry.get()
        self.categoria = self.categoria_entry.get()
        self.valor = self.valor_entry.get()

    def add_dados(self):
        self.variaveis()
        # usando caixa de mensagem se os campo estiver vazio mensagem na tela usuario
        if self.categoria_entry.get() == '':
            msg = 'Campo CATEGORIA esta vazio '
            messagebox.showwarning('Presta atençao Bibi !!!!', msg)

        elif self.valor_entry.get() == '':
            msg = 'Campo VALOR esta vazio '
            messagebox.showinfo('Presta atençao Bibi !!!!', msg)

        else:
            self.conectar_banco_dados()
            self.atualizar_data()

            self.cursor.execute("""INSERT INTO gastos (data,categoria,valor)
            VALUES(?, ?, ?)""", (self.data, self.categoria, self.valor))
            self.mydb.commit()
            self.desconectar_banco()
            self.select_lista()
            self.limpa_tela()
            self.atualizar_data()
            self.criar_grafico()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectar_banco_dados()
        lista = self.cursor.execute(
            """SELECT cod, data,categoria,valor FROM gastos ORDER BY data DESC;""")
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconectar_banco()
        self.limpa_tela()
        self.atualizar_data()

    def duplo_click(self, event):
        self.limpa_tela()
        self.listaCli.selection()
        for i in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(i, 'values')
            self.codigo_entry.insert(END, col1)
            self.data_entry.insert(END, col2)
            self.categoria_entry.insert(END, col3)
            self.valor_entry.insert(END, col4)

    def deleta_dados(self):
        self.variaveis()
        self.conectar_banco_dados()
        self.cursor.execute(
            """DELETE FROM gastos WHERE cod = ? """, (self.codigo,))
        self.mydb.commit()
        self.desconectar_banco()
        self.limpa_tela()
        self.select_lista()
        self.limpa_tela()
        self.atualizar_data()

    def alterar_dados(self):
        self.variaveis()
        self.conectar_banco_dados()
        self.cursor.execute(
            """ UPDATE gastos SET data =?, categoria= ?, valor= ? WHERE cod = ?""",
            (self.data, self.categoria, self.valor, self.codigo))
        self.mydb.commit()
        self.desconectar_banco()
        self.select_lista()
        self.limpa_tela()
        self.atualizar_data()

    def busca_dados(self):
        self.conectar_banco_dados()
        self.listaCli.delete(*self.listaCli.get_children())
        self.categoria_entry.insert(END, '%')
        nome = self.categoria_entry.get()
        self.cursor.execute(
            """SELECT cod,data,categoria,valor FROM gastos WHERE categoria LIKE '%s' ORDER BY categoria ASC """ % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert('', END, values=i)

        self.limpa_tela()
        self.atualizar_data()
        self.desconectar_banco()

    def atualizar_data(self):
        self.data_atual = datetime.datetime.now()
        self.data_formatada = self.data_atual.strftime('%Y/%m/%d')
        self.data_entry.insert(0, self.data_formatada)

    def somar_gasto(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conectar_banco_dados()
        lista = self.cursor.execute(
            """SELECT cod,data,categoria, SUM(valor) FROM gastos GROUP BY categoria """)

        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconectar_banco()
        self.limpa_tela()
        self.atualizar_data()
