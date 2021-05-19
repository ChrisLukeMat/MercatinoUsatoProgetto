from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy

from cliente.controller.ControllerCliente import ControllerCliente

class VistaCliente(QWidget):
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__()
        self.controller = ControllerCliente(cliente)

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
        v_layout.addWidget(self.get_generic_label("Saldo: "))

        v_layout2.addWidget(self.get_generic_label(self.controller.get_nome()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_cognome()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_cf()))
        v_layout2.addWidget(self.get_generic_label((self.controller.get_data_nascita()).strftime("%d-%m-%Y")))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_luogo_nascita()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_indirizzo()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_telefono()))
        v_layout2.addWidget(self.get_generic_label(self.controller.get_id_cliente()))
        v_layout2.addWidget(self.get_generic_label(str(self.controller.get_saldo()) + " €"))

        h_layout.addLayout(v_layout)
        h_layout.addLayout(v_layout2)
        h_layout.setContentsMargins(15, 0, 125, 0)
        h_layout.addStretch()

        self.setLayout(h_layout)
        self.resize(500,400)
        self.setWindowTitle("{} {}".format(cliente.get_nome(), cliente.get_cognome()))

    def get_generic_label(self, text):
        label = QLabel(str(text))
        label.setFont(QFont('Arial', 10))
        #font = label.font()
        #font.setStyle(QFont())
        #font.setPointSize(15)
        #label.setFont(font)
        return label

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button