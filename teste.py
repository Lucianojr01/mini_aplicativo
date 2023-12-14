from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


'''self.Tipvar = StringVar()
        self.TipV = ('solteiro', 'casado', 'viuvo', 'divorciado')
        self.Tipvar.set('solteiro')
        self.popupMenu = OptionMenu(self.abas2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.1, rely=0.1, relheight=0.2, relwidth=0.2)'''


'''self.listaCli.delete(*self.listaCli.get_children())
        self.conectar_banco_dados()
        lista = self.cursor.execute(
            """SELECT cod,data,categoria, SUM(valor) FROM gastos GROUP BY data """)

        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconectar_banco()
        self.limpa_tela()
        self.atualizar_data()'''

root = tk.TK()


def agrupar_por_mes_e_mostrar(dados, treeview):
    # Converter a coluna "data" para o formato de data e criar uma coluna "mes"
    dados['data'] = pd.to_datetime(dados['data'])
    dados['mes'] = dados['data'].dt.month

    # Agrupar os valores por mês e categoria
    dados_agrupados = dados.groupby(['mes', 'categoria'])[
        'valor'].sum().reset_index()

    # Criar um dicionário para armazenar os resultados
    resultados = {}

    # Iterar sobre os dados agrupados e adicionar as categorias e valores ao dicionário
    for i, row in dados_agrupados.iterrows():
        mes = row['mes']
        categoria = row['categoria']
        valor = row['valor']

        if mes not in resultados:
            resultados[mes] = {}

        resultados[mes][categoria] = valor

    # Limpar o Treeview
    for row in treeview.get_children():
        treeview.delete(row)

    # Adicionar as categorias e valores ao Treeview
    for mes in resultados.keys():
        # Adicionar um item para o mês
        mes_item = treeview.insert(
            '', tk.END, text=f'Mês {mes}', values=('', ''))

        # Adicionar os itens de categoria e valor para o mês
        for categoria, valor in resultados[mes].items():
            treeview.insert(mes_item, tk.END, text='',
                            values=(categoria, valor))

    # Ajustar a largura das colunas do Treeview
    treeview.column('#0', width=100)
    treeview.column('#1', width=100)
    treeview.column('#2', width=100)

    # Adicionar as legendas e títulos ao Treeview
    treeview.heading('#0', text='Mês')
    treeview.heading('#1', text='Categoria')
    treeview.heading('#2', text='Valor')
    root.mainloop()
