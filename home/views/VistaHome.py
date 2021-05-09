from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy

from catalogo.views.VistaCatalogo import VistaCatalogo
from listadipendenti.views.VistaListaDipendenti import VistaListaDipendenti


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_button("Catalogo", self.go_catalogo))
        v_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti))
        v_layout.addWidget(self.get_generic_button("Lista Dipendenti", self.go_lista_dipendenti))
        v_layout.addWidget(self.get_generic_button("Lista Transazioni", self.go_lista_transazioni))


        self.setLayout(v_layout)
        self.resize(300,250)
        self.setWindowTitle("Mercatino")


    def get_generic_button(self,titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_catalogo(self):
        self.vista_catalogo = VistaCatalogo()
        self.vista_catalogo.show()


    def go_lista_clienti(self):
        pass
       # self.vista_lista_clienti = VistaListaClienti()
       # self.vista_lista_clienti.show()

    def go_lista_dipendenti(self):
       self.vista_lista_dipendenti = VistaListaDipendenti()
       self.vista_lista_dipendenti.show()

    def go_lista_transazioni(self):
        pass
       # self.vista_lista_transazioni = VistaListaTransazioni()
       # self.vista_lista_transazioni.show()