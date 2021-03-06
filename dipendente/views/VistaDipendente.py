from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from dipendente.controller.ControllerDipendente import ControllerDipendente

class VistaDipendente(QWidget):
    def __init__(self, dipendente, parent=None):
        super(VistaDipendente, self).__init__(parent)
        self.controller = ControllerDipendente(dipendente)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v_layout2 = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label("Nome: "))
        v_layout.addWidget(self.get_generic_label("Cognome: "))
        v_layout.addWidget(self.get_generic_label("Codice Fiscale: "))
        v_layout.addWidget(self.get_generic_label("Data Nascita: "))
        v_layout.addWidget(self.get_generic_label("Luogo Nascita: "))
        v_layout.addWidget(self.get_generic_label("Indirizzo: "))
        v_layout.addWidget(self.get_generic_label("Telefono: "))
        v_layout.addWidget(self.get_generic_label("Id: "))
        v_layout.addWidget(self.get_generic_label("Username: "))
        v_layout.addWidget(self.get_generic_label("Password: "))

        v_layout2.addWidget(self.get_generic_label(self.controller.get_nome()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_cognome()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_cf()))
        v_layout2.addWidget(self.get_generic_label((self.controller.get_data_nascita()).strftime("%d-%m-%Y")))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_luogo_nascita()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_indirizzo()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_telefono()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_id_dipendente()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_username()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_password()))

        h_layout.addLayout(v_layout)
        h_layout.addLayout(v_layout2)

        self.setLayout(h_layout)
        self.resize(500, 400)
        self.setWindowTitle("{} {}".format(dipendente.get_nome(), dipendente.get_cognome()))

    def get_generic_label(self, text):
        label = QLabel(str(text))
        label.setMinimumHeight(40)
        label.setStyleSheet("background-color: rgba(52,52,52,50%); border-radius: 7px; border: 1px solid black;")
        return label