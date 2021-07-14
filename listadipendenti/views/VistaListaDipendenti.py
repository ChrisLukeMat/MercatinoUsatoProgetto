import json
import os

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton, QSizePolicy, QMessageBox

from listadipendenti.views.VistaInserisciDipendente import VistaInserisciDipendente
from listadipendenti.controller.ControllerListaDipendenti import ControllerListaDipendenti
from dipendente.views.VistaDipendente import VistaDipendente
from listadipendenti.views.VistaModificaDipendente import VistaModificaDipendente


class VistaListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)

        h_layout = QHBoxLayout()
        self.controller = ControllerListaDipendenti()
        self.list_view = QListView()
        self.update_ui()
        self.list_view.setMinimumSize(500, 400)
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(self.get_generic_button("Apri", self.show_selected_info))
        buttons_layout.addWidget(self.get_generic_button("Nuovo", self.show_new_dipendente))
        buttons_layout.addWidget(self.get_generic_button("Elimina", self.show_elimina_dipendente))
        buttons_layout.addWidget(self.get_generic_button("Modifica", self.show_modifica_dipendente))

        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(720, 400)
        self.setWindowTitle("Lista dipendenti")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setFixedWidth(350)
        button.setFixedHeight(100)
        button.setFont(QFont("Calibri", 12, QFont.Bold))
        button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        button.clicked.connect(on_click)
        return button

    def show_selected_info(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
            self.vista_dipendente = VistaDipendente(dipendente_selezionato)
            self.vista_dipendente.show()

    def show_new_dipendente(self):
        self.vista_inserisci_dipendente = VistaInserisciDipendente(self.controller, self.update_ui)
        self.vista_inserisci_dipendente.show()

    def show_modifica_dipendente(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
            self.vista_modifica_dipendente = VistaModificaDipendente(dipendente_selezionato, self.update_ui)
            self.vista_modifica_dipendente.show()

    def show_elimina_dipendente(self):
        if len(self.list_view.selectedIndexes()) > 0:
            selected = self.list_view.selectedIndexes()[0].row()
            dipendente_selezionato = self.controller.get_dipendente_by_index(selected)
            self.controller.rimuovi_dipendente_by_id(dipendente_selezionato.get_id_dipendente())
            lista_credenziali = []
            if os.path.isfile('accessocredenziali/credenziali.json'):
                with open('accessocredenziali/credenziali.json') as f:
                    lista_credenziali = json.load(f)
                    f.close()

                    for cred in lista_credenziali:
                        if cred.get("username") == dipendente_selezionato.get_username() and \
                           cred.get("password") == dipendente_selezionato.get_password():
                            lista_credenziali.remove(cred)
            with open('accessocredenziali/credenziali.json', 'w') as f:
                json.dump(lista_credenziali, f)
            self.update_ui()
            QMessageBox.critical(self, 'Eliminato', "Il dipendente: {} {} e' stato eliminato".format(dipendente_selezionato.nome,
                                                                                                    dipendente_selezionato.cognome),
                                     QMessageBox.Ok,
                                     QMessageBox.Ok)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for dipendente in self.controller.get_lista_dipendenti():
            item = QStandardItem()
            item.setText(dipendente.nome + " " + dipendente.cognome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(12)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()