from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy

from catalogo.views.VistaCatalogo import VistaCatalogo
from incassi.VistaIncassi import VistaIncassi
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
        v_layout.addWidget(self.get_generic_button("Incassi", self.go_incassi))

        v_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(v_layout)

        '''
        oImage = QImage("appStyle/IconaMarket.png")
        sImage = oImage.scaled(QSize(375, 300))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        '''
        self.resize(375, 300)
        self.setWindowTitle("Mercatino Usato")


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

    def go_incassi(self):
        self.vista_incassi = VistaIncassi()
        self.vista_incassi.show()