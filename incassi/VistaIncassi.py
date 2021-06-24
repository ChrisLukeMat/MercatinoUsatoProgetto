import json
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy
from datetime import *
from matplotlib import rcParams
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class VistaIncassi(QWidget):
    def __init__(self, parent=None):
        super(VistaIncassi, self).__init__(parent)

        self.lista_date = []
        self.lista_incassi = []

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Ultima settimana", self.show_settimana))
        buttons_layout.addWidget(self.get_generic_button("Ultimo mese", self.show_mese))

        buttons_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(buttons_layout)
        self.resize(720, 400)
        self.setWindowTitle("Incassi")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(350)
        button.setFixedHeight(150)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setMaximumWidth(500)
        button.clicked.connect(on_click)
        return button

    def show_settimana(self):
        self.riempi_liste(7)
        self.grafico(10, 6)
        '''prova = GraficoAndamento(self.lista_date, self.lista_incassi)
        prova.show()'''


    def show_mese(self):
        self.riempi_liste(30)
        self.grafico(15, 8)

    def riempi_liste(self, numero_giorni):
        lista_totale = []
        if os.path.isfile('incassi/incassi.json'):
            with open('incassi/incassi.json') as f:
                lista_totale = json.load(f)
                f.close()

            for i in range (0, len(lista_totale)):
                data = datetime.strptime(lista_totale[i].get("data"), "%d/%m/%Y")
                if datetime.today() - data <= timedelta(days = numero_giorni) and datetime.today() - data > timedelta(days = 0):
                    self.lista_date.append(data)
                    self.lista_incassi.append(lista_totale[i].get("incasso"))

    def grafico(self, length, width):
        rcParams['figure.figsize'] = length, width

        dates = matplotlib.dates.date2num(self.lista_date)
        matplotlib.pyplot.plot_date(dates, self.lista_incassi, marker='o', color='blue')
        myFmt = mdates.DateFormatter('%d/%m')
        plt.gca().xaxis.set_major_formatter(myFmt)
        plt.xticks(dates)
        plt.yticks(self.lista_incassi)
        plt.xlabel("Giorni")
        plt.gcf().autofmt_xdate()
        plt.show()


'''class GraficoAndamento(QWidget):
    def __init__(self,lista_date, lista_incassi, parent = None):
        super(GraficoAndamento, self).__init__(parent)

        self.lista_date = lista_date
        self.lista_incassi = lista_incassi
        v_layout = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        v_layout.addWidget(self.canvas)
        self.grafico(10, 6)

    def grafico(self, length, width):
        rcParams['figure.figsize'] = length, width
        graph = self.canvas.figure.subplots()
        dates = matplotlib.dates.date2num(self.lista_date)
        graph.matplotlib.pyplot.plot_date(dates, self.lista_incassi, marker='o', color='blue')
        myFmt = mdates.DateFormatter('%d/%m')
        plt.gca().xaxis.set_major_formatter(myFmt)
        plt.xticks(dates)
        plt.yticks(self.lista_incassi)
        plt.xlabel("Giorni")
        plt.gcf().autofmt_xdate()
        self.canvas.draw()'''