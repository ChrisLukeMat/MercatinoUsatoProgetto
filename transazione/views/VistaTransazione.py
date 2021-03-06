from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel

from transazione.controller.ControllerTransazione import ControllerTransazione

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

        self.acquirente = self.controller.get_acquirente()
        v_layout2.addWidget(self.get_generic_label(self.controller.get_oggetto_venduto().nome))
        v_layout2.addWidget(self.get_generic_label((str(self.controller.get_oggetto_venduto().prezzo) + " €")))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_oggetto_venduto().proprietario.get_nome() + " " + self.controller.get_oggetto_venduto().proprietario.get_cognome() + " " + self.controller.get_oggetto_venduto().proprietario.get_id_cliente()))
        v_layout2.addWidget(self.get_generic_label(self.acquirente.get_nome() + " " +
                                                   self.acquirente.get_cognome() + " " +
                                                   self.acquirente.get_id_cliente()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_data_vendita().strftime("%d-%m-%Y")))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_id_transazione()))

        h_layout.addLayout(v_layout)
        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.resize(500, 400)
        self.setWindowTitle("Vendita oggetto: " + self.controller.get_oggetto_venduto().nome)

    def get_generic_label(self, text):
        label = QLabel(str(text))
        label.setMinimumHeight(40)
        label.setStyleSheet("background-color: rgba(52,52,52,50%); border-radius: 7px; border: 1px solid black;")
        return label