import json
import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from home.views.VistaHome import VistaHome


class VistaLogin(QWidget):
    def __init__(self, vista_home):
        super(VistaLogin, self).__init__()

        self.vista_home = vista_home
        self.trovato = False
        v_layout = QVBoxLayout()

        v_layout.addWidget(QLabel("Username"))
        self.text_username = QLineEdit(self)
        v_layout.addWidget(self.text_username)

        v_layout.addWidget(QLabel("Password"))
        self.text_password = QLineEdit(self)
        v_layout.addWidget(self.text_password)

        button_login = QPushButton("Login")
        button_login.clicked.connect(self.controlla_credenziali)
        v_layout.addWidget(button_login)

        self.setLayout(v_layout)
        self.resize(250, 300)
        self.setWindowTitle('Login')


    def controlla_credenziali(self):
        if os.path.isfile('accessocredenziali/credenziali.json'):
            with open('accessocredenziali/credenziali.json') as f:
                lista_credenziali = json.load(f)
                for credenziali in lista_credenziali:
                    if credenziali["username"] == self.text_username.text() and credenziali["password"] == self.text_password.text():
                        self.trovato = True
                        self.close()
                        self.vista_home.show()
                if not self.trovato:
                    QMessageBox.critical(self, 'Errore', "Credenziali errate", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Errore', "File credenziali.json non trovato", QMessageBox.Ok, QMessageBox.Ok)