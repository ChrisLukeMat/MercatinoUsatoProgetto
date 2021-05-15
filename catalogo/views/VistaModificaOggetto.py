from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QSizePolicy, QSpacerItem, QPushButton, QTextEdit, \
    QHBoxLayout, QMessageBox
import datetime as dt

class VistaModificaOggetto(QWidget):
    def __init__(self, oggetto, callback, parent=None):
        super(VistaModificaOggetto, self).__init__(parent)
        self.oggetto = oggetto
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        self.text_nome.setText(oggetto.nome)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Prezzo"))
        self.text_prezzo = QLineEdit(self)
        self.text_prezzo.setText(self.oggetto.prezzo)
        v_layout.addWidget(self.text_prezzo)

        v_layout.addWidget(QLabel("Proprietario"))
        self.text_proprietario = QLineEdit(self)
        self.text_nome.setText(self.oggetto.nome)
        v_layout.addWidget(self.text_proprietario)

        v_layout.addWidget(QLabel("Descrizione"))
        self.text_descrizione = QTextEdit(self)
        self.text_descrizione.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.text_descrizione.setAlignment(Qt.AlignTop)
        self.text_descrizione.setText(self.oggetto.descrizione)
        v_layout.addWidget(self.text_descrizione)

        v_layout.addWidget(QLabel("Categoria"))
        self.text_categoria = QLineEdit(self)
        v_layout.addWidget(self.text_categoria)

        v_layout.addWidget(QLabel("Data esposizione"))

        v_layout_giorno = QVBoxLayout()
        v_layout_giorno.addWidget(QLabel("Giorno"))
        self.text_giorno = QLineEdit(self)
        self.text_giorno.setText(str(self.oggetto.data_esposizione.day))
        v_layout_giorno.addWidget(self.text_giorno)

        v_layout_mese = QVBoxLayout()
        v_layout_mese.addWidget(QLabel("Mese"))
        self.text_mese = QLineEdit(self)
        self.text_mese.setText(str(self.oggetto.data_esposizione.month))
        v_layout_mese.addWidget(self.text_mese)

        v_layout_anno = QVBoxLayout()
        v_layout_anno.addWidget(QLabel("Anno"))
        self.text_anno = QLineEdit(self)
        self.text_anno.setText(str(self.oggetto.data_esposizione.year))
        v_layout_anno.addWidget(self.text_anno)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout_giorno)
        h_layout.addLayout(v_layout_mese)
        h_layout.addLayout(v_layout_anno)

        v_layout.addLayout(h_layout)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.modifica_oggetto)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.resize(300, 450)
        self.setWindowTitle('Nuovo Oggetto')

    def modifica_oggetto(self):
        nome = self.text_nome.text()
        prezzo = self.text_prezzo.text()
        proprietario = self.lista_clienti_salvata[self.combo_clienti.currentIndex()]
        giorno_esposizione = self.text_giorno.text()
        mese_esposizione = self.text_mese.text()
        anno_esposizione = self.text_anno.text()
        descrizione = self.text_descrizione.toPlainText()
        categoria = self.text_categoria.text()

        if nome == "" or prezzo == "" or proprietario == "" or descrizione == "" or categoria == "" or giorno_esposizione == "" or mese_esposizione == "" or anno_esposizione == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste",
                                 QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                data_esposizione = dt.date(int(anno_esposizione), int(mese_esposizione), int(giorno_esposizione))
                self.oggetto.set_nome(nome)
                self.oggetto.set_prezzo(prezzo)
                self.oggetto.set_proprietario(proprietario)
                self.oggetto.set_data_esposizione(data_esposizione)
                self.oggetto.set_descrizione(descrizione)
                self.oggetto.set_categoria(categoria)
                self.callback()
                self.close()
            except ValueError:
                QMessageBox.critical(self, 'Errore', "Data non corretta",
                                     QMessageBox.Ok, QMessageBox.Ok)