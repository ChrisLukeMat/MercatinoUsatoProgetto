from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy

from dipendente.controller.ControllerDipendente import ControllerDipendente

class VistaDipendente(QWidget):
    def __init__(self, dipendente, parent=None):
        super(VistaDipendente, self).__init__()
        self.controller = ControllerDipendente(dipendente)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label("Nome: " + self.controller.get_nome()))
        v_layout.addWidget(self.get_generic_label("Cognome:" + self.controller.get_cognome()))
        v_layout.addWidget(self.get_generic_label("Codice Fiscale: " + self.controller.get_cf()))
        v_layout.addWidget(self.get_generic_label("Data Nascita: " + str(self.controller.get_data_nascita())))
        v_layout.addWidget(self.get_generic_label("Luogo Nascita: " + self.controller.get_luogo_nascita()))
        v_layout.addWidget(self.get_generic_label("Indirizzo: " + self.controller.get_indirizzo()))
        v_layout.addWidget(self.get_generic_label("Telefono: " + self.controller.get_telefono()))
        v_layout.addWidget(self.get_generic_label("Id: " + self.controller.get_id_dipendente()))

        h_layout.addLayout(v_layout)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_dipendente))
        #buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_dipendente))
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(500,400)
        self.setWindowTitle("{} {}".format(dipendente.get_nome, dipendente.get_cognome()))

    def get_generic_label(self, text):
        label = QLabel(str(text))
        font = label.font()
        font.setStyle(QFont.StyleItalic)
        font.setPointSize(15)
        label.setFont(font)
        return label

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def show_modifica_dipendente(self):
        pass