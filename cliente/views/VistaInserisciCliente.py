from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtCore import Qt

from cliente.model.Cliente import Cliente

class VistaInserisciCliente(QWidget):
    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciCliente, self).__init__(parent)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Cognome"))
        self.text_cognome = QLineEdit(self)
        v_layout.addWidget(self.text_cognome)

        v_layout.addWidget(QLabel("Codice fiscale"))
        self.text_cf = QLineEdit(self)
        v_layout.addWidget(self.text_cf)

        v_layout.addWidget(QLabel("Data nascita"))
        self.text_data_nascita = QLineEdit(self)
        v_layout.addWidget(self.text_data_nascita)

        v_layout.addWidget(QLabel("Luogo nascita"))
        self.text_luogo_nascita = QLineEdit(self)
        v_layout.addWidget(self.text_luogo_nascita)

        v_layout.addWidget(QLabel("Telefono"))
        self.text_telefono = QLineEdit(self)
        v_layout.addWidget(self.text_telefono)

        v_layout.addWidget(QLabel("Indirizzo"))
        self.text_indirizzo = QLineEdit(self)
        v_layout.addWidget(self.text_indirizzo)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_cliente)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.resize(300,450)
        self.setWindowTitle('Nuovo cliente')

    def add_cliente(self):
        nome = self.text_nome.text()
        cognome = self.text_cognome.text()
        cf = self.text_cf.text()
        data_nascita = self.text_data_nascita.text()
        luogo_nascita = self.text_luogo_nascita.text()
        telefono = self.text_telefono.text()
        indirizzo = self.text_indirizzo.text()

        if nome == "" or cognome == "" or cf == "" or data_nascita == "" or luogo_nascita == "" or telefono == "" or indirizzo == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_cliente(
                Cliente(nome, cognome, cf, data_nascita, luogo_nascita, telefono, indirizzo))
            self.callback()
            self.close()