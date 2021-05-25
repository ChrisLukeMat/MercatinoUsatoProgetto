from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QGridLayout
import tkinter as tk

from catalogo.views.VistaCatalogo import VistaCatalogo
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listatransazioni.views.VistaListaTransazioni import VistaListaTransazioni


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_button("Catalogo", self.go_catalogo))
        v_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti))
        v_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti))
        v_layout.addWidget(self.get_generic_button("Lista Transazioni", self.go_lista_transazioni))

        v_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(v_layout)

        '''
        self.img = QPixmap("appStyle/IconaMarket.png")
        self.label = QLabel()
        self.label.setPixmap(self.img)
        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)
        '''

        #self.setFixedWidth(375)
        #self.setFixedHeight(300)
        self.resize(375,300)
        self.setWindowTitle("Mercatino")


    def get_generic_button(self,titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(350)
        button.setFixedHeight(150)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setMaximumWidth(500)
        button.clicked.connect(on_click)
        return button

    def go_catalogo(self):
        self.vista_catalogo = VistaCatalogo()
        self.vista_catalogo.show()


    def go_lista_clienti(self):
       self.vista_lista_clienti = VistaListaClienti()
       self.vista_lista_clienti.show()

    def go_lista_dipendenti(self):
       self.vista_lista_dipendenti = VistaListaDipendenti()
       self.vista_lista_dipendenti.show()

    def go_lista_transazioni(self):
       self.vista_lista_transazioni = VistaListaTransazioni()
       self.vista_lista_transazioni.show()