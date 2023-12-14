from modulos import *


class Relatorios():
    def printClientes(self):
        webbrowser.open("bibi.pdf")

    def gera_relatorio(self):
        self.c = canvas.Canvas('bibi.pdf')
        self.codigoRel = self.codigo_entry.get()
        self.dataRel = self.data_entry.get()
        self.categoriaRel = self.categoria_entry.get()
        self.valorRel = self.valor_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha da bibi')

        self.c.setFont('Helvetica-Bold', 18)
        self.c.drawString(50, 700, 'Codigo: ')
        self.c.drawString(50, 670, 'data: ')
        self.c.drawString(50, 640, 'categoria: ')
        self.c.drawString(50, 610, 'valor: ')

        self.c.setFont('Helvetica', 18)
        self.c.drawString(150, 700,  self.codigoRel)
        self.c.drawString(150, 670,  self.dataRel)
        self.c.drawString(150, 640,  self.categoriaRel)
        self.c.drawString(150, 610,  self.valorRel)

        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printClientes()
