import json
import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel
from datetime import *
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


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
        self.grafico(15, 9)
        self.prova = GraficoAndamento()
        self.prova.show()

    def show_mese(self):
        self.riempi_liste(30)
        self.grafico(15, 9)
        self.prova = GraficoAndamento()
        self.prova.show()

    def riempi_liste(self, numero_giorni):
        lista_totale = []
        self.lista_date.clear()
        self.lista_incassi.clear()
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
        plt.cla()
        dates = matplotlib.dates.date2num(self.lista_date)
        matplotlib.pyplot.plot_date(dates, self.lista_incassi, marker='o', color='blue')
        myFmt = mdates.DateFormatter('%d/%m')
        plt.gca().xaxis.set_major_formatter(myFmt)
        plt.xticks(dates)

        for i, v in enumerate(self.lista_incassi):
            plt.annotate(str(v), xy=(dates[i], v), xytext=(-7, 7), textcoords='offset points')
        plt.xlabel("Giorni")
        plt.ylabel("Incassi (€)")
        plt.gcf().autofmt_xdate()
        plt.gcf().set_size_inches(length, width)
        plt.savefig('incassi/graficoIncassi.svg', format='svg', dpi=1200)


class GraficoAndamento(QWidget):
    def __init__(self, parent = None):
        super(GraficoAndamento, self).__init__(parent)

        self.pixmap = QPixmap('incassi/graficoIncassi.svg')
        self.label = QLabel()
        self.label.setPixmap(self.pixmap)
        lay = QVBoxLayout()
        lay.addWidget(self.label)
        lay.setAlignment(Qt.AlignCenter)

        self.setLayout(lay)

        self.setWindowTitle("Grafico andamento incassi")