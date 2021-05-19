import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel, QVBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QPushButton, \
    QHBoxLayout, QTextEdit, QComboBox
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

        self.combo_clienti = QComboBox()
        self.comboclienti_model = QStandardItemModel(self.combo_clienti)
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                self.lista_clienti_salvata = pickle.load(f)

            for cliente in self.lista_clienti_salvata:
                item = QStandardItem()
                item.setText(cliente.nome + " " + cliente.cognome + " " + cliente.id_cliente)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.comboclienti_model.appendRow(item)
            self.combo_clienti.setModel(self.comboclienti_model)

        v_layout.addWidget(QLabel("Proprietario"))
        v_layout.addWidget(self.combo_clienti)

        v_layout.addWidget(QLabel("Descrizione (facoltativo)"))
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
        giorno_esposizione = self.text_giorno.text()
        mese_esposizione = self.text_mese.text()
        anno_esposizione = self.text_anno.text()
        descrizione = self.text_descrizione.toPlainText()
        categoria = self.text_categoria.text()

        if nome == "" or prezzo == "" or categoria == "" or giorno_esposizione == "" or mese_esposizione == "" or anno_esposizione == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                proprietario = self.lista_clienti_salvata[self.combo_clienti.currentIndex()]
                data_esposizione = dt.date(int(anno_esposizione), int(mese_esposizione), int(giorno_esposizione))
                self.controller.aggiungi_oggetto(
                    Oggetto(nome, proprietario, float(prezzo), data_esposizione, descrizione, categoria))
                self.callback()
                self.close()
            except ValueError:
                QMessageBox.critical(self, 'Errore', "Formato dei dati non corretto!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            except IndexError:
                QMessageBox.critical(self, 'Errore', "E' necessario inserire almeno un cliente!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            except AttributeError:
                QMessageBox.critical(self, 'Errore', "E' necessario inserire almeno un cliente!",
                                     QMessageBox.Ok, QMessageBox.Ok)