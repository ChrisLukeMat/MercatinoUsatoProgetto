from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy, QHBoxLayout

from catalogo.views.VistaCatalogo import VistaCatalogo
from incassi.VistaIncassi import VistaIncassi
from listaclienti.views.VistaListaClienti import VistaListaClienti
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti
from listatransazioni.views.VistaListaTransazioni import VistaListaTransazioni


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        v_layout = QVBoxLayout()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()

        h_layout1.addWidget(self.get_generic_button("Catalogo", self.go_catalogo))
        h_layout1.addWidget(self.get_generic_button("Clienti", self.go_lista_clienti))
        h_layout2.addWidget(self.get_generic_button("Dipendenti", self.go_lista_dipendenti))
        h_layout2.addWidget(self.get_generic_button("Transazioni", self.go_lista_transazioni))
        h_layout2.addWidget(self.get_generic_button("Incassi", self.go_incassi))

        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        self.setLayout(v_layout)

        self.resize(1200, 650)
        self.setWindowTitle("Mercatino Usato")


    def get_generic_button(self,titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(350)
        button.setFixedHeight(150)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.setMaximumWidth(350)
        button.clicked.connect(on_click)
        button.setFont(QFont("Calibri", 20, QFont.Bold))
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

    def go_incassi(self):
        self.vista_incassi = VistaIncassi()
        self.vista_incassi.show()