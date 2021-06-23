import os
import pickle
import datetime as dt

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton, \
    QComboBox, QMessageBox

from catalogo.controller.ControllerCatalogo import ControllerCatalogo
from listaclienti.controller.ControllerListaClienti import ControllerListaClienti
from transazione.model.Transazione import Transazione


class VistaInserisciTransazione(QWidget):
    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciTransazione, self).__init__(parent)
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()

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

        v_layout.addWidget(QLabel("Acquirente"))
        v_layout.addWidget(self.combo_clienti)

        self.combo_catalogo = QComboBox()
        self.combo_catalogo_model = QStandardItemModel(self.combo_catalogo)

        if os.path.isfile('catalogo/data/catalogo_salvato.pickle'):
            with open('catalogo/data/catalogo_salvato.pickle', 'rb') as f:
                self.catalogo_salvato = pickle.load(f)
            for oggetto in self.catalogo_salvato:
                item = QStandardItem()
                item.setText(oggetto.nome + " " + str(oggetto.prezzo) + " €  " + oggetto.id)
                item.setEditable(False)
                font = item.font()
                font.setPointSize(18)
                item.setFont(font)
                self.combo_catalogo_model.appendRow(item)
            self.combo_catalogo.setModel(self.combo_catalogo_model)

        v_layout.addWidget(QLabel("Oggetto venduto"))
        v_layout.addWidget(self.combo_catalogo)

        v_layout.addWidget(QLabel("Data acquisto"))

        v_layout_giorno = QVBoxLayout()
        v_layout_giorno.addWidget(QLabel("Giorno"))
        self.text_giorno_acquisto = QLineEdit(self)
        self.text_giorno_acquisto.setText(str(dt.date.today().day))
        v_layout_giorno.addWidget(self.text_giorno_acquisto)

        v_layout_mese = QVBoxLayout()
        v_layout_mese.addWidget(QLabel("Mese"))
        self.text_mese_acquisto = QLineEdit(self)
        self.text_mese_acquisto.setText(str(dt.date.today().month))
        v_layout_mese.addWidget(self.text_mese_acquisto)

        v_layout_anno = QVBoxLayout()
        v_layout_anno.addWidget(QLabel("Anno"))
        self.text_anno_acquisto = QLineEdit(self)
        self.text_anno_acquisto.setText(str(dt.date.today().year))
        v_layout_anno.addWidget(self.text_anno_acquisto)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout_giorno)
        h_layout.addLayout(v_layout_mese)
        h_layout.addLayout(v_layout_anno)

        v_layout.addLayout(h_layout)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_transazione)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.resize(300, 300)
        self.setWindowTitle('Nuova Transazione')

    def add_transazione(self):
        giorno_acquisto = self.text_giorno_acquisto.text()
        mese_acquisto = self.text_mese_acquisto.text()
        anno_acquisto = self.text_anno_acquisto.text()

        #controller_clienti = ControllerListaClienti()
        if giorno_acquisto == "" or mese_acquisto == "" or anno_acquisto == "":
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                #acquirente = self.controller_lista_clienti.get_cliente_by_index(self.combo_clienti.currentIndex())
                acquirente = self.lista_clienti_salvata[self.combo_clienti.currentIndex()]
                #oggetto_venduto = self.controller_catalogo.get_oggetto_by_index(self.combo_catalogo.currentIndex())
                oggetto_venduto = self.catalogo_salvato[self.combo_catalogo.currentIndex()]

                if acquirente.get_id_cliente() == oggetto_venduto.proprietario.get_id_cliente():
                    QMessageBox.critical(self, 'Errore', "L' acquirente non può essere il proprietario dell' oggetto!",
                                         QMessageBox.Ok, QMessageBox.Ok)
                else:
                    data_acquisto = dt.date(int(anno_acquisto), int(mese_acquisto), int(giorno_acquisto))

                    transazione = Transazione(oggetto_venduto, acquirente, data_acquisto)
                    self.controller.aggiungi_transazione(transazione)

                    saldo_str = oggetto_venduto.prezzo
                    saldo_parziale = float(saldo_str) / 2

                    for cliente in self.lista_clienti_salvata:
                        if oggetto_venduto.proprietario.get_nome() == cliente.nome and\
                                oggetto_venduto.proprietario.get_cognome() == cliente.cognome and\
                                oggetto_venduto.proprietario.get_id_cliente() == cliente.id_cliente:
                            cliente.set_saldo(float(cliente.get_saldo()) + saldo_parziale)
                            break

                    with open('listaclienti/data/lista_clienti_salvata.pickle', 'wb') as handle:
                        pickle.dump(self.lista_clienti_salvata, handle, pickle.HIGHEST_PROTOCOL)

                    for oggetto in self.catalogo_salvato:
                        if oggetto_venduto.nome == oggetto.nome and oggetto_venduto.prezzo == oggetto.prezzo and oggetto_venduto.id == oggetto.id:
                            self.catalogo_salvato.remove(oggetto)

                    with open('catalogo/data/catalogo_salvato.pickle', 'wb') as handle:
                        pickle.dump(self.catalogo_salvato, handle, pickle.HIGHEST_PROTOCOL)

                    self.callback()
                    self.close()
            except ValueError:
                QMessageBox.critical(self, 'Errore', "Data non corretta",
                                    QMessageBox.Ok, QMessageBox.Ok)
            except IndexError or AttributeError:
                QMessageBox.critical(self, 'Errore', "E' necessario inserire almeno un cliente e un oggetto!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            '''
            except AttributeError:
                QMessageBox.critical(self, 'Errore', "E' necessario inserire almeno un cliente e un oggetto!",
                                     QMessageBox.Ok, QMessageBox.Ok)
            '''