from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy

from catalogo.views.VistaCatalogo import VistaCatalogo


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_button("Catalogo", self.go_catalogo()))
        v_layout.addWidget(self.get_generic_button("Lista Clienti", self.go_lista_clienti()))


        self.setLayout(v_layout)
        self.resize(400,300)
        self.setWindowTitle("Mercatino")


    def get_generic_button(self,titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return button

    def go_catalogo(self):
        self.vista_catalogo = VistaCatalogo()
        self.vista_catalogo.show()


    def go_lista_clienti(self):
        pass
       # self.vista_lista_clienti = VistaListaClienti()
       # self.vista_lista_clienti.show()