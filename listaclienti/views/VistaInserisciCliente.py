import datetime as dt
from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QHBoxLayout
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

        v_layout.addWidget(QLabel("Indirizzo"))
        self.text_indirizzo = QLineEdit(self)
        v_layout.addWidget(self.text_indirizzo)

        v_layout.addWidget(QLabel("Telefono"))
        self.text_telefono = QLineEdit(self)
        v_layout.addWidget(self.text_telefono)

        v_layout.addWidget(QLabel("Luogo nascita"))
        self.text_luogo_nascita = QLineEdit(self)
        v_layout.addWidget(self.text_luogo_nascita)

        v_layout.addWidget(QLabel("Data nascita"))

        v_layout_giorno = QVBoxLayout()
        v_layout_giorno.addWidget(QLabel("Giorno"))
        self.text_giorno_nascita = QLineEdit(self)
        v_layout_giorno.addWidget(self.text_giorno_nascita)

        v_layout_mese = QVBoxLayout()
        v_layout_mese.addWidget(QLabel("Mese"))
        self.text_mese_nascita = QLineEdit(self)
        v_layout_mese.addWidget(self.text_mese_nascita)

        v_layout_anno = QVBoxLayout()
        v_layout_anno.addWidget(QLabel("Anno"))
        self.text_anno_nascita = QLineEdit(self)
        v_layout_anno.addWidget(self.text_anno_nascita)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout_giorno)
        h_layout.addLayout(v_layout_mese)
        h_layout.addLayout(v_layout_anno)

        v_layout.addLayout(h_layout)

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
        giorno_nascita = self.text_giorno_nascita.text()
        mese_nascita = self.text_mese_nascita.text()
        anno_nascita = self.text_anno_nascita.text()
        luogo_nascita = self.text_luogo_nascita.text()
        telefono = self.text_telefono.text()
        indirizzo = self.text_indirizzo.text()

        if nome == "" or cognome == "" or cf == "" or giorno_nascita == "" or luogo_nascita == "" or telefono == "" \
                or indirizzo == "" or mese_nascita == "" or anno_nascita == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        elif self.controlla_data(anno_nascita, mese_nascita, giorno_nascita):
            data_nascita = dt.date(int(anno_nascita), int(mese_nascita), int(giorno_nascita))
            self.controller.aggiungi_cliente(
                Cliente(nome, cognome, cf, data_nascita, luogo_nascita, telefono, indirizzo))
            self.callback()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', "Indicare valori corretti per la data", QMessageBox.Ok, QMessageBox.Ok)

    def controlla_data(self, anno, mese, giorno):
        try:
            dt.date(int(anno), int(mese), int(giorno))
        except:
            return False
        return True