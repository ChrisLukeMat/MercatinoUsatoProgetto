from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from vendita.controller.ControllerVendita import ControllerVendita
from vendita.model.Vendita import Vendita

class VistaVendita(QWidget):
    def __init__(self, vendita, parent=None):
        super(VistaVendita, self).__init__()
        self.controller = ControllerVendita(vendita)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v_layout2 = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label("Oggetto venduto: "))
        v_layout.addWidget(self.get_generic_label("Acquirente: "))
        v_layout.addWidget(self.get_generic_label("Data Vendita: "))

        self.acquirente = self.controller.get_acquirente()
        v_layout2.addWidget(self.get_generic_label(self.controller.get_oggetto_venduto().get_nome()))
        v_layout2.addWidget(self.get_generic_label(self.acquirente.get_nome() + " " +
                                                   self.acquirente.get_cognome() + " " +
                                                   self.acquirente.get_id_cliente()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_data_vendita()))

        h_layout.addLayout(v_layout)
        h_layout.addLayout(v_layout2)
        h_layout.setContentsMargins(15, 0, 125, 0)
        h_layout.addStretch()

        self.setLayout(h_layout)
        self.resize(500, 400)
        self.setWindowTitle("Vendita oggetto: " + self.controller.get_oggetto_venduto().get_nome())

    def get_generic_label(self, text):
        label = QLabel(str(text))
        label.setFont(QFont('Arial', 10))
        return label