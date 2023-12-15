from modulos import *
from Funcoes import Funcs
from GradientFrame import GradientFrame
from relatorios import Relatorios
import pandas as pd
root = tk.Tk()


class application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.abas()
        self.criando_botoes()
        self.lista_frame2()
        self.montar_tabela()
        self.select_lista()
        self.menus()
        self.criar_grafico()
        root.mainloop()

    def tela(self):
        self.root.title('Planilha de gastos Bibi e Ninho')
        self.root.configure(background='DimGray')
        self.root.geometry('1000x600')
        self.root.resizable(True, True)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='DarkSlateGray',
                             highlightbackground='gray', highlightthickness=5)

        self.frame_1.place(relx=0, rely=0.001, relwidth=0.999, relheight=0.50)

        self.frame_2 = Frame(self.root, bd=4, bg='DarkSlateGray',
                             highlightbackground='gray', highlightthickness=5)
        self.frame_2.place(relx=0, rely=0.5, relwidth=0.999, relheight=0.50)

    def abas(self):
        self.abas = ttk.Notebook(self.frame_1)
        self.abas1 = GradientFrame(self.abas, 'darkblue', 'Teal')
        self.abas2 = atk.Frame3d(self.abas, bg='DarkSlateGray')

        # self.abas1.configure(background='DarkSlateGray',)

        # self.abas2.configure(background='DarkSlateGray')

        self.abas.add(self.abas1, text='Dados')
        self.abas.add(self.abas2, text='Grafico')

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

    def criando_botoes(self):
        # usando canvas style dos botoes
        self.canvas_bt = Canvas(
            self.abas1, bd=0, bg='black', highlightbackground='gray', highlightthickness=4)
        self.canvas_bt.place(relx=0.19, rely=0.08,
                             relwidth=0.32, relheight=0.19)
        self.canvas_bt2 = Canvas(
            self.abas1, bd=0, bg='black', highlightbackground='gray', highlightthickness=4)
        self.canvas_bt2.place(relx=0.59, rely=0.08,
                              relwidth=0.32, relheight=0.19)
        # criando botao limpar
        self.bt_limpar = Button(
            self.abas1, text='Limpar', command=self.limpa_tela, bd=8, bg='darkblue', fg='white', font=('Helvetica', 12, 'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botao limpar
        self.bt_limpar = Button(
            self.abas1, text='Gastos', command=self.cria_janela, bd=8, bg='darkblue', fg='white', font=('Helvetica', 12, 'bold'))
        self.bt_limpar.place(relx=0.4, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botao buscar
        self.bt_buscar = Button(
            self.abas1, text='Buscar', bd=8, bg='darkblue', fg='white', font=('Helvetica', 12, 'bold'), command=self.busca_dados)
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botao novo
        self.bt_novo = Button(self.abas1, text='Adiciona', bd=8,
                              bg='darkblue', fg='white', font=('Helvetica', 12, 'bold'), command=self.add_dados)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botao alterar
        self.bt_alterar = Button(
            self.abas1, text='Alterar', bd=8, bg='darkblue', fg='white', font=('Helvetica', 12, 'bold'), command=self.alterar_dados)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botao apagar
        self.bt_apagar = Button(
            self.abas1, text='Apagar', bd=8, bg='darkblue', fg='white', font=('Helvetica', 12, 'bold'), command=self.deleta_dados)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # criaçao da label e entrada do codigo
        self.lb_codigo = Label(
            self.abas1, text='Codigo', bg='black', fg='blue', highlightthickness=2, highlightbackground='gray')
        self.lb_codigo.place(relx=0.05, rely=0.05,)

        self.codigo_entry = Entry(self.abas1, fg='black', font=(
            'Helvetica', 15, 'bold'), background='GreenYellow', border=6)
        self.codigo_entry.place(relx=0.05, rely=0.15,
                                relwidth=0.05, relheight=0.1)
        # criaçao da label e entrada do Categoria
        self.lb_categoria = Label(self.abas1, text='categoria', padx=10, pady=8, highlightthickness=4, highlightbackground='gray',
                                  bg='black', fg='blue', font=('Helvetica', 19, 'bold'))
        self.lb_categoria.place(relx=0.05, rely=0.30,
                                relwidth=0.2, relheight=0.15)

        self.categoria_entry = Entry(self.abas1, justify='center', fg='black', font=(
            'Helvetica', 15, 'bold'), background='GreenYellow', border=6)
        self.categoria_entry.place(relx=0.05, rely=0.45,
                                   relwidth=0.2, relheight=0.15)
        # criando label e entrada Valor
        self.lb_valor = Label(self.abas1, text='valor', padx=10, pady=8, highlightthickness=4, highlightbackground='gray',
                              bg='black', fg='blue', font=('Helvetica', 19, 'bold'))
        self.lb_valor.place(relx=0.35, rely=0.30, relwidth=0.2, relheight=0.15)

        
        self.valor_entry = Entry(self.abas1, justify='center', fg='black', font=(
            'Helvetica', 18, 'bold'), background='GreenYellow', border=6)
        self.valor_entry.place(relx=0.35, rely=0.45,
                               relwidth=0.2, relheight=0.15)
        # criando label e entrada Data
        self.lb_data = Label(self.abas1, text='Data :', padx=10, pady=8, highlightthickness=4, highlightbackground='gray',
                             bg='black', fg='blue', font=('Helvetica', 19, 'bold'))
        self.lb_data.place(relx=0.65, rely=0.30, relwidth=0.2, relheight=0.15)

        self.data_entry = Entry(self.abas1, fg='black', font=(
            'Helvetica', 18, 'bold'), background='GreenYellow', border=6)
        self.data_entry.place(relx=0.65, rely=0.45,
                              relwidth=0.2, relheight=0.15)

        # criando balao de mensagens
        atk.tooltip(
            self.bt_buscar, text='Digite no campo Categoria: a categoria que deseja Pesquisar')

        atk.tooltip(self.bt_limpar, text='Limpa todos os campos')

        atk.tooltip(self.bt_novo, text='Envia os dados')

        atk.tooltip(
            self.bt_apagar, text='Apaga os dados do sistema: de 2 click na informaçao que deseja apagar depois click aqui')

        atk.tooltip(
            self.bt_alterar, text='de 2 click n informaçao que deseja alterar faça as alteraçoes nos campos depois click aqui para alterar')

    def lista_frame2(self):
        style = ttk.Style()
        style.configure("BW.TLabel", foreground="white",
                        background="MidnightBlue", font=('clam', 15, 'bold'))
        self.listaCli = ttk.Treeview(
            self.frame_2, style="BW.TLabel", height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='codigo')
        self.listaCli.heading('#2', text='Data')
        self.listaCli.heading('#3', text='Categoria')
        self.listaCli.heading('#4', text='Valor')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', width=100)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=200)
        self.listaCli.column('#4', width=200)
        self.listaCli.place(relx=0.00, rely=0.00,
                            relwidth=0.99, relheight=1)

        self.scroollista = ttk.Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx=0.96, rely=0,
                               relwidth=0.04, relheight=1)
        self.listaCli.bind("<Double-1>", self.duplo_click)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenus2 = Menu(menubar)
        def Quit(): self.root.destroy()

        menubar.add_cascade(label="opçoes", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenus2)

        filemenu.add_command(label='Sair', background='red', command=Quit)
        filemenu.add_command(label='Reset',
                             background='green', command=self.select_lista)

        filemenus2.add_command(label='Ficha da bibi',
                               background='green', command=self.gera_relatorio)

    def cria_janela(self):
        self.root2 = Toplevel()
        self.root2.title('Bem vindo aos graficos')
        self.root2.configure(background='darkblue')
        self.root2.geometry('600x400')
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

        self.dados = tk.Text(self.root2, spacing1=1, spacing3=30, padx=70, pady=30,
                             bg='black', fg='white',  font=('Verdana', 15, 'bold'))
        self.dados.pack()
        self.conectar_banco_dados()
        self.cursor.execute(
            "SELECT Data,Categoria,Valor FROM gastos")

        df = self.cursor.fetchall()
        df2 = pd.DataFrame(df, columns=['Data', 'Categoria', 'Valor'])

        df2['Data'] = pd.to_datetime(df2['Data'])

        #df3 = df2.groupby(pd.Grouper(key='Data', freq='M')).sum()

        df4 = df2.groupby(['Data', 'Categoria'])['Valor'].sum()

        self.dados.delete('1.0', tk.END)
        #df3.sort_values(by='Data', inplace=True, ascending=False)
        #self.dados.insert(tk.END, df3.to_string(index=True))
        #df4.sort_values(by='Data', inplace=True, ascending=False)
        self.dados.insert(tk.END, df4.to_string(index=True))

    def criar_grafico(self):

        self.conectar_banco_dados()
        lista = self.cursor.execute(
            """SELECT data,valor FROM gastos ;""")
        lista2 = self.cursor.fetchall()
        lista2 = pd.DataFrame(lista2, columns=['data', 'valor'])
        lista2['data'] = pd.to_datetime(lista2['data'])
        lista2['mes'] = lista2['data'].dt.month

        # Agrupar os valores por mês
        dados_mes = lista2.groupby('mes')['valor'].sum()
        # print(dados_mes)
        # Criar uma figura matplotlib e um eixo
        fig = plt.Figure(figsize=(6, 4), dpi=100)
        eixo = fig.add_subplot(111)

        # Plotar os dados no eixo
        eixo.bar(dados_mes.index, dados_mes.values)

        # Definir o rótulo do eixo x como "Mês"
        eixo.set_xlabel('Mês')

 # for para aparecer os valores em texto
        for i, txt in enumerate(dados_mes):
            eixo.text(dados_mes.index[i], dados_mes.values[i], txt)
# adiciona o gráfico à janela do tkinter
        canvas = FigureCanvasTkAgg(fig, self.abas2)
        # canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)

application()
