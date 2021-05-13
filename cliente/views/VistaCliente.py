from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy

from cliente.controller.ControllerCliente import ControllerCliente

class VistaCliente:
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__()
        self.controller = ControllerCliente(cliente)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.get_generic_label(self.controller.get_nome()))
        v_layout.addWidget(self.get_generic_label(self.controller.get_cognome()))
        v_layout.addWidget(self.get_generic_label(self.controller.get_cf()))
        v_layout.addWidget(self.get_generic_label(self.controller.get_data_nascita()))
        v_layout.addWidget(self.get_generic_label(self.controller.get_luogo_nascita()))
        v_layout.addWidget(self.get_generic_label(self.controller.get_indirizzo()))
        v_layout.addWidget(self.get_generic_label(self.controller.get_telefono()))
        v_layout.addWidget(self.get_generic_label(self.controller.get_id_cliente()))

        h_layout.addLayout(v_layout)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_cliente))
        #buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_cliente))
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(500,400)
        self.setWindowTitle("{} {}".format(cliente.get_nome, cliente.get_cognome()))

    def get_generic_label(self, text):
        label = QLabel(text)
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        return label

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    #def show_modifica_oggetto(self):