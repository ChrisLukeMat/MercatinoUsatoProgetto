from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QPushButton
from PyQt5.QtCore import Qt

from oggetto.model.Oggetto import Oggetto


class VistaInserisciOggetto(QWidget):
    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciOggetto, self).__init__(parent)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Prezzo"))
        self.text_prezzo = QLineEdit(self)
        v_layout.addWidget(self.text_prezzo)

        v_layout.addWidget(QLabel("Proprietario"))
        self.text_proprietario = QLineEdit(self)
        v_layout.addWidget(self.text_proprietario)

        v_layout.addWidget(QLabel("Data esposizione"))
        self.text_data_esposizione = QLineEdit(self)
        v_layout.addWidget(self.text_data_esposizione)

        v_layout.addWidget(QLabel("Descrizione"))
        self.text_descrizione = QLineEdit(self)
        self.text_descrizione.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.text_descrizione.setAlignment(Qt.AlignTop)
        v_layout.addWidget(self.text_descrizione)

        v_layout.addWidget(QLabel("Categoria"))
        self.text_categoria = QLineEdit(self)
        v_layout.addWidget(self.text_categoria)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_oggetto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.resize(300,450)
        self.setWindowTitle('Nuovo Oggetto')

    def add_oggetto(self):
        nome = self.text_nome.text()
        prezzo = self.text_prezzo.text()
        proprietario = self.text_proprietario.text()
        data_esposizione = self.text_data_esposizione.text()
        descrizione = self.text_descrizione.text()
        categoria = self.text_categoria.text()

        if nome == "" or prezzo == "" or proprietario == "" or data_esposizione == "" or descrizione == "" or categoria == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_oggetto(
                Oggetto(nome, proprietario, prezzo, data_esposizione, descrizione, categoria))
            self.callback()
            self.close()
