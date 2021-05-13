from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QHBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
from datetime import datetime
import datetime as dt
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
        '''
        v_layout.addWidget(QLabel("Data esposizione"))
        self.text_data_esposizione = QLineEdit(self)
        self.text_data_esposizione.setText(datetime.now().strftime('%d-%m-%Y'))
        v_layout.addWidget(self.text_data_esposizione)
        '''
        v_layout.addWidget(QLabel("Descrizione"))
        self.text_descrizione = QTextEdit(self)
        self.text_descrizione.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.text_descrizione.setAlignment(Qt.AlignTop)
        v_layout.addWidget(self.text_descrizione)

        v_layout.addWidget(QLabel("Categoria"))
        self.text_categoria = QLineEdit(self)
        v_layout.addWidget(self.text_categoria)


        v_layout.addWidget(QLabel("Data esposizione"))

        v_layout_giorno = QVBoxLayout()
        v_layout_giorno.addWidget(QLabel("Giorno"))
        self.text_giorno = QLineEdit(self)
        self.text_giorno.setText(datetime.now().strftime('%d'))
        v_layout_giorno.addWidget(self.text_giorno)

        v_layout_mese = QVBoxLayout()
        v_layout_mese.addWidget(QLabel("Mese"))
        self.text_mese = QLineEdit(self)
        self.text_mese.setText(datetime.now().strftime('%m'))
        v_layout_mese.addWidget(self.text_mese)

        v_layout_anno = QVBoxLayout()
        v_layout_anno.addWidget(QLabel("Anno"))
        self.text_anno = QLineEdit(self)
        self.text_anno.setText(datetime.now().strftime('%Y'))
        v_layout_anno.addWidget(self.text_anno)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout_giorno)
        h_layout.addLayout(v_layout_mese)
        h_layout.addLayout(v_layout_anno)

        v_layout.addLayout(h_layout)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_oggetto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.resize(300, 450)
        self.setWindowTitle('Nuovo Oggetto')

    def add_oggetto(self):
        nome = self.text_nome.text()
        prezzo = self.text_prezzo.text()
        proprietario = self.text_proprietario.text()
        giorno_esposizione = self.text_giorno.text()
        mese_esposizione = self.text_mese.text()
        anno_esposizione = self.text_anno.text()
        descrizione = self.text_descrizione.toPlainText()
        categoria = self.text_categoria.text()

        if nome == "" or prezzo == "" or proprietario == "" or descrizione == "" or categoria == "" or giorno_esposizione == "" or mese_esposizione == "" or anno_esposizione == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                data_esposizione = dt.date(int(anno_esposizione), int(mese_esposizione), int(giorno_esposizione))
                self.controller.aggiungi_oggetto(
                    Oggetto(nome, proprietario, prezzo, data_esposizione, descrizione, categoria))
                self.callback()
                self.close()
            except ValueError:
                QMessageBox.critical(self, 'Errore', "Data non corretta",
                                     QMessageBox.Ok, QMessageBox.Ok)