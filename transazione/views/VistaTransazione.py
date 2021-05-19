from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from transazione.controller.ControllerTransazione import ControllerTransazione
from transazione.model.Transazione import Transazione

class VistaTransazione(QWidget):
    def __init__(self, transazione, parent=None):
        super(VistaTransazione, self).__init__(parent)
        self.controller = ControllerTransazione(transazione)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v_layout2 = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label("Oggetto venduto: "))
        v_layout.addWidget(self.get_generic_label("Prezzo: "))
        v_layout.addWidget(self.get_generic_label("Proprietario: "))
        v_layout.addWidget(self.get_generic_label("Acquirente: "))
        v_layout.addWidget(self.get_generic_label("Data Vendita: "))
        v_layout.addWidget(self.get_generic_label("Id Transazione: "))
        v_layout.addStretch()

        self.acquirente = self.controller.get_acquirente()
        v_layout2.addWidget(self.get_generic_label(self.controller.get_oggetto_venduto().nome))
        v_layout2.addWidget(self.get_generic_label((str(self.controller.get_oggetto_venduto().prezzo) + " €")))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_oggetto_venduto().proprietario.get_nome() + " " + self.controller.get_oggetto_venduto().proprietario.get_cognome() + " " + self.controller.get_oggetto_venduto().proprietario.get_id_cliente()))
        v_layout2.addWidget(self.get_generic_label(self.acquirente.get_nome() + " " +
                                                   self.acquirente.get_cognome() + " " +
                                                   self.acquirente.get_id_cliente()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_data_vendita().strftime("%d-%m-%Y")))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_id_transazione()))
        v_layout2.addStretch()

        h_layout.addLayout(v_layout)
        h_layout.addLayout(v_layout2)
        h_layout.setContentsMargins(15, 0, 125, 0)
        h_layout.addStretch()

        self.setLayout(h_layout)
        self.resize(500, 400)
        self.setWindowTitle("Vendita oggetto: " + self.controller.get_oggetto_venduto().nome)

    def get_generic_label(self, text):
        label = QLabel(str(text))
        label.setFont(QFont('Arial', 10))
        return label