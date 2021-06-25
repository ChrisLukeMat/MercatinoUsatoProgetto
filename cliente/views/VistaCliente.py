from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QMessageBox
from cliente.controller.ControllerCliente import ControllerCliente

class VistaCliente(QWidget):
    def __init__(self, cliente, parent=None):
        super(VistaCliente, self).__init__()
        self.controller = ControllerCliente(cliente)

        v_layout_tot = QVBoxLayout()
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

        v_layout_tot.addLayout(h_layout)
        v_layout_tot.addWidget(self.get_generic_button("Riscuoti saldo", self.vista_riscuoti))

        self.setLayout(v_layout_tot)
        self.resize(500, 400)
        self.setWindowTitle("{} {}".format(cliente.get_nome(), cliente.get_cognome()))

    def get_generic_label(self, text):
        label = QLabel(str(text))
        label.setStyleSheet("background-color: rgba(52,52,52,50%); border-radius: 7px; border: 1px solid black;")
        return label

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        button.setFixedWidth(150)
        button.setFixedHeight(50)
        return button

    def vista_riscuoti(self):
        view = QMessageBox()
        if self.controller.get_saldo() != 0.0:
            view.setText("Riscossione andata a buon fine!")
            self.controller.set_saldo(0.0)
        else:
            view.setIcon(QMessageBox.Critical)
            view.setText("Saldo nullo!")
        view.setWindowTitle("Riscossione saldo {} {}".format(self.controller.get_nome(), self.controller.get_cognome()))
        view.exec()